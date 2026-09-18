"""Finite discrete-time observation and additional-censoring operators."""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Iterable, Mapping, Sequence


@dataclass(frozen=True)
class LatentRow:
    x: tuple[float, ...]
    t: int
    c: int


@dataclass(frozen=True)
class SurvivalRecord:
    x: tuple[float, ...]
    y: int
    delta: int


def observe(row: LatentRow) -> SurvivalRecord:
    if row.t < 0 or row.c < 0:
        raise ValueError("times must be nonnegative")
    return SurvivalRecord(row.x, min(row.t, row.c), int(row.t <= row.c))


def recensor(record: SurvivalRecord, c_prime: int) -> SurvivalRecord:
    """Apply extra administrative censoring without inventing event times."""
    if c_prime < 0:
        raise ValueError("c_prime must be nonnegative")
    if record.delta not in (0, 1):
        raise ValueError("delta must be binary")
    return SurvivalRecord(record.x, min(record.y, c_prime),
                          int(record.delta == 1 and record.y <= c_prime))


def recensor_many(records: Sequence[SurvivalRecord], c_primes: Sequence[int]) -> tuple[SurvivalRecord, ...]:
    if len(records) != len(c_primes):
        raise ValueError("record and intervention lengths differ")
    return tuple(recensor(r, c) for r, c in zip(records, c_primes))


def observe_composed(row: LatentRow, c_prime: int) -> SurvivalRecord:
    return observe(LatentRow(row.x, row.t, min(row.c, c_prime)))


def composition_identity(rows: Iterable[LatentRow], c_prime: int) -> bool:
    return all(recensor(observe(row), c_prime) == observe_composed(row, c_prime)
               for row in rows)


def no_intervention_identity(records: Sequence[SurvivalRecord], c_prime: int | None) -> bool:
    if c_prime is None:
        return True
    return all(recensor(r, c_prime) == r for r in records if r.y <= c_prime)


def common_support(original_followup: Mapping[int, float],
                   intervened_followup: Mapping[int, float],
                   horizons: Iterable[int], epsilon: float = 0.0) -> dict[int, bool]:
    """Population common-support mask; no empirical threshold is implied."""
    return {t: original_followup.get(t, 0.0) > epsilon and
               intervened_followup.get(t, 0.0) > epsilon for t in horizons}


def stratified_km(records: Sequence[SurvivalRecord], horizons: Sequence[int]) -> dict[tuple[float, ...], dict[int, float]]:
    """Small exact Kaplan–Meier estimator by covariate stratum."""
    groups = sorted({r.x for r in records})
    out = {}
    for g in groups:
        subset = [r for r in records if r.x == g]
        surv = 1.0
        curve = {}
        for t in sorted(horizons):
            at_risk = sum(r.y >= t for r in subset)
            events = sum(r.y == t and r.delta == 1 for r in subset)
            if at_risk:
                surv *= 1.0 - events / at_risk
            curve[t] = surv
        out[g] = curve
    return out


def prediction_discrepancy(pred_a: Mapping[tuple[float, ...], Mapping[int, float]],
                           pred_b: Mapping[tuple[float, ...], Mapping[int, float]],
                           common: Mapping[int, bool]) -> float:
    vals = [abs(pred_a[g][t] - pred_b[g][t])
            for g in pred_a for t, ok in common.items() if ok and t in pred_a[g] and t in pred_b[g]]
    return sum(vals) / len(vals) if vals else float("nan")
