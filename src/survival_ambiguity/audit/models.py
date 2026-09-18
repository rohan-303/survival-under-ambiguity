"""Finite-population adversarial audit contracts."""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from typing import Iterable, Sequence


@dataclass(frozen=True)
class RecordedTuple:
    """The auditable recorded tuple; never contains a post-censoring T."""

    group: int
    y_bin: int
    delta: int


@dataclass(frozen=True)
class AuditOutcome:
    audited_indices: tuple[int, ...]
    clean_records: tuple[RecordedTuple, ...]

    def validate(self, n: int) -> None:
        if len(self.audited_indices) != len(self.clean_records):
            raise ValueError("audit indices and records differ in length")
        if len(set(self.audited_indices)) != len(self.audited_indices):
            raise ValueError("audit indices must be unique")
        if any(i < 0 or i >= n for i in self.audited_indices):
            raise ValueError("audit index out of range")


@dataclass(frozen=True)
class EventFractionInterval:
    lower: float
    upper: float
    remaining_corruption: int
    audited_corruptions: int

    @property
    def width(self) -> float:
        return self.upper - self.lower


def hamming_distance(a: Sequence[RecordedTuple], b: Sequence[RecordedTuple]) -> int:
    if len(a) != len(b):
        raise ValueError("records must have equal length")
    return sum(x != y for x, y in zip(a, b))


def post_audit_event_fraction(observed: Sequence[RecordedTuple], outcome: AuditOutcome,
                              corruption_budget: int) -> EventFractionInterval:
    """Exact interval for clean event-record fraction under binary event coding.

    `event` means the recorded tuple has delta=1. Audits reveal the correct
    recorded tuple only. Censored records remain censored; no latent T is used.
    """
    n = len(observed)
    outcome.validate(n)
    if corruption_budget < 0:
        raise ValueError("corruption budget must be nonnegative")
    audited = set(outcome.audited_indices)
    audited_corruptions = sum(observed[i] != clean for i, clean in zip(outcome.audited_indices, outcome.clean_records))
    if audited_corruptions > corruption_budget:
        raise ValueError("audit outcome exceeds corruption budget")
    remaining = corruption_budget - audited_corruptions
    clean_audited_events = sum(clean.delta == 1 for clean in outcome.clean_records)
    unverified = [observed[i] for i in range(n) if i not in audited]
    ones = sum(z.delta == 1 for z in unverified)
    zeros = len(unverified) - ones
    lower_count = clean_audited_events + ones - min(ones, remaining)
    upper_count = clean_audited_events + ones + min(zeros, remaining)
    return EventFractionInterval(lower_count / n, upper_count / n, remaining, audited_corruptions)


def survival_interval_from_recorded(interval: EventFractionInterval, followup: float) -> tuple[float, float]:
    """Translate a recorded-event fraction to a one-bin event probability.

    This is a declared known-channel sensitivity calculation, not an assertion
    that a finite sample exactly identifies a population probability.
    """
    if not 0 < followup <= 1:
        raise ValueError("followup must lie in (0,1]")
    return interval.lower / followup, interval.upper / followup


def enumerate_clean_records(observed: Sequence[RecordedTuple], audited: AuditOutcome,
                            corruption_budget: int) -> list[tuple[RecordedTuple, ...]]:
    """Truth-oracle enumeration for a tiny binary recorded alphabet."""
    audited.validate(len(observed))
    alphabet = tuple(RecordedTuple(0, y, d) for y in (0, 1) for d in (0, 1))
    # Include all group values used by observed/audited records.
    groups = sorted({r.group for r in observed} | {r.group for r in audited.clean_records})
    alphabet = tuple(RecordedTuple(g, y, d) for g in groups for y in (0, 1) for d in (0, 1))
    out = []
    audited_map = dict(zip(audited.audited_indices, audited.clean_records))
    for candidate in product(alphabet, repeat=len(observed)):
        if any(candidate[i] != truth for i, truth in audited_map.items()):
            continue
        if hamming_distance(observed, candidate) <= corruption_budget:
            out.append(candidate)
    return out


def brute_force_event_interval(observed: Sequence[RecordedTuple], outcome: AuditOutcome,
                               corruption_budget: int) -> EventFractionInterval:
    worlds = enumerate_clean_records(observed, outcome, corruption_budget)
    if not worlds:
        raise ValueError("no compatible clean world")
    values = [sum(r.delta == 1 for r in w) / len(w) for w in worlds]
    audited_corruptions = sum(observed[i] != c for i, c in zip(outcome.audited_indices, outcome.clean_records))
    return EventFractionInterval(min(values), max(values), corruption_budget - audited_corruptions,
                                 audited_corruptions)


def audit_subsets(n: int, budget: int) -> Iterable[tuple[int, ...]]:
    if not 0 <= budget <= n:
        raise ValueError("invalid audit budget")
    for b in range(budget + 1):
        yield from combinations(range(n), b)
