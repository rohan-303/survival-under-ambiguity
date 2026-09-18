"""Confidence-certified recorded and one-bin survival intervals."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .hypergeom_bounds import confidence_bounds_m, confidence_set_m
from .models import AuditOutcome, EventFractionInterval, RecordedTuple, post_audit_event_fraction


@dataclass(frozen=True)
class CertifiedInterval:
    recorded: EventFractionInterval
    m_set: tuple[int, ...]
    confidence_level: float
    survival_lower: float | None
    survival_upper: float | None

    @property
    def recorded_width(self) -> float:
        return self.recorded.width

    @property
    def survival_width(self) -> float | None:
        if self.survival_lower is None or self.survival_upper is None:
            return None
        return self.survival_upper - self.survival_lower


def certified_stratum_interval(observed: Sequence[RecordedTuple], outcome: AuditOutcome,
                               n_h: int, b_h: int, alpha_h: float,
                               followup: float | None = None) -> CertifiedInterval:
    """Invert D's exact hypergeometric law, then apply deterministic corruption bounds."""
    if n_h != len(observed) or b_h != len(outcome.audited_indices):
        raise ValueError("stratum size/audit size mismatch")
    d = sum(observed[i] != clean for i, clean in zip(outcome.audited_indices, outcome.clean_records))
    m_set = confidence_set_m(n_h, b_h, d, alpha_h)
    upper_m = m_set[-1]
    recorded = post_audit_event_fraction(observed, outcome, upper_m)
    if followup is None:
        low = high = None
    elif followup == 0:
        low = high = None
    elif 0 < followup <= 1:
        low = max(0.0, recorded.lower / followup)
        high = min(1.0, recorded.upper / followup)
    else:
        raise ValueError("followup must be in [0,1]")
    return CertifiedInterval(recorded, m_set, 1 - alpha_h, low, high)


def clean_audit_upper_m(n: int, b: int, alpha: float) -> int:
    """Upper endpoint of C_M after observing D=0."""
    return confidence_bounds_m(n, b, 0, alpha)[1]


def worst_clean_audit_recorded_width(n: int, b: int, alpha: float) -> float:
    """Worst event-fraction width over observed binary compositions when D=0."""
    u = clean_audit_upper_m(n, b, alpha)
    return min(n, 2 * u) / n


def clean_audit_survival_width(n: int, b: int, alpha: float, followup: float) -> float:
    if followup <= 0:
        raise ValueError("zero follow-up gives no channel identification")
    return min(1.0, worst_clean_audit_recorded_width(n, b, alpha) / followup)
