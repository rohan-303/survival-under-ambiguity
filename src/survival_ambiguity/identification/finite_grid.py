"""Finite discrete survival observation operators."""
from __future__ import annotations

import numpy as np


def censoring_operator(censoring_probs: np.ndarray, event_times: np.ndarray) -> np.ndarray:
    """Build A_q; rows are event cells then censor cells, columns event+tail.

    Censor support is `0.5, 1.5, ...`; event is observed when T <= C.
    """
    q = np.asarray(censoring_probs, dtype=float)
    times = np.asarray(event_times, dtype=float)
    if q.ndim != 1 or times.ndim != 1 or len(q) == 0 or len(times) == 0:
        raise ValueError("one-dimensional nonempty inputs required")
    if np.any(q < 0) or not np.isclose(q.sum(), 1.0):
        raise ValueError("censoring probabilities must be nonnegative and sum to one")
    if np.any(np.diff(times) <= 0):
        raise ValueError("event times must be strictly increasing")
    censor_times = np.arange(len(q), dtype=float) + 0.5
    k = len(times)
    a = np.zeros((k + len(q), k + 1), dtype=float)
    for l, c in enumerate(censor_times):
        for j, t in enumerate(times):
            if t <= c:
                a[j, j] += q[l]
            else:
                a[k + l, j] += q[l]
        a[k + l, k] += q[l]
    if not np.allclose(a.sum(axis=0), 1.0):
        raise AssertionError("observation operator is not stochastic")
    return a


def grouped_recorded_operator(operators: list[np.ndarray], prevalences: np.ndarray) -> np.ndarray:
    """Return the clean joint operator mapping conditional masses to records."""
    pi = np.asarray(prevalences, dtype=float)
    if len(operators) != len(pi) or not np.isclose(pi.sum(), 1.0):
        raise ValueError("operator/prevalence mismatch")
    rows = []
    for a, p in zip(operators, pi):
        rows.append(p * a)
    return np.block([[rows[i] if i == j else np.zeros_like(rows[i])
                      for j in range(len(rows))] for i in range(len(rows))])


def label_mixed_operator(operators: list[np.ndarray], prevalences: np.ndarray,
                         label_matrix: np.ndarray) -> np.ndarray:
    """Map conditional latent masses to observed-label/record cells.

    Output is grouped by observed label. `label_matrix[a,b]` is P(G_obs=b|G_clean=a).
    """
    pi = np.asarray(prevalences, dtype=float)
    m = np.asarray(label_matrix, dtype=float)
    groups = len(operators)
    if m.shape != (groups, groups) or not np.allclose(m.sum(1), 1.0):
        raise ValueError("label matrix must be row-stochastic")
    obs = operators[0].shape[0]
    cols = groups * operators[0].shape[1]
    out = np.zeros((groups * obs, cols))
    for clean_g, a in enumerate(operators):
        for obs_g in range(groups):
            out[obs_g * obs:(obs_g + 1) * obs,
                clean_g * a.shape[1]:(clean_g + 1) * a.shape[1]] = pi[clean_g] * m[clean_g, obs_g] * a
    return out
