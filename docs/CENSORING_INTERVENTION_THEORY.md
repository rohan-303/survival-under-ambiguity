# Censoring-intervention theory

## 1. Observation operator

Let `P` be the distribution of `(X,T)`, with `Y=min(T,C)` and `Delta=1{T<=C}`. For a censoring mechanism `G`, `A_G(P)` is the observed-data law of `(X,Y,Delta)`. The clean null is `T independent of C conditional on X`.

## 2. Additional-censoring operator

For an observed record `(X,Y,Delta)` and analyst-chosen `C'`, define

`Y'=min(Y,C')`, `Delta'=1{Delta=1 and Y<=C'}`.

This operation only removes follow-up. It never reconstructs a censored subject's latent `T`.

## 3. Composition identity — ELEMENTARY

For a latent row `(X,T,C)`, applying the original observation map and then the additional-censoring map gives the same recorded tuple as observing once with censoring time `min(C,C')`:

`R(A_G(T,C),C') = A_{min(C,C')}(T,C)`.

The finite discrete-time implementation exhaustively verifies this identity. The continuous-time analogue is the same pointwise minimum identity, subject to the chosen tie convention.

## 4. Learning functional

A population learner `L` maps an observed-data law to a predictor, for example `S_L(t|x)`. Cox, KM, neural survival models, and pseudo-observation regressors need not target the same functional under misspecification. Therefore invariance cannot be assumed merely because they use the same input notation.

## 5. Common identifiable region

Compare predictions only on horizons where both observation processes have positive follow-up support. The pilot uses a transparent positive at-risk mask; a real study would require a population support condition such as `P(C>=t|X=x)>0` and `P(min(C,C')>=t|X=x)>0`. Differences outside this region are not evidence of shortcut dependence.

## 6. Population intervention invariance — ELEMENTARY

If `L` is Fisher-consistent for the same conditional event law `P(T|X)` under every valid independent-censoring mechanism in the intervention class, then

`L(A_G(P)) = L(A_{G'} A_G(P))`

on the common region. This follows because the target is unchanged and the intervention changes only observation, not `(X,T)`. The result is a necessary consequence of the consistency assumption, not a new identification theorem.

## 7. Necessary-condition theorem — CONDITIONAL

Under valid intervention, common support, stable target definition, and Fisher consistency, nonzero population prediction discrepancy falsifies at least one assumption in that bundle: target consistency, intervention validity, censoring assumptions, positivity, or the claim that the learner targets the same functional. It does not identify which assumption failed.

## 8. Non-sufficiency counterexample — REFUTED

Invariance does not imply correctness. A learner that always outputs the same incorrect survival curve is invariant under every intervention. Likewise, two misspecified learners can share a censoring-invariant pseudo-target. Therefore the diagnostic is one-sided: instability can falsify a bundle; stability cannot validate event-model correctness.

## 9. Prediction-instability functional

The primary descriptive functional is

`D_CI = E_X[ mean_{t in T_common} |S_G(t|X)-S_{G,G'}(t|X)| ]`.

The Step 08 pilot uses paired empirical averages and no p-value. Metric instability and parameter/estimand instability are reported separately, not folded into `D_CI`.

## 10. Prediction vs metric vs parameter instability

Prediction instability changes the learned curve for the same covariate. Metric instability changes Brier/C-index evaluation because censoring weights or evaluable subjects change. Parameter instability changes a model coefficient or pseudo-target estimand. Existing work directly addresses important parts of the latter two categories.[3][4]

## 11. Equal-rate interventions

A matched search found two interventions with the same pilot-level observed event and censor counts but different censoring rates by the shortcut stratum. Their Cox prediction discrepancy was `0.022574`; the intentionally invalid observed-event learner discrepancy was `0.045833`. These are descriptive finite-sample values, not calibrated evidence of a causal mechanism.

## 12. Information-loss controls

Same-subject pairing, equal observed event/censor counts, common-support masking, and a Cox null-control learner were implemented. They reduce obvious information-loss confounding but do not prove that residual discrepancy is mechanism-specific. Generic subsampling and effective-information matching were not developed into a formal control.

## 13. Shortcut DGP

The pilot includes a feature that affects censoring but not latent event time. The intentionally invalid learner, which treats censoring as a non-event, changes more under re-censoring than the Cox control. This is a sanity check, not a benchmark claim.

## 14. Mixed genuine-risk/censoring-signal DGP

The pilot includes a risk feature and a separate censoring-related feature. The current result does not reliably distinguish a pure shortcut from a legitimate risk feature that also predicts censoring. This remains a limitation.

## 15. Limitations

The pilot is small, deterministic, and descriptive. It does not establish finite-sample calibration, universal learner behavior, or a causal interpretation of instability. The Cox implementation is a reference fixture, not production survival software. Re-censoring cannot test late horizons outside common support.

## 16. Claim-status table

| Claim | Status |
|---|---|
| Re-censoring composition identity | ELEMENTARY |
| Fisher-consistency implies population invariance | ELEMENTARY |
| Instability falsifies an assumption bundle | CONDITIONAL |
| Stability proves correctness | REFUTED |
| Paired prediction discrepancy is computable without latent `T` | KNOWN / IMPLEMENTED |
| Equal-rate matched interventions isolate mechanism in finite samples | OPEN |
| Cox/naive shortcut pilot detects a signal | IMPLEMENTED sanity check, not a theorem |
| General censoring-intervention diagnostic novelty | REFUTED / occupied-threat unresolved |

## Prior-art boundary

Censoring distribution shift and administrative-cutoff leakage already cover adjacent failure modes.[1][2]

Dependent-censoring evaluation, administrative Brier scoring, and survival domain generalization cover additional nearby robustness and evaluation problems.[3][4][6]

Most importantly, SurvFM explicitly reports paired censoring interventions holding the latent prediction problem fixed, uses coupled mechanisms at multiple censoring levels, and includes matched covariate-dependent-censoring diagnostics.[5] That is a direct novelty threat to the proposed benchmark framing.

## Sources

[1] https://www.nber.org/papers/w35643
[2] https://arxiv.org/abs/2607.10466
[3] https://arxiv.org/abs/2502.19460
[4] https://jmlr.org/papers/v24/19-1030.html
[5] https://arxiv.org/html/2607.09577v2
[6] https://proceedings.mlr.press/v174/pfisterer22a.html
