# Q4 Label-Selection Kill Test

## Corbin, Baiocchi & Chen

Corbin et al. study clinical model evaluation when only a subset of outcomes is observed. They describe three classes of label selection, simulate causally distinct mechanisms, show that naïve discrimination/calibration estimates can fail, and use weighting estimators when selection probabilities are properly specified. Their framing includes deployment monitoring and directly rejects the idea that observed labels automatically represent the full deployment population.

Q4's M1 weighting result is therefore composition, not novelty. Randomly acquiring a validation/adjudication subset is also adjacent to their injected-randomization design.

## Selective labels versus delayed labels

A delayed label is eventually observed; a selective label is observed only for a policy-selected subset and may never arrive. These are different data-generating regimes, but combining them does not create novelty. Q4 must specify whether `D<infinity` is guaranteed and whether `R` depends on `Y` after conditioning on `X,G,A`.

## Random adjudication

If unresolved cases are randomly adjudicated with positive probability within each subgroup, the unresolved outcome distribution becomes identifiable under a valid reference standard and positivity. This is a design remedy, not a new estimator. If adjudication quality or transport differs by subgroup, the target changes or requires sensitivity analysis.

## Verdict

**Label-Selection Gate L: `FAIL`.** M1, M3, inverse weighting, selection probabilities, and randomized acquisition are ordinary label-selection/missing-data machinery. Q4 adds subgroup conditioning but no nontrivial theorem beyond stratified application.
