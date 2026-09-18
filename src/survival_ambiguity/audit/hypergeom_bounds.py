"""Exact hypergeometric certification for exchangeable corruption locations."""
from __future__ import annotations

from math import comb


def hypergeom_pmf(n: int, m: int, b: int, d: int) -> float:
    if min(n, m, b) < 0 or m > n or b > n:
        raise ValueError("invalid finite-population parameters")
    if d < max(0, b - (n - m)) or d > min(b, m):
        return 0.0
    return comb(m, d) * comb(n - m, b - d) / comb(n, b)


def hypergeom_support(n: int, m: int, b: int) -> range:
    return range(max(0, b - (n - m)), min(b, m) + 1)


def confidence_set_m(n: int, b: int, d: int, alpha: float) -> tuple[int, ...]:
    """Conservative equal-tail inversion over the finite M=0,...,N space.

    M is retained when both one-sided tail probabilities are greater than or
    equal to alpha/2. This is exact finite-population coverage, not an
    asymptotic approximation and not a prior on M.
    """
    if not 0 <= alpha < 1 or not 0 <= b <= n or not 0 <= d <= b:
        raise ValueError("invalid confidence-set inputs")
    if b == 0:
        return tuple(range(n + 1))
    retained = []
    for m in range(n + 1):
        lower_tail = sum(hypergeom_pmf(n, m, b, x) for x in range(d, b + 1))
        upper_tail = sum(hypergeom_pmf(n, m, b, x) for x in range(0, d + 1))
        if lower_tail + 1e-15 >= alpha / 2 and upper_tail + 1e-15 >= alpha / 2:
            retained.append(m)
    return tuple(retained)


def confidence_bounds_m(n: int, b: int, d: int, alpha: float) -> tuple[int, int]:
    values = confidence_set_m(n, b, d, alpha)
    if not values:
        raise ValueError("empty exact confidence set")
    return values[0], values[-1]


def coverage(n: int, m: int, b: int, alpha: float) -> float:
    return sum(hypergeom_pmf(n, m, b, d)
               for d in hypergeom_support(n, m, b)
               if m in confidence_set_m(n, b, d, alpha))
