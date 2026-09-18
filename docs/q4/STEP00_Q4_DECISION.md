# Step 00 Q4 Decision

## Status

`Q4_CLOSED_WITH_FAIL`

## Gates

| Gate | Result | Reason |
|---|---|---|
| Delayed-Feedback Gate D | `CONDITIONAL` | Delayed ACI covers fixed/ultimately observed delay, but not all outcome-selective feedback. The residual problem is generic partial feedback. |
| Label-Selection Gate L | `FAIL` | Corbin et al. and missing-data/selection theory cover naïve bias, weighting, and randomized label acquisition. |
| Subgroup Gate G | `CONDITIONAL` | Subgroups matter for precision and safety, but separate subgroup monitoring is not a new theory. |
| Identifiability Gate I | `CONDITIONAL` | M0–M3 boundaries are standard; T3 remains open but not established as a distinct result. |
| Data Gate | `CONDITIONAL` | Retrospective MIMIC/eICU can support a declared protocol benchmark, not actual deployed label maturation. |
| Novelty Gate N-Q4 | `FAIL` | No precise contribution beyond delayed conformal, label-selection, missing-data, or partial-feedback theory was established. |
| Sufficiency Gate S-Q4 | `CONDITIONAL` | The monitoring advice is actionable, but the elementary false-safe example is already known in substance. |

## Master decision

**`Q4-G — FAIL FOR MULTIPLE REASONS`**

Do not create a new project. Do not automatically start Q9 or Q10.

## Strongest identifiable result

Under `R independent of Y | X,G,A`, subgroup selective risk is identified by standard inverse-probability-of-maturation weighting under positivity and correct propensity specification.

## Strongest impossibility result

Under outcome-dependent or permanent label maturation, two data-generating processes can have identical observed `(X,G,A,R,RY)` distributions but different subgroup selective risks. This is generic MNAR nonidentification, not a new theorem.

## Delayed ACI answer

Delayed ACI does not subsume M2/M3 because its core setup has delayed but ultimately observed feedback and focuses on adaptive coverage under temporal dependence. It subsumes M0 and much of M1. The remaining selective-feedback problem is not shown to exceed generic missing-feedback/online-learning theory.

## Corbin/selective-label answer

Corbin et al. substantially subsume Q4's label-selection core, including bias from observed-label subsets, weighting, and injected randomization. Q4's subgroup condition adds operational stratification but no nontrivial theorem.

## Random-adjudication status

Positive-probability randomized adjudication within each subgroup restores identification under standard consistency, positivity, and valid-reference assumptions. This is a known design remedy and is adjacent to Corbin et al.; no minimum-rate theorem beyond standard sampling was established.

## Strongest delayed-conformal result

Outcome/score/action-dependent feedback can make adaptive conformal updates see a selected error stream, so delay-only guarantees cannot be transferred automatically. This is a credible open question, but not a verified Q4 contribution.

## Strongest clinical use case

Monitoring early subgroup safety for a deployed model with delayed readmission or pathology labels. Available public datasets only support a reconstructed protocol, not real deployment evidence.

## Exact surviving contribution

None established.

## Recommendation

`NO_AUTOMATIC_NEXT_CANDIDATE`
