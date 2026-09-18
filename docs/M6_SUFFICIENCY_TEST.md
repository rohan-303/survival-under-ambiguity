# M6 sufficiency test

## Strongest supported abstract

Under exchangeable corruption locations within trusted strata and arbitrary corrupted values, exact hypergeometric inversion yields confidence sets for finite stratum corruption counts. Combining those sets with a deterministic adversarial event-fraction interval and a known one-bin censoring channel gives confidence-certified survival intervals and an exact small-population allocation oracle under a global corruption cap.

## Remove “survival” and “censoring”

The abstract becomes exact finite-population audit certification with a downstream weighted binary functional. The proof and implementation remain essentially unchanged. The only survival-specific operation is division by `g_h` and truncation at one.

**Result:** survival specificity is weak.

## Remove audit allocation

What remains is hypergeometric defect-count certification plus an adversarial binary-functional interval and the scalar channel transform. The first component is standard; the latter is elementary composition.

**Result:** no sufficient contribution remains beyond standard certification.

## Gate implication

The transfer assumption is useful for honest finite-population certification, but this frozen direction does not supply a publishable survival-specific theorem. The pivot fails its kill test.
