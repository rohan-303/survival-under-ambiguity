"""Tiny dependency-free Cox PH and intentionally naive comparison learners."""
from __future__ import annotations

import math
from typing import Sequence

from .operators import SurvivalRecord


def _dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def fit_cox(records: Sequence[SurvivalRecord], max_iter: int = 40) -> tuple[float, ...]:
    """Breslow-ties Cox partial-likelihood Newton fit for a small pilot."""
    p = len(records[0].x) if records else 0
    beta = [0.0] * p
    event_times = sorted({r.y for r in records if r.delta == 1})
    for _ in range(max_iter):
        grad = [0.0] * p
        hess = [[0.0] * p for _ in range(p)]
        for t in event_times:
            events = [r for r in records if r.delta == 1 and r.y == t]
            risk = [r for r in records if r.y >= t]
            weights = [math.exp(max(-40.0, min(40.0, _dot(beta, r.x)))) for r in risk]
            denom = sum(weights)
            mean = [sum(w * r.x[j] for w, r in zip(weights, risk)) / denom for j in range(p)]
            for r in events:
                for j in range(p):
                    grad[j] += r.x[j] - mean[j]
            for j in range(p):
                for k in range(p):
                    second = sum(w * r.x[j] * r.x[k] for w, r in zip(weights, risk)) / denom
                    hess[j][k] -= len(events) * (second - mean[j] * mean[k])
        # Solve (-H) step = gradient; ridge stabilizes tiny deterministic fixtures.
        a = [[-hess[i][j] + (1e-8 if i == j else 0.0) for j in range(p)] + [grad[i]] for i in range(p)]
        for i in range(p):
            pivot = max(range(i, p), key=lambda k: abs(a[k][i]))
            if abs(a[pivot][i]) < 1e-12:
                return tuple(beta)
            a[i], a[pivot] = a[pivot], a[i]
            scale = a[i][i]
            a[i] = [v / scale for v in a[i]]
            for k in range(p):
                if k == i:
                    continue
                scale = a[k][i]
                a[k] = [x - scale * y for x, y in zip(a[k], a[i])]
        step = [a[i][-1] for i in range(p)]
        beta = [b + s for b, s in zip(beta, step)]
        if max(abs(s) for s in step) < 1e-8:
            break
    return tuple(beta)


def cox_survival(records: Sequence[SurvivalRecord], beta: Sequence[float],
                 horizons: Sequence[int]) -> dict[tuple[float, ...], dict[int, float]]:
    """Breslow baseline survival predictions, grouped by exact x vector."""
    event_times = sorted({r.y for r in records if r.delta == 1})
    cumulative = 0.0
    base = {}
    for t in event_times:
        d = sum(r.delta == 1 and r.y == t for r in records)
        denom = sum(math.exp(max(-40.0, min(40.0, _dot(beta, r.x)))) for r in records if r.y >= t)
        cumulative += d / denom if denom else 0.0
        base[t] = math.exp(-cumulative)
    groups = sorted({r.x for r in records})
    out = {}
    for x in groups:
        curve = {}
        for t in horizons:
            h = sum(v for u, v in base.items() if u <= t)
            curve[t] = math.exp(-h * math.exp(_dot(beta, x)))
        out[x] = curve
    return out


def naive_observed_event_risk(records: Sequence[SurvivalRecord], horizons: Sequence[int]):
    """Deliberately invalid learner: treats censoring as a non-event at horizon."""
    groups = sorted({r.x for r in records})
    out = {}
    for x in groups:
        subset = [r for r in records if r.x == x]
        out[x] = {t: sum(r.delta == 1 and r.y <= t for r in subset) / len(subset)
                  for t in horizons}
    return out
