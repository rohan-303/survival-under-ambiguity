"""Audit-regime contracts for finite grouped survival identification."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Sequence

import numpy as np


class AuditRegime(str, Enum):
    A0_GLOBAL_ONLY = "A0_GLOBAL_ONLY"
    A1_TRUSTED_MARGINAL = "A1_TRUSTED_MARGINAL"
    A2_MARGINAL_PRESERVING = "A2_MARGINAL_PRESERVING"
    A3_GROUP_CAPS = "A3_GROUP_CAPS"
    A4_KNOWN_LABEL_CHANNEL = "A4_KNOWN_LABEL_CHANNEL"


@dataclass(frozen=True)
class AuditSpec:
    """Population audit assumptions for a finite grouped model.

    `prevalences` are clean group masses when known. `group_caps` are
    conditional contamination caps, not total-population masses.
    """

    regime: AuditRegime
    epsilon: float
    prevalences: tuple[float, ...] | None = None
    group_caps: tuple[float, ...] | None = None
    label_matrix: tuple[tuple[float, ...], ...] | None = None

    def validate(self, groups: int) -> None:
        if not 0 <= self.epsilon < 1:
            raise ValueError("epsilon must lie in [0, 1)")
        if self.prevalences is not None:
            if len(self.prevalences) != groups or any(p <= 0 for p in self.prevalences):
                raise ValueError("prevalences must be positive and group-sized")
            if not np.isclose(sum(self.prevalences), 1.0):
                raise ValueError("prevalences must sum to one")
        if self.regime in (AuditRegime.A1_TRUSTED_MARGINAL,
                           AuditRegime.A2_MARGINAL_PRESERVING,
                           AuditRegime.A3_GROUP_CAPS,
                           AuditRegime.A4_KNOWN_LABEL_CHANNEL) and self.prevalences is None:
            raise ValueError(f"{self.regime} requires clean prevalences")
        if self.regime == AuditRegime.A3_GROUP_CAPS:
            if self.group_caps is None or len(self.group_caps) != groups:
                raise ValueError("A3 requires one conditional cap per group")
            if any(not 0 <= x < 1 for x in self.group_caps):
                raise ValueError("group caps must lie in [0, 1)")
        if self.regime == AuditRegime.A4_KNOWN_LABEL_CHANNEL:
            m = np.asarray(self.label_matrix, dtype=float)
            if m.shape != (groups, groups) or np.any(m < 0) or not np.allclose(m.sum(1), 1):
                raise ValueError("label_matrix must be row-stochastic and group-sized")


def group_block_masses(recorded: np.ndarray, groups: int, observations: int) -> np.ndarray:
    """Return observed group masses from group-major recorded blocks."""
    r = np.asarray(recorded, dtype=float).reshape(groups, observations)
    return r.sum(axis=1)


def effective_group_caps(spec: AuditSpec) -> tuple[float, ...]:
    """Return the conditional caps implied by G-D (caller supplies prevalences)."""
    if spec.regime != AuditRegime.A3_GROUP_CAPS or spec.group_caps is None:
        raise ValueError("effective_group_caps is only defined for A3")
    return spec.group_caps
