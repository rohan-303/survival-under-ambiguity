"""Small exact allocation utilities for stratified audit certificates."""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Sequence

from .hypergeom_bounds import confidence_set_m
from .models import AuditOutcome, RecordedTuple


@dataclass(frozen=True)
class AggregateInterval:
    lower_count: int
    upper_count: int
    total_n: int
    caps: tuple[int, ...]

    @property
    def lower(self) -> float:
        return self.lower_count / self.total_n

    @property
    def upper(self) -> float:
        return self.upper_count / self.total_n

    @property
    def width(self) -> float:
        return self.upper - self.lower


def _allocate_uncertainty(ones: list[int], zeros: list[int], caps: list[int], budget: int,
                          minimize: bool) -> int:
    """Optimize clean event count over integer remaining-corruption allocations."""
    budget = min(budget, sum(caps))
    best = None
    for allocation in product(*(range(c + 1) for c in caps)):
        if sum(allocation) > budget:
            continue
        total = 0
        for o, z, k in zip(ones, zeros, allocation):
            total += o - min(o, k) if minimize else o + min(z, k)
        best = total if best is None else (min(best, total) if minimize else max(best, total))
    if best is None:
        raise ValueError("no feasible corruption allocation")
    return best


def aggregate_recorded_interval(observed_by_stratum: Sequence[Sequence[RecordedTuple]],
                                outcomes: Sequence[AuditOutcome],
                                alpha_h: Sequence[float],
                                global_cap: int | None = None) -> AggregateInterval:
    """Combine stratum confidence upper bounds, optionally under sum M_h<=m."""
    if len(observed_by_stratum) != len(outcomes) or len(outcomes) != len(alpha_h):
        raise ValueError("stratum inputs differ in length")
    ones, zeros, caps, audited_events = [], [], [], 0
    total_n = 0
    for observed, outcome, alpha in zip(observed_by_stratum, outcomes, alpha_h):
        n = len(observed); b = len(outcome.audited_indices)
        outcome.validate(n)
        d = sum(observed[i] != clean for i, clean in zip(outcome.audited_indices, outcome.clean_records))
        m_set = confidence_set_m(n, b, d, alpha)
        cap = m_set[-1] - d
        audited = set(outcome.audited_indices)
        unverified = [observed[i] for i in range(n) if i not in audited]
        ones.append(sum(x.delta == 1 for x in unverified))
        zeros.append(len(unverified) - ones[-1])
        caps.append(max(0, cap))
        audited_events += sum(x.delta == 1 for x in outcome.clean_records)
        total_n += n
    remaining_global = sum(caps) if global_cap is None else max(0, global_cap - sum(
        sum(observed[i] != clean for i, clean in zip(outcome.audited_indices, outcome.clean_records))
        for observed, outcome in zip(observed_by_stratum, outcomes)))
    lower = audited_events + _allocate_uncertainty(ones, zeros, caps, remaining_global, True)
    upper = audited_events + _allocate_uncertainty(ones, zeros, caps, remaining_global, False)
    return AggregateInterval(lower, upper, total_n, tuple(caps))


def enumerate_allocations(total_budget: int, strata: int) -> list[tuple[int, ...]]:
    out = []
    def rec(prefix, remaining, k):
        if k == strata - 1:
            out.append(tuple(prefix + [remaining]))
            return
        for x in range(remaining + 1):
            rec(prefix + [x], remaining - x, k + 1)
    rec([], total_budget, 0)
    return out
