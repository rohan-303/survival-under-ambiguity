# Candidate 3 — Deployment Use Case

## Plausible consequence

A clinical prediction developer might restrict or audit measurement-count, missingness, and workflow features; compare P0–P4 feature tiers; require local validation after monitoring-policy changes; or abstain when observation support is outside training range.

## Why this is not yet a contribution

These are sensible extensions of clinical-presence and transportability practice. The 2026 cross-database study already supports the actionable warning that richer observation summaries can improve internal discrimination while worsening external transportability and calibration. A generic observation-drift score would not establish whether clinical risk changed or whether calibration will fail.

## Strongest use case

Sepsis mortality prediction across ICU databases is the strongest concrete use case because it has a direct published observation-process comparison. It is unavailable as a novel empirical contribution: the central experiment has already been done.

## Fairness, leakage, and care

Observation processes can reflect access, clinician behavior, and resource availability. Some features are downstream of clinical suspicion and may be leakage; others are legitimate early signals. Candidate 3 cannot treat observation information as intrinsically invalid. It must distinguish stable predictive content from mutable workflow, which ordinary feature ablation cannot causally do.
