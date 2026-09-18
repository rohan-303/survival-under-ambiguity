# STEP 08 — CENSORING-INTERVENTION FRESH-CORE REPORT

## 1. Final status

**COMPLETE_WITH_WARNINGS — coherent idea, but the primary formulation is occupied by close prior work and does not clear the novelty/sufficiency gates.**

## 2. Starting HEAD

`ecff179b2cfbcefb8e7bab75e62c72f8cb28b03f`, branch `main`, clean and synchronized after `git pull --ff-only`.

## 3. Closed prior branches

Steps 01–07 are recorded in `docs/CLOSED_RESEARCH_LINES.md`. None was revived.

## 4. Fresh research question

Can valid analyst-controlled additional censoring be used as a paired falsification stress test for survival predictors, rather than merely as a sensitivity analysis?

## 5. Observation/intervention model

`Y=min(T,C)` and `Delta=1{T<=C}`. Additional censoring uses `Y'=min(Y,C')` and `Delta'=1{Delta=1 and Y<=C'}`. It only removes follow-up and never reveals a censored subject's latent `T`.

## 6. Composition identity

Finite discrete exhaustive checks verified that observing with `C` and then re-censoring at `C'` equals observing once with `min(C,C')`. This is `ELEMENTARY_DERIVATION`, not a novelty claim.

## 7. Learning functional

The implementation includes stratified Kaplan–Meier, a small Breslow-ties Cox PH fitter, and an intentionally invalid observed-event learner. Different learners can target different functionals under misspecification; predictions must therefore be compared at the learner level.

## 8. Common support

The pilot masks horizons with no positive at-risk support in either view. For uniform re-censoring at four time units, horizons 1–4 remained supported and horizon 5 did not. Unsupported horizons are not interpreted as instability evidence.

## 9. Population invariance

A learner Fisher-consistent for the same `P(T|X)` under every valid independent-censoring mechanism is invariant on common support. This is a direct consistency implication and is classified `ELEMENTARY`.

## 10. Falsification implication

A population instability can falsify the joint bundle of consistency, valid intervention, independent censoring, positivity, stable target, and common-support assumptions. It cannot identify which component failed and cannot establish causality by itself.

## 11. Non-sufficiency counterexample

A learner that always returns the same incorrect survival curve is perfectly invariant. Therefore stability does not imply correctness; the proposed principle is one-sided.

## 12. Stability functional

The primary descriptive functional is the average absolute prediction difference over covariates and common horizons:

`D_CI = E_X mean_t |S_G(t|X)-S_{G,G'}(t|X)|`.

No p-value or calibrated threshold was introduced.

## 13. Prediction/metric/parameter distinction

Prediction instability changes fitted curves. Metric instability changes Brier/C-index evaluation because censoring and evaluability change. Parameter/estimand instability changes coefficients or target definitions. Existing literature already covers important parts of metric and estimand instability.[3][4]

## 14. Intervention family

The pilot implemented deterministic additional administrative cutoffs and covariate-dependent cutoffs. Stochastic random administrative truncation, calendar-time simulation, and deliberately dependent censoring were not developed beyond the finite fixture.

## 15. Information-loss controls

Same-subject pairing, common-support masking, an event/censor-count-matched pair, and a Cox null-control learner were used. Generic effective-sample-size matching was not formally solved.

## 16. Equal-rate paired interventions

An exact finite-fixture search found two interventions with identical observed event count `75` and censor count `165`, but different censoring rates by shortcut stratum. The Cox prediction discrepancy was `0.022574`; the intentionally invalid observed-event learner discrepancy was `0.045833`. These are descriptive pilot outputs, not calibrated evidence.

## 17. Correct-model experiment

Under a discrete proportional-hazard-like event generator with censoring dependent on a covariate but independent of `T` conditional on `X`, Cox prediction discrepancy between original and uniform re-censored data was `0.002720`. This is a sanity check, not a population theorem.

## 18. Misspecified-model experiment

The observed-event learner deliberately treats censoring as a non-event. Its discrepancy under the same uniform intervention was `0.006667`; under a stronger shortcut-geometry intervention it was `0.052500`. The result confirms that an invalid learner can react to re-censoring, but does not validate a diagnostic threshold.

## 19. Shortcut-feature experiment

A binary shortcut feature affects censoring but not the latent event generator. The pilot included it in the Cox covariates and in the invalid learner. The invalid learner showed the stronger response; the Cox response remained a finite-sample reference signal.

## 20. Mixed-feature experiment

The pilot included a genuine risk feature and a separate censoring-related feature. It did not establish a reliable distinction between pure shortcut, legitimate risk-plus-censoring association, and model misspecification.

## 21. Administrative-cutoff experiment

A real calendar-date reconstruction was **NOT COMPUTED**. The fixture's cutoff intervention is only administrative-cutoff-like. Xu et al. already provide the stronger calendar-specific failure-mode analysis.[2]

## 22. Non-calendar shortcut experiment

A non-calendar shortcut was piloted through covariate-dependent re-censoring. The observed-event learner responded, but the result is not novel or sufficient because the learner is intentionally invalid and the matched benchmark is already threatened by SurvFM.[5]

## 23. Common-support test

The implementation correctly excludes late unsupported horizons. The test passed; the project does not interpret missing late follow-up as prediction instability.

## 24. Current literature comparison

Censoring-distribution shift and administrative-cutoff leakage already cover adjacent robustness problems.[1][2]

Dependent-censoring evaluation, administrative Brier scoring, and survival domain generalization cover nearby evaluation and shift problems.[3][4][6]

Conformalized survival prediction was reviewed as an adjacent prediction-validity direction, but its primary page was not extractable in this environment and it is not used as a load-bearing novelty claim.

## 25. Krishnamoorthy 2026 comparison

Their work treats limited overlap and censoring-distribution shift as a survival prediction problem and proposes CWITE. It is a direct threat to generic censoring-shift framing, although not the same as a learner-agnostic falsification null.[1]

## 26. Xu et al. 2026 comparison

Their work formalizes administrative-cutoff leakage, distinguishes it from informative censoring and temporal risk changes, and proposes practical detection/design principles. It directly threatens the calendar-shortcut branch.[2]

## 27. Lillelund et al. 2026 comparison

Their work introduces a semi-synthetic dependent-censoring framework preserving covariate structure and known event times, focused on evaluation-metric correction rather than prediction instability. It threatens any claim that semi-synthetic censoring stress tests are themselves new.[3]

## 28. Strongest surviving distinction

The only residual distinction is a prediction-level invariance functional with common-support masking and matched information controls, explicitly used as a one-sided falsification signal. Step 08 did not establish that this distinction is not subsumed by SurvFM's paired and matched intervention design.[5]

## 29. Fresh Core Gate F

**FAIL.** The proposed core is substantially occupied by censoring-shift, administrative-leakage, and especially paired-censoring benchmark work.

## 30. Falsification-Theory Gate I

**CONDITIONAL.** The necessary-condition logic is correct, but elementary; its converse is false.

## 31. Benchmark/Method Gate B

**CONDITIONAL.** Equal-count paired interventions produced a descriptive signal, but information-loss separation is incomplete and the closest benchmark overlap is substantial.

## 32. Novelty Gate N

**FAIL.** No specific contribution survived the direct SurvFM overlap and administrative-leakage threat.[2][5]

## 33. Sufficiency Gate S

**FAIL.** No calibrated or clearly distinct diagnostic rule was established that a model developer would need beyond existing censoring-shift and leakage checks.

## 34. Selected C1–C6 path

**PATH C5 — IDEA IS INTERESTING BUT ALREADY OCCUPIED.**

## 35. Files changed

- `docs/CLOSED_RESEARCH_LINES.md`
- `docs/CENSORING_INTERVENTION_PRIOR_ART.md`
- `docs/CENSORING_INTERVENTION_THEORY.md`
- `docs/M7_THEOREM_AND_BENCHMARK_CANDIDATES.md`
- `docs/M7_SUFFICIENCY_TEST.md`
- `docs/M7_DIRECTION_DECISION.md`
- `src/survival_ambiguity/censoring_interventions/operators.py`
- `src/survival_ambiguity/censoring_interventions/learners.py`
- `src/survival_ambiguity/censoring_interventions/__init__.py`
- `tests/test_step08_censoring_interventions.py`
- `scripts/step08_reference_checks.py`
- `results/step08/censoring_intervention_checks.json`
- this report

## 36. Tests

`python -m pytest -q` passed: **34 tests**. Tests cover no-created-event behavior, event preservation, composition, no-intervention identity, common support, deterministic KM, Cox finiteness, and shortcut sanity behavior.

## 37. Simulation results

The deterministic pilot used seed `8` and `240` synthetic rows. Original data contained `91` events and `149` censored records. Uniform re-censoring contained `82` events and `158` censored records. Equal-count paired interventions each contained `75` events and `165` censored records, with different shortcut-stratum censoring geometry.

## 38. Deviations

No deep survival models, formal p-values, real datasets, full calendar-date reconstruction, stochastic intervention family, or two-stage adaptive diagnostic were run. These were intentionally excluded because the core already faced a direct prior-art overlap and the step was a kill test.

## 39. Limitations

The Cox and KM implementations are small reference fixtures, not production estimators. The pilot is finite-sample and descriptive. The equal-rate pair matches observed event/censor counts, not every information functional. The literature review establishes a strong threat boundary, not universal proof that no refinement could ever be novel.

## 40. Recommended Step 09 only

Do not begin Step 09 from this formulation. If the broader project continues, freeze a genuinely independent research question and perform a new primary-source search before implementation. Do not revive Steps 01–07 or turn this descriptive stress test into a novelty claim.

## Sources

[1] https://www.nber.org/papers/w35643
[2] https://arxiv.org/abs/2607.10466
[3] https://arxiv.org/abs/2502.19460
[4] https://jmlr.org/papers/v24/19-1030.html
[5] https://arxiv.org/html/2607.09577v2
[6] https://proceedings.mlr.press/v174/pfisterer22a.html
