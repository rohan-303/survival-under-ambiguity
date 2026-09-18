import itertools

from survival_ambiguity.audit import (
    AuditOutcome, RecordedTuple, brute_force_event_interval,
    post_audit_event_fraction, survival_interval_from_recorded,
)


def rec(delta, group=0, y=0):
    return RecordedTuple(group, y, delta)


def test_audit_reveals_recorded_tuple_only():
    observed = (rec(0, y=1),)
    outcome = AuditOutcome((0,), (rec(0, y=1),))
    interval = post_audit_event_fraction(observed, outcome, 1)
    assert interval.width == 0
    # The object has no latent T field; censoring remains represented by delta=0.
    assert outcome.clean_records[0].delta == 0


def test_closed_form_matches_bruteforce_after_corruption_discovery():
    observed = (rec(1), rec(0), rec(1), rec(0))
    outcome = AuditOutcome((0,), (rec(0),))
    closed = post_audit_event_fraction(observed, outcome, 2)
    exact = brute_force_event_interval(observed, outcome, 2)
    assert closed.lower == exact.lower and closed.upper == exact.upper
    assert closed.audited_corruptions == 1
    assert closed.remaining_corruption == 1


def test_verified_clean_record_and_zero_budget():
    observed = (rec(1), rec(0), rec(1))
    outcome = AuditOutcome((1,), (rec(0),))
    out = post_audit_event_fraction(observed, outcome, 1)
    assert out.audited_corruptions == 0
    assert out.width > 0
    exact = post_audit_event_fraction(observed, AuditOutcome((), ()), 0)
    assert exact.width == 0


def test_full_audit_identifies_clean_recorded_event_fraction():
    observed = (rec(1), rec(0), rec(1))
    clean = (rec(0), rec(0), rec(1))
    outcome = AuditOutcome((0, 1, 2), clean)
    out = post_audit_event_fraction(observed, outcome, 2)
    assert out.lower == out.upper == 1 / 3


def test_censoring_scales_declared_recorded_channel_interval():
    observed = (rec(1), rec(0), rec(1), rec(0))
    out = post_audit_event_fraction(observed, AuditOutcome((), ()), 1)
    low, high = survival_interval_from_recorded(out, followup=0.5)
    assert high - low == 2 * out.width


def test_rare_group_example_is_explicitly_computable():
    observed = (rec(1, group=1), rec(0, group=1), rec(0, group=0), rec(0, group=0))
    outcome = AuditOutcome((0,), (rec(0, group=1),))
    out = post_audit_event_fraction(observed, outcome, 1)
    assert out.audited_corruptions == 1
    assert out.width >= 0
