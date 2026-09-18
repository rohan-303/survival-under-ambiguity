"""Small LP reference solver for exact finite-grid audit bounds."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.optimize import linprog

from .audit_models import AuditRegime, AuditSpec
from .finite_grid import label_mixed_operator


@dataclass(frozen=True)
class BoundResult:
    lower: float | None
    upper: float | None
    status: str
    message: str
    primal_residual: float | None
    lower_dual: tuple[float, ...] = ()
    upper_dual: tuple[float, ...] = ()


def _solve(c: np.ndarray, a_ub: np.ndarray, b_ub: np.ndarray,
           a_eq: np.ndarray, b_eq: np.ndarray) -> tuple[float | None, str, str, float | None, tuple[float, ...]]:
    n = len(c)
    res = linprog(c, A_ub=a_ub if len(a_ub) else None, b_ub=b_ub if len(a_ub) else None,
                  A_eq=a_eq if len(a_eq) else None, b_eq=b_eq if len(a_eq) else None,
                  bounds=[(0.0, None)] * n, method="highs")
    if not res.success:
        return None, res.status.__str__(), res.message, None, ()
    residual = 0.0
    if len(a_ub):
        residual = max(residual, float(np.max(a_ub @ res.x - b_ub)))
    if len(a_eq):
        residual = max(residual, float(np.max(np.abs(a_eq @ res.x - b_eq))))
    dual = tuple(float(x) for x in getattr(res.ineqlin, "marginals", []))
    return float(res.fun), "OPTIMAL", res.message, residual, dual


def _conditional_problem(operators: list[np.ndarray], recorded: np.ndarray,
                         spec: AuditSpec) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    groups = len(operators)
    spec.validate(groups)
    pi = np.asarray(spec.prevalences, dtype=float)
    obs_per_group = operators[0].shape[0]
    latent_per_group = operators[0].shape[1]
    r = np.asarray(recorded, dtype=float)
    if r.size != groups * obs_per_group:
        raise ValueError("recorded law has wrong size")
    if np.any(r < -1e-12) or not np.isclose(r.sum(), 1.0):
        raise ValueError("recorded law must be a probability vector")

    if spec.regime == AuditRegime.A4_KNOWN_LABEL_CHANNEL:
        b = label_mixed_operator(operators, pi, np.asarray(spec.label_matrix, dtype=float))
    else:
        b = np.zeros((groups * obs_per_group, groups * latent_per_group))
        for g, a in enumerate(operators):
            b[g * obs_per_group:(g + 1) * obs_per_group,
              g * latent_per_group:(g + 1) * latent_per_group] = pi[g] * a
    a_ub = (1.0 - spec.epsilon) * b
    b_ub = r.copy()
    a_eq = np.zeros((groups, groups * latent_per_group))
    for g in range(groups):
        a_eq[g, g * latent_per_group:(g + 1) * latent_per_group] = 1.0
    b_eq = np.ones(groups)

    # A2 requires observed and clean group marginals to agree. A3 adds a
    # conditional contamination-cap feasibility condition. Under fixed pi and
    # fixed R these constraints are data-contract checks, not hidden width gains.
    observed_group_mass = r.reshape(groups, obs_per_group).sum(1)
    if spec.regime == AuditRegime.A2_MARGINAL_PRESERVING and not np.allclose(observed_group_mass, pi):
        a_ub = np.vstack([a_ub, np.zeros((groups, groups * latent_per_group))])
        b_ub = np.r_[b_ub, np.full(groups, -1.0)]
    if spec.regime == AuditRegime.A3_GROUP_CAPS:
        caps = np.asarray(spec.group_caps, dtype=float)
        implied_q_mass = observed_group_mass - (1.0 - spec.epsilon) * pi
        slack = pi * caps - implied_q_mass
        a_ub = np.vstack([a_ub, np.zeros((groups, groups * latent_per_group))])
        b_ub = np.r_[b_ub, slack]
    return b, a_ub, b_ub, a_eq, b_eq


def bound_conditional_functional(operators: list[np.ndarray], recorded: np.ndarray,
                                 spec: AuditSpec, group: int, weights: np.ndarray) -> BoundResult:
    """Bound a conditional group functional under A1-A4.

    A0 has unknown clean prevalence, making a conditional target a ratio; use
    `bound_joint_functional` for its linear joint-mass counterpart.
    """
    if spec.regime == AuditRegime.A0_GLOBAL_ONLY:
        raise ValueError("A0 conditional bounds require a linear-fractional solver; use joint bounds")
    _, a_ub, b_ub, a_eq, b_eq = _conditional_problem(operators, recorded, spec)
    latent = operators[0].shape[1]
    c = np.zeros(len(operators) * latent)
    c[group * latent:(group + 1) * latent] = np.asarray(weights, dtype=float)
    lo, st_lo, msg_lo, res_lo, dual_lo = _solve(c, a_ub, b_ub, a_eq, b_eq)
    hi_neg, st_hi, msg_hi, res_hi, dual_hi = _solve(-c, a_ub, b_ub, a_eq, b_eq)
    if lo is None or hi_neg is None:
        return BoundResult(None, None, "INFEASIBLE", f"lower={msg_lo}; upper={msg_hi}", None)
    return BoundResult(lo, -hi_neg, "OPTIMAL", msg_lo, max(res_lo or 0, res_hi or 0), dual_lo, dual_hi)


def bound_joint_functional(operators: list[np.ndarray], recorded: np.ndarray,
                           epsilon: float, group: int, weights: np.ndarray) -> BoundResult:
    """A0 global-only bound for the linear joint functional pi_g*psi_g."""
    groups = len(operators)
    obs = operators[0].shape[0]
    latent = operators[0].shape[1]
    r = np.asarray(recorded, dtype=float)
    if r.size != groups * obs or np.any(r < -1e-12) or not np.isclose(r.sum(), 1.0):
        raise ValueError("recorded law must be a probability vector")
    b = np.zeros((groups * obs, groups * latent))
    for g, op in enumerate(operators):
        b[g * obs:(g + 1) * obs, g * latent:(g + 1) * latent] = op
    a_ub = (1.0 - epsilon) * b
    c = np.zeros(groups * latent)
    c[group * latent:(group + 1) * latent] = np.asarray(weights, dtype=float)
    a_eq = np.ones((1, groups * latent)); b_eq = np.array([1.0])
    lo, _, msg_lo, res_lo, dual_lo = _solve(c, a_ub, r, a_eq, b_eq)
    hi_neg, _, msg_hi, res_hi, dual_hi = _solve(-c, a_ub, r, a_eq, b_eq)
    if lo is None or hi_neg is None:
        return BoundResult(None, None, "INFEASIBLE", f"lower={msg_lo}; upper={msg_hi}", None)
    return BoundResult(lo, -hi_neg, "OPTIMAL", msg_lo, max(res_lo or 0, res_hi or 0), dual_lo, dual_hi)
