"""Step 04 deterministic checks and tiny multi-bin diagnostics."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from scipy import __version__ as scipy_version
from scipy.optimize import linprog

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from survival_ambiguity.identification import (  # noqa: E402
    AuditRegime, AuditSpec, bound_conditional_functional, censoring_operator,
    rmst_weights, survival_weights,
)


def one_bin_diameter_lp(epsilon: float, pi: float, followup: float) -> float:
    """Maximize |p-p'| over two clean worlds with one common contaminated R."""
    # two groups, one event mass and one tail mass per group; three observed cells
    # for each group: event, early censor, late censor.
    a = np.array([[0.0, 0.0], [1.0, 1.0], [followup, 0.0]])
    # columns sum to one; row 0 is the event cell, row 1 early censor, row 2 late event.
    b1 = pi * a
    b0 = (1 - pi) * a
    # x=(p1,p1',p0,p0',R), with p vectors each length 2 and R length 6.
    n = 8 + 6
    aub, bub = [], []
    for offset, b, g in ((0, b1, 0), (2, b1, 0), (4, b0, 1), (6, b0, 1)):
        # only group-specific blocks, inserted into full clean-record vector
        rowblock = np.zeros((6, n))
        xoff = offset
        # b is already scaled by its group prevalence
        for cell in range(3):
            for col in range(2):
                rowblock[g * 3 + cell, xoff + col] = (1 - epsilon) * b[cell, col]
        # R block dominates the clean mixture
        for cell in range(3):
            rowblock[g * 3 + cell, 8 + g * 3 + cell] -= 1
        aub.extend(rowblock)
        bub.extend(np.zeros(6))
    # The loop above duplicated whole rows; remove rows that are identically zero.
    aub = np.asarray(aub)
    bub = np.asarray(bub)
    keep = np.any(np.abs(aub) > 1e-14, axis=1)
    aub, bub = aub[keep], bub[keep]
    aeq = np.zeros((5, n)); beq = np.array([1, 1, 1, 1, 1.0])
    for row, off in enumerate((0, 2, 4, 6)):
        aeq[row, off:off + 2] = 1
    aeq[4, 8:] = 1
    # direction p1_event - p1'_event
    c = np.zeros(n); c[0] = -1; c[2] = 1
    out = []
    for sign in (1, -1):
        cc = sign * c
        res = linprog(cc, A_ub=aub, b_ub=bub, A_eq=aeq, b_eq=beq,
                       bounds=[(0, None)] * n, method="highs")
        if not res.success:
            raise RuntimeError(res.message)
        out.append(float(-res.fun))
    return max(out)


def main() -> None:
    rows = []
    for e in (0.0, 0.05, 0.2, 0.5):
        for pi in (0.1, 0.5, 0.9):
            for g in (0.25, 0.7, 1.0):
                analytic = min(1.0, e / ((1 - e) * pi * g)) if e else 0.0
                lp = one_bin_diameter_lp(e, pi, g)
                if not np.isclose(analytic, lp, atol=2e-8):
                    raise AssertionError((e, pi, g, analytic, lp))
                rows.append({"epsilon": e, "pi": pi, "followup": g,
                             "analytic": analytic, "lp": lp})

    times = np.array([0.25, 1.0, 2.0])
    ops = [censoring_operator(np.array([0.25, 0.25, 0.50]), times),
           censoring_operator(np.array([0.50, 0.25, 0.25]), times)]
    pi = (0.2, 0.8)
    clean = np.array([0.30, 0.25, 0.15, 0.30, 0.10, 0.25, 0.20, 0.15])
    # use valid conditional mass vectors (4 entries per group)
    clean = np.array([0.30, 0.20, 0.20, 0.30, 0.10, 0.20, 0.30, 0.40])
    clean_recorded = np.r_[pi[0] * ops[0] @ clean[:4], pi[1] * ops[1] @ clean[4:]]
    contaminant = np.full(clean_recorded.shape, 1 / clean_recorded.size)
    recorded = 0.9 * clean_recorded + 0.1 * contaminant
    spec = AuditSpec(AuditRegime.A1_TRUSTED_MARGINAL, 0.1, pi)
    multi = []
    for group in (0, 1):
        for horizon in (0.25, 1.0, 2.0):
            w = survival_weights(times, horizon)
            out = bound_conditional_functional(ops, recorded, spec, group, w)
            multi.append({"group": group, "functional": f"S({horizon})",
                          "lower": out.lower, "upper": out.upper,
                          "width": out.upper - out.lower, "status": out.status})
        w = rmst_weights(times, 2.5)
        out = bound_conditional_functional(ops, recorded, spec, group, w)
        multi.append({"group": group, "functional": "RMST(2.5)",
                      "lower": out.lower, "upper": out.upper,
                      "width": out.upper - out.lower, "status": out.status})
    result = {"scipy_version": scipy_version, "tolerance": 2e-8,
              "one_bin_checks": rows, "multi_bin_checks": multi,
              "notes": ["population LP diagnostics only", "no finite-sample inference"]}
    out_path = ROOT / "results" / "step04" / "audit_checks.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"one_bin_rows": len(rows), "multi_bin_rows": len(multi),
                      "scipy_version": scipy_version, "output": str(out_path)}, indent=2))


if __name__ == "__main__":
    main()
