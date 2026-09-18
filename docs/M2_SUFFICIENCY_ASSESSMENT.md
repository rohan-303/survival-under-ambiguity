# M2 Sufficiency Assessment

## Criterion

A theorem passes the sufficiency screen only if it would change how a survival analyst diagnoses, reports, or abstains on subgroup survival under contamination. The statement “small groups have less information” is not sufficient.

## Candidate assessment

### T1/T2: one-bin G-A diameter and frontier

**Conditional.** The exact frontier is easy to interpret and can certify that a subgroup target is population-unidentified under stated assumptions. However, the current form is an elementary rescaling by effective observable mass and may be scientifically too obvious without an operational audit or decision rule.

### T3: label contamination

**Open/conditional.** Label corruption could matter materially because the clean subgroup estimand may cease to be directly tied to the observed stratum. It becomes sufficient only if a sharp result exposes a threshold or trade-off not captured by generic misclassification sensitivity analysis.

### T4: global versus groupwise audit information

**Most promising.** A sharp comparison could tell analysts exactly when a global data-quality guarantee is inadequate for a subgroup and how much group-specific audit information restores recoverability. This has a direct reporting implication and survives removal of OT and synthetic generation.

### T5: multi-group allocation

**Conditional.** The effective-information-mass ordering is useful for triage, but the one-bin result is a fractional-budget calculation. It would need a nontrivial extension, such as joint subgroup decision stability or a multi-functional frontier, to be more than an intuition formalization.

### T6: multi-bin survival/RMST

**Conditional.** This is the strongest survival-specific route. It may become sufficient if the operator creates horizon-dependent trade-offs where no single scalar `pi_g G_{C,g}(t)` describes RMST or survival-function uncertainty. That has not yet been demonstrated.

## Provisional sufficiency verdict

**CONDITIONAL.**

The current theorem candidates contain a potentially useful audit-to-abstention message, but the one-bin result alone is not enough. A future sufficient result should include an exact identified-set comparison across contamination audits and at least one survival-functional consequence beyond a scalar rescaling.
