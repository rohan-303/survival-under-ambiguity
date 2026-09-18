"""Linear survival and RMST functionals on a finite event grid."""
from __future__ import annotations

import numpy as np


def survival_weights(event_times: np.ndarray, horizon: float) -> np.ndarray:
    """Weights for P(T > horizon), with terminal tail after the event grid."""
    times = np.asarray(event_times, dtype=float)
    return np.r_[times > horizon, True].astype(float)


def rmst_weights(event_times: np.ndarray, tau: float) -> np.ndarray:
    """Weights for E[min(T,tau)] under event masses plus terminal tail."""
    if tau <= 0:
        raise ValueError("tau must be positive")
    times = np.asarray(event_times, dtype=float)
    return np.minimum(np.r_[times, np.inf], tau)


def validate_survival_vector(values: np.ndarray, tolerance: float = 1e-9) -> None:
    values = np.asarray(values, dtype=float)
    if np.any(values[1:] - values[:-1] > tolerance):
        raise ValueError("survival vector is not nonincreasing")
