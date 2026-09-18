# M5 verification-design prior art

| Citation | Domain | Survival? | Right censoring? | Error type | Adversarial? | Gold validation? | Audit reveals | Fixed/adaptive? | Objective | Point estimate? | Partial ID? | Worst-case? | Rare group? | Main theorem/result | Exact overlap | Remaining distinction |
|---|---|---:|---:|---|---:|---:|---|---|---|---:|---:|---:|---:|---|---|---|
| Horowitz & Manski (1995), *Identification and Robustness with Contaminated and Corrupted Data* [1] | Econometrics/partial ID | No | No | Contamination/corruption | Yes | No | Clean/contaminated relationship is bounded abstractly | N/A | Identification/robustness | Yes | Yes | Yes | No | General identification under contaminated/corrupted data | Baseline for V-F impossibility | Survival observation operator and audit oracle remain distinct if a theorem survives |
| Magaret/Xie et al. (2008), *Incorporating Validation Subsets into Discrete Proportional Hazards Models for Mismeasured Outcomes* [2] | Survival measurement error | Yes | Discrete time-to-event and censoring | Mismeasured failure outcome | No; sensitivity/specificity framework | Yes | True failure status through observed failure/censoring on validation subset | Validation subset; model-based | Reduce bias/efficiency of PH estimation | Yes | No adversarial identified set | No | No | Validation data can reduce bias when mismeasurement rates unknown | Closest survival validation precedent | It assumes a statistical outcome-mismeasurement model and targets hazard estimation, not arbitrary row corruption/minimax width |
| Giganti et al. (2018), *A validation sampling approach for consistent estimation of adverse drug reaction risk with misclassified right-censored survival data* [3] | Pharmacovigilance | Yes | Yes | Misclassified ADR/outcome | No | Yes | Gold-standard validation of the misclassified survival outcome | Sampling design | Consistent estimation | Yes | No | No arbitrary-corruption guarantee | Not primary | Directly blocks broad claims that validation plus censored survival is new | Exact finite-population adversarial audit and sharp width objective remain different |
| Han et al. (2021), *Two-Phase Sampling Designs for Data Validation in Settings with Covariate Measurement Error and Continuous Outcome* [4] | Validation sampling | No survival target | No | Covariate measurement error | No | Yes | True covariate in phase 2 | Fixed/design-based strata | Model/design-based estimator efficiency | Yes | No | No | No | Optimal/nearly optimal validation designs | Threat to allocation language | Different survival target and no adversarial minimax interval |
| Optimal multiwave validation of secondary-use data with outcome/exposure misclassification (2021/2024) [5] | EHR validation | Not primarily survival | Not the Step 06 survival operator | Outcome/exposure misclassification | No | Yes | Gold-standard database variables | Adaptive multiwave | Minimize MLE variance; estimate design parameters in waves | Yes | No | No | Potential strata | Adaptive grid search and efficiency gains | Strongest audit-allocation threat | Objective is variance/likelihood efficiency, not worst-case identified width |
| Steinhardt, Charikar & Valiant (2017), *Learning from Untrusted Data* [6] | Robust/semi-verified learning | No | No | Arbitrary untrusted fraction | Yes | Trusted sample/oracle | Trusted labels/data for queried examples | Query/trusted-data model | Accurate learning/estimation | Yes | Not survival partial ID | Robust guarantees | No | Semi-verified learning can leverage trusted data with untrusted data | Threat to generic “trusted plus untrusted” framing | Survival censoring and finite-population clean-record interval are not its target |
| Two-phase survival validation literature and related internal validation sources | Biostatistics | Yes | Often yes | Measurement error | Usually no | Yes | Validated outcome/status under a statistical error model | Often stratified/adaptive | Variance, bias, consistency | Yes | Rarely | Rarely | Sometimes | Established validation design/inference | Threat to V-P | V-F arbitrary row corruption and minimax width need a distinct theorem |

## Strongest novelty threats

1. **Direct survival validation:** Magaret/Xie 2008 and Giganti et al. 2018 show that validating mismeasured right-censored outcomes is established practice with formal estimation theory.
2. **Optimal audit allocation:** the Han/two-phase and multiwave EHR literature already optimizes validation strata, often adaptively.
3. **Generic trusted/untrusted robustness:** semi-verified learning already studies a small trusted set plus a large untrusted set.
4. **Generic partial identification:** Horowitz–Manski blocks broad claims that arbitrary corruption plus identified intervals is new.

The only candidate distinction left is narrow: a finite-population, recorded-tuple audit oracle with arbitrary row corruption and an exact minimax width/impossibility theorem that explicitly preserves censoring loss. Whether that is publishable or merely a direct specialization remains `OPEN`.

## Sources

[1] Horowitz & Manski (1995) bibliographic record: https://www.diw.de/sixcms/media.php/17/gc_syllabus_ss2017_MC_partial_identification.pdf

[2] https://pmc.ncbi.nlm.nih.gov/articles/PMC2574985/

[3] https://pubmed.ncbi.nlm.nih.gov/30084171/

[4] https://pmc.ncbi.nlm.nih.gov/articles/PMC8715909/

[5] https://pmc.ncbi.nlm.nih.gov/articles/PMC11610482/ and https://arxiv.org/html/2108.13263v3

[6] https://arxiv.org/abs/1611.02315

No full copyrighted papers were downloaded or staged. Claims about each source are limited to verified abstracts/full-text passages or explicitly marked as unresolved.
