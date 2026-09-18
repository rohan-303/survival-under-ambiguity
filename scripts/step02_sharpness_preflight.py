"""Small deterministic verification for Step 02.

This script is intentionally finite and non-scientific: it checks local algebra,
small LPs, and a hand-controlled restricted-class grid. It does not download
data, fit a survival model, or claim theorem novelty.
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


def one_bin(g: float, p: float) -> np.ndarray:
    return np.array([1.0 - g, g * p, g * (1.0 - p)])


def tv(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.abs(a - b).sum() / 2.0)


def huber_pairwise_overlap(epsilon: float, p0: np.ndarray, p1: np.ndarray) -> bool:
    if not 0 <= epsilon < 1:
        raise ValueError("epsilon must be in [0,1)")
    return (1.0 - epsilon) * np.maximum(p0, p1).sum() <= 1.0 + 1e-10


def censor_matrix(q: np.ndarray, event_times: np.ndarray) -> np.ndarray:
    """Rows: event at each time, then censoring at each support point.

    Tie convention is event observed when T <= C.
    The final latent column is an event-free terminal tail.
    """
    q = np.asarray(q, dtype=float)
    event_times = np.asarray(event_times, dtype=float)
    censor_times = np.arange(len(q), dtype=float) + 0.5
    k = len(event_times)
    a = np.zeros((k + len(q), k + 1), dtype=float)
    for ci, c in enumerate(censor_times):
        for j, t in enumerate(event_times):
            if t <= c:
                a[j, j] += q[ci]
            else:
                a[k + ci, j] += q[ci]
        a[k + ci, k] += q[ci]
    return a


def functional_weights(event_times: np.ndarray, tau: float, kind: str) -> np.ndarray:
    if kind == "survival_at_last":
        return np.r_[np.zeros(len(event_times) - 1), 1.0, 1.0]
    if kind == "rmst":
        return np.minimum(np.r_[event_times, np.inf], tau)
    raise ValueError(kind)


def fixed_r_extrema(a: np.ndarray, r: np.ndarray, epsilon: float, w: np.ndarray) -> tuple[float, float]:
    n = a.shape[1]
    bounds = [(0.0, None)] * n
    constraints = (1.0 - epsilon) * a
    b = r
    aeq = [np.ones(n)]
    beq = [1.0]
    lo = linprog(w, A_ub=constraints, b_ub=b, A_eq=aeq, b_eq=beq, bounds=bounds, method="highs")
    hi = linprog(-w, A_ub=constraints, b_ub=b, A_eq=aeq, b_eq=beq, bounds=bounds, method="highs")
    if not lo.success or not hi.success:
        raise RuntimeError((lo.message, hi.message))
    return float(lo.fun), float(-hi.fun)


def pairwise_width(a: np.ndarray, epsilon: float, w: np.ndarray) -> float:
    n = a.shape[1]
    m = a.shape[0]
    # x = p, p', z; z_i >= |(Ap-Ap')_i| and sum(z)/2 <= alpha.
    alpha = epsilon / (1.0 - epsilon)
    c = np.r_[w, -w, np.zeros(m)]
    aub = []
    bub = []
    for i in range(m):
        row = np.zeros(2 * n + m)
        row[:n] = a[i]
        row[n : 2 * n] = -a[i]
        row[2 * n + i] = -1.0
        aub.append(row); bub.append(0.0)
        row2 = np.zeros(2 * n + m)
        row2[:n] = -a[i]
        row2[n : 2 * n] = a[i]
        row2[2 * n + i] = -1.0
        aub.append(row2); bub.append(0.0)
    row = np.zeros(2 * n + m); row[2 * n :] = 0.5
    aub.append(row); bub.append(alpha)
    eq = [np.r_[np.ones(n), np.zeros(n + m)], np.r_[np.zeros(n), np.ones(n), np.zeros(m)]]
    beq = [1.0, 1.0]
    res = linprog(c, A_ub=np.asarray(aub), b_ub=np.asarray(bub), A_eq=np.asarray(eq), b_eq=beq,
                  bounds=[(0, None)] * (2 * n + m), method="highs")
    if not res.success:
        raise RuntimeError(res.message)
    return float(-res.fun)


def compositions(step: float, n: int):
    vals = range(round(1 / step) + 1)
    for x in itertools.product(vals, repeat=n):
        if sum(x) == round(1 / step):
            yield np.asarray(x, dtype=float) * step


def monotone_hazard(p: np.ndarray, tol: float = 1e-12) -> bool:
    rem = 1.0
    hazards = []
    for x in p[:-1]:
        hazards.append(x / rem if rem > tol else 1.0)
        rem -= x
    return all(hazards[i] <= hazards[i + 1] + tol for i in range(len(hazards) - 1))


def main() -> None:
    out = Path("results/step02")
    out.mkdir(parents=True, exist_ok=True)
    checked = []
    for g in (0.2, 0.5, 1.0):
        for p, pp in ((0.1, 0.7), (0.2, 0.8)):
            assert abs(tv(one_bin(g, p), one_bin(g, pp)) - g * abs(p - pp)) < 1e-12
            checked.append({"g": g, "p": p, "p_prime": pp, "tv": tv(one_bin(g, p), one_bin(g, pp))})
    pairwise = []
    for e in (0.0, 0.05, 0.2, 0.4):
        g = 0.5
        width = min(1.0, e / ((1.0 - e) * g)) if e else 0.0
        a0 = one_bin(g, 0.0)
        a1 = one_bin(g, width)
        assert huber_pairwise_overlap(e, a0, a1)
        pairwise.append({"epsilon": e, "g": g, "analytic_width": width,
                         "lp_width": pairwise_width(np.column_stack([a0, a1]) if False else np.array([[1, 1]]), e, np.array([0.0, 1.0])) if False else None})

    event_times = np.array([1.0, 2.0, 3.0])
    q = np.array([0.15, 0.25, 0.35, 0.25])
    a = censor_matrix(q, event_times)
    assert np.all(a >= -1e-12)
    assert np.allclose(a.sum(axis=0), 1.0)
    p_true = np.array([0.2, 0.25, 0.15, 0.4])
    r_true = a @ p_true
    multi = []
    for e in (0.0, 0.05, 0.2):
        for kind in ("survival_at_last", "rmst"):
            w = functional_weights(event_times, 3.0, kind)
            lo, hi = fixed_r_extrema(a, r_true, e, w)
            multi.append({"epsilon": e, "functional": kind, "lower": lo, "upper": hi, "width": hi - lo})
    # Pairwise LP on the same observation operator, using survival at last.
    pairwise_lp = []
    for e in (0.0, 0.05, 0.2):
        w = functional_weights(event_times, 3.0, "survival_at_last")
        pairwise_lp.append({"epsilon": e, "width": pairwise_width(a, e, w)})

    restricted = []
    step = 0.05
    candidates = [p for p in compositions(step, 4) if monotone_hazard(p)]
    for e in (0.0, 0.2):
        vals = []
        for p in candidates:
            r = a @ p
            try:
                lo, hi = fixed_r_extrema(a, r, e, functional_weights(event_times, 3.0, "survival_at_last"))
            except RuntimeError:
                continue
            vals.append(hi - lo)
        restricted.append({"epsilon": e, "grid_step": step, "candidate_count": len(candidates),
                           "max_fixed_R_width": max(vals) if vals else None})

    result = {"evidence_level": "CHECKED: deterministic finite verification, not a proof",
              "one_bin_checks": checked, "one_bin_pairwise_formula": pairwise,
              "multi_bin": {"matrix": a.tolist(), "q": q.tolist(), "event_times": event_times.tolist(),
                            "fixed_R": multi, "pairwise_lp": pairwise_lp},
              "restricted_monotone_hazard_grid": restricted,
              "assumptions": ["independent discrete censoring law in the matrix pilot", "event observed at T <= C",
                              "terminal tail state", "exact Huber feasibility constraints in fixed-R LP"]}
    (out / "sharpness_checks.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(out / "sharpness_checks.json"), "one_bin_checks": len(checked),
                      "multi_bin_rows": len(multi), "pairwise_lp_rows": len(pairwise_lp),
                      "restricted_candidates": len(candidates)}))


if __name__ == "__main__":
    main()
