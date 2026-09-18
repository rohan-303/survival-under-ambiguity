"""Small deterministic Step 08 synthetic preflight.

This is a diagnostic pilot, not a performance benchmark or calibrated test.
"""
from __future__ import annotations

import itertools
import json
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from survival_ambiguity.censoring_interventions import (
    LatentRow, common_support, cox_survival, fit_cox, naive_observed_event_risk,
    observe, prediction_discrepancy, recensor, stratified_km,
)

OUT = ROOT / "results" / "step08"
OUT.mkdir(parents=True, exist_ok=True)


def build_rows(seed: int = 8, n: int = 240):
    rng = random.Random(seed)
    rows = []
    for i in range(n):
        risk = float(i % 2)
        shortcut = float((i // 2) % 2)
        # Discrete proportional-hazard-like event generation. The shortcut has
        # no role in T; it only changes the original censoring distribution.
        t = 7
        for time in range(1, 7):
            hazard = 0.10 * (2.0 if risk else 1.0)
            if rng.random() < hazard:
                t = time
                break
        c = rng.randint(3, 6) if shortcut == 0 else rng.randint(1, 4)
        rows.append(LatentRow((risk, shortcut), t, c))
    return tuple(rows)


def records(rows, cutoffs=None):
    base = tuple(observe(r) for r in rows)
    return base if cutoffs is None else tuple(recensor(r, c) for r, c in zip(base, cutoffs))


def counts(records_):
    return {"n": len(records_), "censored": sum(r.delta == 0 for r in records_),
            "events": sum(r.delta == 1 for r in records_)}


def cox_discrepancy(a, b):
    horizons = [1, 2, 3, 4, 5]
    pa = cox_survival(a, fit_cox(a), horizons)
    pb = cox_survival(b, fit_cox(b), horizons)
    common = {t: any(r.y >= t for r in a) and any(r.y >= t for r in b) for t in horizons}
    return prediction_discrepancy(pa, pb, common), common


def naive_discrepancy(a, b):
    horizons = [1, 2, 3, 4, 5]
    pa = naive_observed_event_risk(a, horizons)
    pb = naive_observed_event_risk(b, horizons)
    common = {t: True for t in horizons}
    return prediction_discrepancy(pa, pb, common)


def find_equal_rate_pair(rows):
    groups = sorted({(r.x[0], r.x[1]) for r in rows})
    candidates = []
    for vals in itertools.product((2, 4, 6), repeat=len(groups)):
        mapping = dict(zip(groups, vals))
        cut = tuple(mapping[(r.x[0], r.x[1])] for r in rows)
        rs = records(rows, cut)
        by_shortcut = {s: sum(r.delta == 0 for r in rs if r.x[1] == s) / sum(r.x[1] == s for r in rs)
                       for s in (0.0, 1.0)}
        candidates.append((counts(rs), by_shortcut, cut))
    best = None
    for a, b in itertools.combinations(candidates, 2):
        if a[0]["censored"] != b[0]["censored"] or a[0]["events"] != b[0]["events"]:
            continue
        geometry = abs((a[1][0.0] - a[1][1.0]) - (b[1][0.0] - b[1][1.0]))
        if best is None or geometry > best[0]:
            best = (geometry, a, b)
    return best


def true_risk(rows):
    out = defaultdict(list)
    for r in rows:
        out[r.x].append(r.t)
    return {str(k): {str(t): sum(v > t for v in vals) / len(vals) for t in range(1, 6)}
            for k, vals in out.items()}


def main():
    rows = build_rows()
    original = records(rows)
    uniform = records(rows, (4,) * len(rows))
    shortcut_intervention = records(rows, tuple(2 if r.x[1] == 0 else 6 for r in rows))
    pair = find_equal_rate_pair(rows)
    scenarios = {
        "A_valid_independent_censoring_cox": {
            "original": counts(original), "uniform_re_censor": counts(uniform),
            "cox_discrepancy": cox_discrepancy(original, uniform)[0],
            "naive_discrepancy": naive_discrepancy(original, uniform),
        },
        "B_valid_independent_censoring_misspecified_observed_event_learner": {
            "original": counts(original), "shortcut_geometry_intervention": counts(shortcut_intervention),
            "naive_discrepancy": naive_discrepancy(original, shortcut_intervention),
            "cox_discrepancy": cox_discrepancy(original, shortcut_intervention)[0],
        },
    }
    if pair is None:
        equal_rate = {"status": "NOT_FOUND"}
    else:
        _, a, b = pair
        ra, rb = records(rows, a[2]), records(rows, b[2])
        equal_rate = {
            "status": "FOUND", "counts_a": a[0], "counts_b": b[0],
            "shortcut_censoring_rates_a": a[1], "shortcut_censoring_rates_b": b[1],
            "cox_discrepancy": cox_discrepancy(ra, rb)[0],
            "naive_discrepancy": naive_discrepancy(ra, rb),
        }
    # Population common support is represented here by empirical positive at-risk
    # support only as a deterministic pilot diagnostic; no inferential threshold.
    horizons = [1, 2, 3, 4, 5]
    support = {t: any(r.y >= t for r in original) and any(r.y >= t for r in uniform) for t in horizons}
    payload = {
        "step": 8, "status": "PREFLIGHT_ONLY", "seed": 8,
        "true_risk_by_group": true_risk(rows),
        "scenarios": scenarios, "equal_rate_pair": equal_rate,
        "common_support_mask": support,
        "administrative_cutoff_like": {"status": "PILOTED_VIA_SHORTCUT_INTERVENTION", "caveat": "not a real calendar-date benchmark"},
        "non_calendar_shortcut": {"status": "PILOTED", "caveat": "naive learner is intentionally invalid; Cox is the null-control learner"},
        "formal_p_values": "NOT_COMPUTED",
        "interpretation": "paired discrepancies are descriptive and not calibrated tests",
    }
    (OUT / "censoring_intervention_checks.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
