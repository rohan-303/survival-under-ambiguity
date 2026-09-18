# Candidate 3 — Observation-Process Model

## Scope

This is a pre-project model, not an implementation. Three objects are kept separate:

- `L(t)`: latent physiology and disease severity;
- `V(t)`: encounter/presence process, describing when the patient is seen;
- `M_j(t)`: within-encounter measurement process for variable `j`.

The observed record is `O = A_{pi_obs}(L)`, where `pi_obs` governs encounter timing, variables measured, and recording. The outcome is `Y_{t+tau}` or event time `T`.

## Feature partition

`X_phys` contains observed content summaries: values, trends, and clinically meaningful temporal features. `X_obs` contains visit counts, time since visit, measurement counts, missingness masks, order patterns, inter-observation gaps, and documentation intensity. Last-value, variability, and min/max features can encode `X_obs` indirectly and cannot be classified by column name alone.

The hierarchy is:

- P0: physiology/content only;
- P1: content plus missingness mask;
- P2: content plus measurement counts;
- P3: content plus timing/intensity;
- P4: workflow, orders, and action history.

This partition is analytical, not causal identification. A recorded measurement can be both content and a consequence of clinical concern.

## Process distinctions

Informative presence is the fact that being observed by a health system is informative. Informative observation is the longitudinal analogue: when, how often, and what is measured are informative. The visit process and conditional measurement process must not be collapsed. A site can preserve visit frequency while changing laboratory ordering, or preserve test counts while changing timing.

## Policy intervention notation

A passive policy intervention changes only `A_pi` while holding the latent trajectory and treatment mechanism fixed. A monitoring intervention may change clinician action and therefore `L` and `Y`; it is not a nuisance intervention. Ordinary EHR data do not identify the passive counterfactual without consistency, policy exchangeability, positivity, and measurement-mechanism assumptions.

## Sources

Sisk et al., DOI `10.1093/jamia/ocaa242`, defines informative presence/observation and reviews derived predictors, modeling under informative presence, and latent structures. Jeanselme et al., arXiv `2205.13481`, explicitly separates longitudinal, inter-observation, and missingness processes.
