"""Step 05 deterministic joint-RMST verification and gap phase study."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from scipy import __version__ as scipy_version

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from survival_ambiguity.identification import (  # noqa: E402
    censoring_operator, compatible_joint_set, coupling_gaps,
    pointwise_bounds, rmst_event_weights, rmst_survival_representation,
    rmst_bounds,
)


def capped_simplex_linear_bounds(cap: np.ndarray, objective: np.ndarray) -> tuple[float, float]:
    """Closed form min/max of c^T p over p>=0, sum p=1, p<=cap."""
    if np.any(cap < 0) or cap.sum() < 1 - 1e-10:
        raise ValueError("empty capped simplex")
    def fill(order):
        remaining = 1.0
        value = 0.0
        for i in order:
            take = min(float(cap[i]), remaining)
            value += take * float(objective[i])
            remaining -= take
        if remaining > 1e-8:
            raise ValueError("capped simplex is empty")
        return value
    return fill(np.argsort(objective)), fill(np.argsort(-objective))


def check_k2_identity() -> dict[str, object]:
    rows = []
    times = np.array([1.0, 2.0])
    for e in (0.0, 0.05, 0.2, 0.4):
        for r in (np.array([0.1, 0.3, 0.6]), np.array([0.4, 0.4, 0.2])):
            a = np.eye(3)
            p = np.array([0.2, 0.3, 0.5])
            recorded = (1 - e) * p + e * r
            poly = compatible_joint_set(a, recorded, e)
            for c in (rmst_event_weights(times, 3.0),
                      np.array([0.0, 1.0, 1.0]),
                      np.array([0.0, 0.0, 1.0])):
                analytic = capped_simplex_linear_bounds(recorded / (1 - e), c) if e < 1 else None
                solved = rmst_bounds(poly, times, 3.0) if np.allclose(c, rmst_event_weights(times, 3.0)) else None
                if solved is None:
                    from survival_ambiguity.identification.joint_survival import bound_linear
                    solved = bound_linear(poly, c)
                if not np.allclose([solved.lower, solved.upper], analytic, atol=2e-8):
                    raise AssertionError((e, r, c, analytic, solved))
                rows.append({"epsilon": e, "recorded": r.tolist(),
                             "objective": c.tolist(), "analytic": analytic,
                             "lp": [solved.lower, solved.upper]})
    return {"rows": rows, "count": len(rows)}


def phase_study() -> dict[str, object]:
    rows = []
    max_gap = 0.0
    for k in (2, 3, 5):
        times = np.arange(1, k + 1, dtype=float)
        q_patterns = [
            np.ones(k + 1) / (k + 1),
            np.linspace(1, k + 1, k + 1) / ((k + 1) * (k + 2) / 2),
        ]
        p_patterns = [
            np.ones(k + 1) / (k + 1),
            np.arange(1, k + 2, dtype=float) / ((k + 1) * (k + 2) / 2),
        ]
        for q in q_patterns:
            a = censoring_operator(q, times)
            for e in (0.0, 0.05, 0.1, 0.2):
                for p in p_patterns:
                    contam = np.roll(np.arange(1, a.shape[0] + 1, dtype=float), 1)
                    contam /= contam.sum()
                    r = (1 - e) * (a @ p) + e * contam
                    poly = compatible_joint_set(a, r, e)
                    out = coupling_gaps(poly, times, float(k) + 0.5)
                    max_gap = max(max_gap, float(out["gamma_width"]))
                    rows.append({"k": k, "epsilon": e, "q": q.tolist(),
                                 "p": p.tolist(), **out})
    return {"rows": rows, "count": len(rows), "max_gamma_width": max_gap}


def main() -> None:
    identity = check_k2_identity()
    phase = phase_study()
    counterexamples = {
        "strict_gap_found_in_structured_censoring_grid": phase["max_gamma_width"] > 2e-8,
        "step04_unweighted_sum_was_not_rmst_pointwise_width": True,
        "interpretation": "The earlier apparent gap compared an unweighted sum of pointwise widths with an RMST width. Correct RMST survival weights eliminate that comparison error in the checked scenario.",
        "k2_identity_closed_form_verified": True,
        "tested_structured_cases": phase["count"],
    }
    out_dir = ROOT / "results" / "step05"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "joint_rmst_checks.json").write_text(json.dumps({
        "scipy_version": scipy_version, "tolerance": 2e-8,
        "identity_k2": identity, "phase_study": phase,
        "counterexamples": counterexamples,
        "status": "CHECKED_NOT_PROVED",
    }, indent=2) + "\n", encoding="utf-8")
    (out_dir / "counterexamples.json").write_text(json.dumps(counterexamples, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"identity_rows": identity["count"], "phase_rows": phase["count"],
                      "max_gamma_width": phase["max_gamma_width"],
                      "output": str(out_dir / "joint_rmst_checks.json")}, indent=2))


if __name__ == "__main__":
    main()
