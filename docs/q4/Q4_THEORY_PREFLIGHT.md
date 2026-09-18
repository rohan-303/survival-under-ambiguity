# Q4 Theory Preflight

## Status

This is a pre-project kill gate. The central conclusion is that the elementary delay and missing-label results are known. The only potentially non-generic direction is selective outcome-dependent feedback interacting with adaptive subgroup monitoring; it was not established as novel.

## 1. Deployment cohort and frozen action

Fix a cohort of prediction instances issued in `[u-W,u]` before looking at label maturity. Let `X` be prediction-time features, `G` a prespecified subgroup, `A=1` mean the deployed system accepts/acts on the prediction, `Y` the eventual outcome, and `D` the time until the label becomes observable. At monitor time `u`, `R(u)=1{D <= u-s}`.

The primary target is selective risk `R_g = E[l(f(X),Y) | G=g,A=1]`. Secondary target: coverage `C_g=P(Y in Gamma(X)|G=g,A=1)`. The action meaning is not switched: `A=1` is accepted/acted-on.

## 2. Maturation regimes

- **M0 fixed delay:** `D=d` for all instances. This is stale feedback, not a fundamental identification problem if all labels eventually arrive.
- **M1 conditionally noninformative maturation:** `R independent of Y | X,G,A`. Standard inverse-probability-of-maturation weighting identifies risk if the propensity is known/consistently estimated and positive.
- **M2 outcome-dependent maturation:** `R not independent of Y | X,G,A`. The observed tuple `(X,G,A,R,RY)` does not identify risk without additional restrictions.
- **M3 permanent/selective missingness:** `P(D=infinity)>0`. Point identification fails without validation, audit, or random acquisition assumptions.

## 3. Naive monitor and elementary false-safe example

The naive monitor averages losses only over `R=1`. If group 0 has 8 correct and 2 errors, while errors mature with probability 0.1 and correct labels with probability 0.9, its observed error rate is `2/(72+2)=0.027`. If group 1 has the same true 0.2 error rate and equal 0.9 maturation for both classes, its observed error rate is 0.2. Group 0 falsely appears safer despite equal true selective risk. Reversing maturation rates reverses the apparent ranking. This is an elementary selection-bias example, not a theorem contribution.

## 4. M1 result

Under `R independent of Y | X,G,A`, risk is identified by standard inverse-probability weighting with `1/P(R=1|X,G,A)`, assuming positivity and correct conditioning. Estimating the maturation propensity creates ordinary missing-at-random estimation error. Unequal subgroup maturity reduces effective sample size and widens uncertainty; it does not create novelty by itself. **Classification: KNOWN/COMPOSITION.**

## 5. M2 result

Two populations can share the same observed masses `P(R=1,Y=1)=0.1`, `P(R=1,Y=0)=0.4`, and `P(R=0,RY=0)=0.5`, while the unresolved half contains no errors in one population and all errors in another. True risks are 0.1 and 0.6, but observed data are identical. **Classification: KNOWN generic MNAR NONIDENTIFICATION.**

## 6. M3 result

Permanent missingness creates the same or stronger nonidentification. Bounds require assumptions on missing-outcome prevalence, sensitivity parameters, or a validation/random-adjudication sample. **Classification: KNOWN.**

## 7. Random adjudication and holdout

Randomly adjudicating unresolved labels with positive probability within each subgroup restores identification under consistency and a valid adjudication reference standard, provided positivity and transport from adjudicated to unresolved cases hold. A subgroup holdout or shadow-mode arm can provide labels under a reference policy, but this is ordinary randomized exploration/withholding and is directly adjacent to Corbin et al.'s injected-randomization design. Positive probability is an asymptotic identification condition, not a finite-sample precision guarantee.

## 8. Delayed adaptive conformal interaction

If delay is fixed or independent of the outcome conditional on available history, delayed adaptive conformal methods address feedback lag. If whether feedback ever arrives depends on score, action, subgroup, or outcome, the update sequence is selectively observed. Standard delayed-ACI bounds do not by themselves identify subgroup selective risk or guarantee coverage under outcome-dependent missing feedback. However, stating this gap is not sufficient: it is a missing-feedback/online-learning problem unless a sharper clinical result is derived.

## 9. Theorem candidates

| Candidate | Status | Reason |
|---|---|---|
| T1 identification boundary M0–M3 | KNOWN/COMPOSITION | Fixed delay, MAR weighting, and MNAR nonidentification are standard. |
| T2 minimal randomized label acquisition | KNOWN/COMPOSITION | Positive-probability randomized validation is adjacent to injected randomization and survey/causal sampling. |
| T3 subgroup selective-feedback ACI | OPEN, not shown novel | Could yield an impossibility/repair result under score- or outcome-dependent feedback; generic partial-feedback conformal theory is a major threat. |
| T4 simultaneous subgroup safety monitor | KNOWN/COMPOSITION | Stratified concentration, multiplicity, and effective sample-size analysis are standard. |

## 10. Claim classification

- Fixed-delay stale monitoring: `KNOWN`.
- MAR inverse weighting: `KNOWN`.
- MNAR nonidentification: `KNOWN`.
- False-safe subgroup signal: `ELEMENTARY`.
- Random adjudication restores identification: `KNOWN/COMPOSITION`.
- Selectively observed delayed conformal feedback: `POTENTIALLY_NOVEL / OPEN`, but unresolved against generic online partial-feedback theory.

## Sources

See the Q4 report. Primary threats include El Halabi & Brandt arXiv:2609.07251 and Corbin, Baiocchi & Chen, PubMed PMID 37350883.
