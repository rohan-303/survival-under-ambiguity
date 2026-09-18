import itertools

from survival_ambiguity.audit import (
    AuditOutcome, RecordedTuple, aggregate_recorded_interval,
    certified_stratum_interval, clean_audit_survival_width, confidence_bounds_m,
    confidence_set_m, coverage, enumerate_allocations, hypergeom_pmf,
)


def rec(delta, group=0, y=0):
    return RecordedTuple(group, y, delta)


def test_hypergeom_normalizes_and_handles_limits():
    for n in range(1, 9):
        for m in range(n + 1):
            for b in range(n + 1):
                assert abs(sum(hypergeom_pmf(n, m, b, d) for d in range(b + 1)) - 1) < 1e-12
                if b == 0:
                    assert confidence_set_m(n, b, 0, 0.05) == tuple(range(n + 1))
                if b == n:
                    assert confidence_set_m(n, b, m, 0.05) == (m,)


def test_exact_confidence_coverage_exhaustive_small_populations():
    alpha = 0.10
    for n in range(1, 10):
        for b in range(n + 1):
            for m in range(n + 1):
                assert coverage(n, m, b, alpha) >= 1 - alpha - 1e-12


def test_endpoint_discoveries_have_valid_bounds():
    lo, hi = confidence_bounds_m(12, 5, 0, 0.05)
    assert lo == 0 and hi <= 12
    lo, hi = confidence_bounds_m(12, 5, 5, 0.05)
    assert lo >= 5 and hi == 12


def test_end_to_end_exchangeable_audit_coverage_with_arbitrary_values():
    n, m, b, alpha = 6, 2, 3, 0.10
    clean = tuple(rec(x) for x in (1, 1, 0, 0, 1, 0))
    # Corrupted values are fixed adversarial flips; only locations are random.
    covered = 0.0
    total = 0.0
    for locations in itertools.combinations(range(n), m):
        observed = list(clean)
        for i in locations:
            observed[i] = rec(1 - observed[i].delta)
        for audited in itertools.combinations(range(n), b):
            outcome = AuditOutcome(audited, tuple(clean[i] for i in audited))
            cert = certified_stratum_interval(tuple(observed), outcome, n, b, alpha)
            p = 1 / (comb_count(n, m) * comb_count(n, b))
            total += p
            truth = sum(r.delta for r in clean) / n
            covered += p * (cert.recorded.lower - 1e-12 <= truth <= cert.recorded.upper + 1e-12)
    assert abs(total - 1) < 1e-12
    assert covered >= 1 - alpha - 1e-12


def comb_count(n, k):
    from math import comb
    return comb(n, k)


def test_survival_channel_boundaries_and_heavy_censoring():
    assert clean_audit_survival_width(20, 20, 0.05, 1.0) == 0
    assert clean_audit_survival_width(20, 0, 0.05, 0.2) == 1
    try:
        clean_audit_survival_width(20, 4, 0.05, 0)
    except ValueError:
        pass
    else:
        raise AssertionError("g=0 must not be treated as identified")


def test_global_cap_can_tighten_aggregate_certificate():
    observed = ((rec(1), rec(0), rec(0)), (rec(1), rec(0), rec(0)))
    outcomes = (AuditOutcome((), ()), AuditOutcome((), ()))
    independent = aggregate_recorded_interval(observed, outcomes, (0.05, 0.05))
    coupled = aggregate_recorded_interval(observed, outcomes, (0.05, 0.05), global_cap=1)
    assert coupled.width <= independent.width


def test_allocations_are_exact_integer_compositions():
    assert enumerate_allocations(3, 2) == [(0, 3), (1, 2), (2, 1), (3, 0)]
