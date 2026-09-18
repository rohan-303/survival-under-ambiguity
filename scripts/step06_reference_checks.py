"""Step 06 exact finite-population adversarial-audit checks."""
from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from survival_ambiguity.audit import (  # noqa: E402
    AuditOutcome, RecordedTuple, audit_subsets, brute_force_event_interval,
    post_audit_event_fraction,
)


def records(bits):
    return tuple(RecordedTuple(0, 0, int(x)) for x in bits)


def worst_width(n: int, m: int, audited: tuple[int, ...]) -> float:
    maximum = 0.0
    for observed_bits in itertools.product((0, 1), repeat=n):
        observed = records(observed_bits)
        for clean_bits in itertools.product((0, 1), repeat=n):
            clean = records(clean_bits)
            if sum(a != b for a, b in zip(observed, clean)) > m:
                continue
            outcome = AuditOutcome(audited, tuple(clean[i] for i in audited))
            out = post_audit_event_fraction(observed, outcome, m)
            exact = brute_force_event_interval(observed, outcome, m)
            if abs(out.width - exact.width) > 1e-12:
                raise AssertionError((observed_bits, clean_bits, out, exact))
            maximum = max(maximum, out.width)
    return maximum


def main() -> None:
    rows = []
    for n, m in ((3, 1), (4, 1), (4, 2), (5, 2)):
        for b in range(n + 1):
            widths = [worst_width(n, m, subset) for subset in itertools.combinations(range(n), b)]
            rows.append({"n": n, "m": m, "B": b,
                         "worst_case_width": max(widths),
                         "best_fixed_subset_width": min(widths)})
    # Explicit adversarial witness: all observed and audited records are censored,
    # while one unaudited clean record may be an event when B<n and m>=1.
    witness = {"n": 4, "m": 1, "B": 2, "observed": [0, 0, 0, 0],
               "audit_set": [0, 1], "audit_clean": [0, 0],
               "compatible_clean_worlds_event_counts": [0, 1],
               "width": 0.25}
    out_dir = ROOT / "results" / "step06"
    out_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "status": "CHECKED_NOT_PROVED",
        "model": "finite population, binary recorded event/censor indicator, at most m arbitrary row corruptions",
        "rows": rows,
        "witness": witness,
        "conclusion": "For m>=1, every fixed audit policy with B<n has a positive worst-case post-audit width; full audit is required for a universal zero-width guarantee under unrestricted corruption.",
    }
    (out_dir / "audit_checks.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "output": str(out_dir / "audit_checks.json"),
                      "full_audit_widths": [r for r in rows if r["B"] == r["n"]]}, indent=2))


if __name__ == "__main__":
    main()
