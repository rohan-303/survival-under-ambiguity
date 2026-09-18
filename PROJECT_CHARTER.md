# Project Charter

## Motivation

Observed survival records contain baseline covariates `X`, latent event time `T`, censoring time `C`, observed time `Y = min(T,C)`, and event indicator `Delta = 1{T <= C}`. In addition to censoring, records may be contaminated. The project studies what latent survival conclusions remain defensible under this combined ambiguity.

A generic starting formulation is `P_obs = (1-epsilon) A_H(P_0) + epsilon Q`, where `P_0` is a latent clean law, `H` a censoring law, `A_H` an observation operator, and `Q` a contamination law. This is a starting model, not a frozen theorem or universal formulation.

## Central question

When right-censored survival observations may also be contaminated, which properties of the latent survival population remain identifiable, how sharply can they be bounded, how does recoverability degrade for rare subgroups, and how should trustworthy synthetic data represent unresolved ambiguity?

## Theory objective

Characterize sharp or near-sharp identified sets and minimax/recoverability moduli for selected survival functionals under explicit censoring, contamination, and structural assumptions.

## Rare-subgroup objective

Derive, refute, or replace candidate dependence on global contamination, subgroup prevalence, and subgroup-specific follow-up. No heuristic scaling is treated as a result.

## TV versus OT

Compare Huber/TV-native ambiguity with robust optimal-transport geometries. OT is retained only if it gives valid, materially informative results beyond TV analysis.

## Synthetic-world idea

If justified later, construct compatible latent survival scenarios at functional extrema or a central/minimax representative. They are scenarios under assumptions, not posterior draws or equally probable truths without a probability model.

## Explicit non-goals

- No neural-network experiments in Step 01.
- No claim of novelty, theorem, empirical result, or publication readiness.
- No data acquisition, model downloads, or broad implementation.
- No modification of existing `Survival_Model` or `Robust_optimal_Transport_updated` repositories.
- No GitHub remote configuration or push in Step 01.

## Success criteria

A clean, local, minimally executable repository; a precise research contract; explicit evidence labels and non-claims; a passing package smoke test; and a recorded local Git state.

## Failure and pivot criteria

Pivot or stop if the closest literature already contains the intended theorem, if OT adds no defensible value, if the rare-group effect disappears under correct modeling, if assumptions are scientifically indefensible, or if finite-sample procedures cannot be certified. A negative or narrowed result remains scientifically useful when clearly documented.
