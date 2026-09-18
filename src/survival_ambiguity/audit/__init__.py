"""Adversarial finite-population survival auditing utilities."""

from .models import (
    AuditOutcome, EventFractionInterval, RecordedTuple, audit_subsets,
    brute_force_event_interval, enumerate_clean_records, hamming_distance,
    post_audit_event_fraction, survival_interval_from_recorded,
)
from .hypergeom_bounds import (
    confidence_bounds_m, confidence_set_m, coverage, hypergeom_pmf,
    hypergeom_support,
)
from .survival_certificate import (
    CertifiedInterval, certified_stratum_interval, clean_audit_upper_m,
    clean_audit_survival_width, worst_clean_audit_recorded_width,
)
from .allocation import AggregateInterval, aggregate_recorded_interval, enumerate_allocations

__all__ = [
    "AuditOutcome", "EventFractionInterval", "RecordedTuple", "audit_subsets",
    "brute_force_event_interval", "enumerate_clean_records", "hamming_distance",
    "post_audit_event_fraction", "survival_interval_from_recorded",
    "confidence_bounds_m", "confidence_set_m", "coverage", "hypergeom_pmf",
    "hypergeom_support", "CertifiedInterval", "certified_stratum_interval",
    "clean_audit_upper_m", "clean_audit_survival_width",
    "worst_clean_audit_recorded_width", "AggregateInterval",
    "aggregate_recorded_interval", "enumerate_allocations",
]
