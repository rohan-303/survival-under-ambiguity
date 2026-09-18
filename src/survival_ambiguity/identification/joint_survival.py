"""Joint survival-set and RMST geometry on an exact finite-grid polytope."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np
from scipy.optimize import linprog


@dataclass(frozen=True)
class LPResult:
    lower: float | None
    upper: float | None
    status: str
    message: str
    residual: float | None
    optimizer_upper: tuple[float, ...] = ()
    optimizer_lower: tuple[float, ...] = ()


@dataclass(frozen=True)
class JointSet:
    """Exact compatibility polytope for one latent event-mass vector."""

    operator: np.ndarray
    recorded: np.ndarray
    epsilon: float
    equality_matrix: np.ndarray
    equality_rhs: np.ndarray
    inequality_matrix: np.ndarray
    inequality_rhs: np.ndarray

    @property
    def dimension(self) -> int:
        return self.operator.shape[1]

    @property
    def constraint_count(self) -> tuple[int, int]:
        return self.equality_matrix.shape[0], self.inequality_matrix.shape[0]

    def validate(self) -> None:
        if self.dimension != self.equality_matrix.shape[1]:
            raise ValueError("inconsistent polytope dimensions")
        if np.any(self.inequality_matrix @ np.zeros(self.dimension) - self.inequality_rhs > 1e-10):
            raise ValueError("inconsistent zero check")


def compatible_joint_set(operator: np.ndarray, recorded: np.ndarray, epsilon: float) -> JointSet:
    """Construct P_epsilon(R,q) from exact Huber residual nonnegativity."""
    a = np.asarray(operator, dtype=float)
    r = np.asarray(recorded, dtype=float)
    if a.ndim != 2 or r.ndim != 1 or a.shape[0] != r.size:
        raise ValueError("operator and recorded law have incompatible shapes")
    if np.any(a < -1e-12) or np.any(r < -1e-12) or not np.isclose(a.sum(0), 1).all():
        raise ValueError("operator/recorded law must be nonnegative and stochastic")
    if not 0 <= epsilon < 1 or not np.isclose(r.sum(), 1):
        raise ValueError("invalid epsilon or recorded law")
    k = a.shape[1]
    eq = np.ones((1, k))
    # p >= 0 is supplied as LP bounds; exact Q existence is H p <= R.
    return JointSet(a, r, epsilon, eq, np.array([1.0]),
                    (1.0 - epsilon) * a, r.copy())


def survival_map(event_times: np.ndarray, horizons: Iterable[float] | None = None) -> np.ndarray:
    """Map event masses (plus tail) to S(t)=P(T>t)."""
    times = np.asarray(event_times, dtype=float)
    hs = times if horizons is None else np.asarray(list(horizons), dtype=float)
    if times.ndim != 1 or np.any(np.diff(times) <= 0):
        raise ValueError("event times must be strictly increasing")
    return np.asarray([np.r_[times > h, True].astype(float) for h in hs])


def _solve(poly: JointSet, objective: np.ndarray, extra_eq: np.ndarray | None = None,
           extra_rhs: np.ndarray | None = None) -> tuple[float | None, str, str, float | None, np.ndarray | None]:
    eq = poly.equality_matrix if extra_eq is None else np.vstack([poly.equality_matrix, extra_eq])
    rhs = poly.equality_rhs if extra_rhs is None else np.r_[poly.equality_rhs, extra_rhs]
    out = linprog(objective, A_ub=poly.inequality_matrix, b_ub=poly.inequality_rhs,
                  A_eq=eq, b_eq=rhs, bounds=[(0.0, None)] * poly.dimension, method="highs")
    if not out.success:
        return None, "INFEASIBLE", out.message, None, None
    residual = max(float(np.max(poly.inequality_matrix @ out.x - poly.inequality_rhs)),
                   float(np.max(np.abs(eq @ out.x - rhs))))
    return float(out.fun), "OPTIMAL", out.message, residual, out.x


def bound_linear(poly: JointSet, objective: np.ndarray) -> LPResult:
    c = np.asarray(objective, dtype=float)
    if c.shape != (poly.dimension,):
        raise ValueError("objective has wrong dimension")
    lo, sl, ml, rl, xl = _solve(poly, c)
    hi_neg, su, mu, ru, xu = _solve(poly, -c)
    if lo is None or hi_neg is None:
        return LPResult(None, None, "INFEASIBLE", f"lower={ml}; upper={mu}", None)
    return LPResult(lo, -hi_neg, "OPTIMAL", ml, max(rl or 0, ru or 0),
                    tuple(float(v) for v in xu), tuple(float(v) for v in xl))


def pointwise_bounds(poly: JointSet, event_times: np.ndarray) -> tuple[np.ndarray, np.ndarray, list[LPResult]]:
    b = survival_map(event_times)
    results = [bound_linear(poly, row) for row in b]
    if any(x.status != "OPTIMAL" for x in results):
        raise ValueError("infeasible pointwise problem")
    return np.array([x.lower for x in results]), np.array([x.upper for x in results]), results


def rmst_event_weights(event_times: np.ndarray, tau: float) -> np.ndarray:
    """Direct E[min(T,tau)] coefficients for event masses plus a terminal tail."""
    if tau <= 0:
        raise ValueError("tau must be positive")
    times = np.asarray(event_times, dtype=float)
    return np.minimum(np.r_[times, np.inf], tau)


def rmst_survival_representation(event_times: np.ndarray, tau: float) -> tuple[float, np.ndarray]:
    """Return constant and nonnegative survival weights for the same RMST."""
    times = np.asarray(event_times, dtype=float)
    if tau < times[0]:
        return tau, np.zeros(len(times))
    active = times[times < tau]
    if not len(active):
        return tau, np.zeros(len(times))
    weights = np.zeros(len(times))
    for j in range(len(times)):
        left = times[j]
        right = tau if j == len(times) - 1 else min(times[j + 1], tau)
        weights[j] = max(0.0, right - left)
    return min(times[0], tau), weights


def rmst_bounds(poly: JointSet, event_times: np.ndarray, tau: float) -> LPResult:
    return bound_linear(poly, rmst_event_weights(event_times, tau))


def common_endpoint_feasible(poly: JointSet, survival_targets: np.ndarray,
                             event_times: np.ndarray, tolerance: float = 1e-8) -> bool:
    b = survival_map(event_times)
    target = np.asarray(survival_targets, dtype=float)
    if target.shape != (b.shape[0],):
        raise ValueError("target has wrong shape")
    _, status, _, residual, _ = _solve(poly, np.zeros(poly.dimension), b, target)
    return status == "OPTIMAL" and (residual if residual is not None else np.inf) <= tolerance


def coupling_gaps(poly: JointSet, event_times: np.ndarray, tau: float) -> dict[str, float | bool]:
    lower, upper, _ = pointwise_bounds(poly, event_times)
    constant, weights = rmst_survival_representation(event_times, tau)
    direct = rmst_bounds(poly, event_times, tau)
    if direct.status != "OPTIMAL":
        raise ValueError("infeasible RMST problem")
    naive_lower = constant + float(weights @ lower)
    naive_upper = constant + float(weights @ upper)
    upper_gap = naive_upper - direct.upper
    lower_gap = direct.lower - naive_lower
    active = weights > 1e-12
    upper_common = common_endpoint_feasible(poly, upper[active], np.asarray(event_times)[active])
    lower_common = common_endpoint_feasible(poly, lower[active], np.asarray(event_times)[active])
    return {
        "rmst_lower": float(direct.lower), "rmst_upper": float(direct.upper),
        "pointwise_lower": float(naive_lower), "pointwise_upper": float(naive_upper),
        "gamma_minus": float(lower_gap), "gamma_plus": float(upper_gap),
        "gamma_width": float(upper_gap + lower_gap),
        "upper_common_attainable": bool(upper_common),
        "lower_common_attainable": bool(lower_common),
    }
