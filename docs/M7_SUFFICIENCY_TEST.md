# M7 sufficiency test

## Test 1 — elementary theory versus empirical value

C1 is mathematically correct but elementary. C2/C3 could still be useful as a benchmark only if they exposed failures missed by standard metrics and were distinct from existing paired-censoring work. The direct SurvFM overlap prevents that conclusion here.

## Test 2 — developer action

A model developer could use common-support, equal-information, and paired prediction checks. However, no calibrated threshold or decision rule was established, and the strongest existing threat already performs paired intervention experiments.

## Test 3 — ordinary metrics

The toy pilot demonstrates that a deliberately invalid observed-event learner can move under re-censoring while Cox moves less. It does not establish that C2/C3 reveal failures hidden by C-index, IBS, or calibration in a valid fitted survival learner.

## Test 4 — information-loss confounding

Same-subject pairing, event/censor-count matching, and common-support masking were implemented. They reduce obvious confounding, but the residual discrepancy remains finite-sample and learner-dependent. A full effective-information-matched control was not established.

## Test 5 — need for fully observed T

The operator and prediction discrepancy require no latent `T` for censored records. The synthetic pilot uses latent `T` only for validation and interpretation, not for the diagnostic input. This is a practical strength but not a novelty result.

## Conclusion

The diagnostic idea is coherent and potentially useful, but this step does not establish a distinct or practically sufficient contribution. The project should not continue this core without an independently specified novelty target.
