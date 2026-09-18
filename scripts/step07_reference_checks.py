"""Deterministic Step 07 exact checks and compact result artifacts."""
from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from survival_ambiguity.audit import (
    confidence_bounds_m, coverage, clean_audit_survival_width,
    enumerate_allocations, hypergeom_pmf,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "step07"
OUT.mkdir(parents=True, exist_ok=True)


def main() -> None:
    alpha = 0.05
    coverage_rows = []
    for n, b in [(5, 0), (5, 2), (5, 5), (8, 3), (12, 6)]:
        vals = [coverage(n, m, b, alpha) for m in range(n + 1)]
        coverage_rows.append({"N": n, "b": b, "min_coverage": min(vals), "coverage_by_M": vals})

    sample_rows = []
    for n in (20, 50):
        for g in (1.0, 0.5, 0.2):
            for delta in (0.10, 0.20):
                eligible = [b for b in range(n + 1)
                            if clean_audit_survival_width(n, b, alpha, g) <= delta + 1e-12]
                sample_rows.append({"N": n, "alpha": alpha, "g": g, "delta": delta,
                                    "b_star_clean_outcome": min(eligible) if eligible else None,
                                    "width_at_b_star": clean_audit_survival_width(n, min(eligible), alpha, g) if eligible else None})

    # Exact one-bin reduction: survival width is the recorded certificate width / g,
    # capped at one. This table compares the computed implementation directly.
    reduction_rows = []
    for n, b, g in [(12, 0, 1.0), (12, 4, 0.5), (12, 8, 0.2), (12, 12, 0.5)]:
        u = confidence_bounds_m(n, b, 0, alpha)[1]
        recorded = min(n, 2 * u) / n
        survival = clean_audit_survival_width(n, b, alpha, g)
        reduction_rows.append({"N": n, "b": b, "g": g, "U_M_D0": u,
                               "recorded_width": recorded, "survival_width": survival,
                               "equals_capped_recorded_over_g": abs(survival - min(1.0, recorded / g)) < 1e-12})

    # A small exact allocation oracle under the clean-audit outcome. The objective
    # is a declared weighted sum of per-stratum worst-case survival widths.
    strata = ((20, 1.0, 0.6), (20, 0.2, 0.4))
    allocation_rows = []
    for B in (4, 8, 12):
        scored = []
        for alloc in enumerate_allocations(B, 2):
            objective = sum(pi * clean_audit_survival_width(n, b, alpha, g)
                            for (n, g, pi), b in zip(strata, alloc))
            scored.append((objective, alloc))
        scored.sort()
        allocation_rows.append({"B": B, "optimal_allocations": [list(x[1]) for x in scored if abs(x[0] - scored[0][0]) < 1e-12],
                                "minimum_weighted_width": scored[0][0],
                                "proportional_reference": [round(B / 2), B - round(B / 2)]})

    payload = {
        "step": 7,
        "model": "stratified exchangeable corruption-location model",
        "alpha": alpha,
        "coverage_checks": coverage_rows,
        "clean_audit_sample_complexity": sample_rows,
        "acceptance_sampling_reduction": reduction_rows,
        "allocation_oracle": allocation_rows,
        "two_bin_pilot": {"status": "NOT_COMPUTED", "reason": "one-bin direction failed the survival-specificity kill test"},
    }
    (OUT / "exchangeable_checks.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
