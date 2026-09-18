"""Deterministic Step 03 rare-group fragility verification.

This is a finite algebra/LP sanity suite. It does not estimate a population,
fit a survival model, or establish literature novelty.
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.step02_sharpness_preflight import censor_matrix, pairwise_width


def clipped_diameter(epsilon: float, mass: float, followup: float) -> float:
    if mass < 0 or followup < 0 or epsilon < 0 or epsilon >= 1:
        raise ValueError("invalid parameter")
    if mass == 0 or followup == 0:
        return 1.0
    return min(1.0, epsilon / ((1.0 - epsilon) * mass * followup))


def critical_epsilon(mass: float, followup: float) -> float:
    if mass <= 0 or followup <= 0:
        return 0.0
    return (mass * followup) / (1.0 + mass * followup)


def prevalence_interval(observed_prevalence: float, epsilon: float) -> tuple[float, float]:
    """Whole-row Huber replacement interval for clean binary prevalence."""
    r = observed_prevalence
    return (max(0.0, (r - epsilon) / (1.0 - epsilon)),
            min(1.0, r / (1.0 - epsilon)))


def group_cap_diameter(epsilon: float, pi: float, bar_epsilon: float, g: float) -> float:
    """G-D: conditional group contamination eta <= bar_epsilon and pi*eta <= epsilon."""
    eta = min(bar_epsilon, epsilon / pi) if pi > 0 else bar_epsilon
    if eta >= 1.0 or g == 0:
        return 1.0
    return min(1.0, eta / ((1.0 - eta) * g))


def make_phase_table(out: Path) -> list[dict[str, object]]:
    epsilons = (0.01, 0.03, 0.05, 0.10)
    prevalences = (0.01, 0.02, 0.05, 0.10, 0.25, 0.50)
    followups = (0.10, 0.25, 0.50, 0.75, 1.0)
    rows = []
    for e in epsilons:
        for pi in prevalences:
            for g in followups:
                d = clipped_diameter(e, pi, g)
                rows.append({"epsilon": e, "pi": pi, "g": g, "diameter": d,
                             "critical_epsilon": critical_epsilon(pi, g),
                             "saturated": d >= 1.0 - 1e-12})
    with (out / "phase_diagram.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader(); writer.writerows(rows)
    return rows


def main() -> None:
    out = Path("results/step03")
    out.mkdir(parents=True, exist_ok=True)

    # Boundary and monotonicity checks for G-A.
    for e in (0.0, 0.01, 0.1, 0.4):
        for pi in (0.01, 0.2, 0.5, 1.0):
            for g in (0.0, 0.1, 0.5, 1.0):
                d = clipped_diameter(e, pi, g)
                assert 0.0 <= d <= 1.0
                if e == 0 and pi > 0 and g > 0:
                    assert d == 0.0
                if g == 0 or pi == 0:
                    assert d == 1.0
    for pi, g in ((0.01, 0.5), (0.1, 1.0), (0.5, 0.5)):
        assert clipped_diameter(0.02, pi, g) <= clipped_diameter(0.05, pi, g)
        assert clipped_diameter(0.05, pi, g) >= clipped_diameter(0.05, min(1.0, pi + 0.1), g)
        assert clipped_diameter(0.05, pi, g) >= clipped_diameter(0.05, pi, 1.0)

    # G-A majority/minority comparison.
    comparison = []
    for e, pi, g0, g1 in ((0.05, 0.1, 0.8, 0.5), (0.1, 0.2, 0.5, 0.5), (0.2, 0.05, 1.0, 0.25)):
        rare = clipped_diameter(e, pi, g1)
        majority = clipped_diameter(e, 1.0 - pi, g0)
        comparison.append({"epsilon": e, "pi_rare": pi, "g_majority": g0, "g_rare": g1,
                           "rare_diameter": rare, "majority_diameter": majority,
                           "rare_minus_majority": rare - majority})

    # G-B1 clean prevalence interval from observed prevalence under whole-row replacement.
    prevalence_examples = []
    for r, e in ((0.1, 0.05), (0.1, 0.2), (0.5, 0.1), (0.02, 0.1)):
        lo, hi = prevalence_interval(r, e)
        prevalence_examples.append({"observed_prevalence": r, "epsilon": e,
                                    "clean_prevalence_lower": lo, "clean_prevalence_upper": hi})

    # G-B1 complete nonidentification construction: if clean prevalence may be as
    # small as the overlap budget, subgroup outcomes can be switched while the
    # majority compensates. This records the threshold, not a universal fixed-R formula.
    complete_threshold_examples = []
    for e in (0.01, 0.05, 0.2):
        alpha = e / (1.0 - e)
        complete_threshold_examples.append({"epsilon": e, "overlap_budget": alpha,
                                            "some_positive_pi_can_be_hidden": e > 0,
                                            "sufficient_small_pi_threshold": min(1.0, alpha)})

    # G-C and G-D comparison.
    audit_comparison = []
    for e, pi, g, bar in ((0.1, 0.05, 0.5, 0.05), (0.1, 0.05, 0.5, 0.5), (0.2, 0.2, 0.25, 0.1)):
        audit_comparison.append({"epsilon": e, "pi": pi, "g": g, "bar_epsilon_g": bar,
                                 "G_A_global": clipped_diameter(e, pi, g),
                                 "G_C_marginal_preserving": clipped_diameter(e, 1.0, g),
                                 "G_D_per_group_cap": group_cap_diameter(e, pi, bar, g)})

    # Multi-group resource allocation: alpha is the pairwise Huber overlap
    # budget; changing only group j costs pi_j*g_j*d_j in observed TV.
    groups = [{"j": 1, "pi": 0.01, "g": 0.5}, {"j": 2, "pi": 0.09, "g": 0.8},
              {"j": 3, "pi": 0.30, "g": 0.6}, {"j": 4, "pi": 0.60, "g": 0.9}]
    multi_rows = []
    for e in (0.02, 0.1, 0.2):
        alpha = e / (1.0 - e)
        for row in groups:
            m = row["pi"] * row["g"]
            multi_rows.append({"epsilon": e, "group": row["j"], "pi": row["pi"], "g": row["g"],
                               "effective_information_mass": m,
                               "sharp_group_diameter": min(1.0, alpha / m)})

    # Tiny multi-bin subgroup LP check: block scaling by pi changes the
    # observed-TV cost, but the full operator remains the object to optimize.
    q = np.array([0.2, 0.3, 0.25, 0.25])
    events = np.array([1.0, 2.0, 3.0])
    a = censor_matrix(q, events)
    tail_functional = np.array([0.0, 0.0, 0.0, 1.0])
    multibin_lp = []
    for e in (0.02, 0.1, 0.2):
        for pi in (0.05, 0.2):
            # Pairwise width over conditional tail mass with joint block cost.
            # Construct a scaled block operator; the majority block is fixed
            # and contributes no difference, so the width is the LP result.
            scaled = pi * a
            width = pairwise_width(scaled, e, tail_functional)
            multibin_lp.append({"epsilon": e, "pi": pi, "lp_width": width})

    phase_rows = make_phase_table(out)
    result = {
        "evidence_level": "CHECKED: deterministic algebra and finite LP examples; not a novelty proof",
        "G_A": {"formula": "min(1, epsilon/((1-epsilon)*pi*g))",
                "critical_epsilon": "pi*g/(1+pi*g)", "boundary_checks": True},
        "majority_minority": comparison,
        "G_B1_prevalence_intervals": prevalence_examples,
        "G_B1_threshold_examples": complete_threshold_examples,
        "G_C_G_D": audit_comparison,
        "multi_group": multi_rows,
        "multi_bin_lp": multibin_lp,
        "phase_rows": len(phase_rows),
        "models": {
            "G_A": "trusted label, fixed clean prevalence, arbitrary global row contamination",
            "G_B1": "whole-row Huber replacement; clean prevalence not fixed",
            "G_B2": "label-only corruption; requires a specified flip channel; no universal formula claimed",
            "G_C": "contamination preserves subgroup marginal exactly",
            "G_D": "conditional group contamination eta_g <= bar_epsilon_g and pi_g*eta_g <= epsilon",
        },
    }
    (out / "rare_group_checks.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"phase_rows": len(phase_rows), "multi_group_rows": len(multi_rows),
                      "multibin_lp_rows": len(multibin_lp), "output": str(out / "rare_group_checks.json")}))


if __name__ == "__main__":
    main()
