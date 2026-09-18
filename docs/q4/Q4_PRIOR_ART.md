# Q4 Prior-Art Matrix

| Citation | Delayed labels | Variable delay | Outcome-dependent delay | Permanent missing labels | Policy-dependent labels | Selective predictions | Subgroup target | Conformal | Risk monitoring | Randomization | IPC weighting | Finite-sample guarantee | Deployment setting | Exact overlap | Remaining distinction |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| El Halabi & Brandt, arXiv:2609.07251 | Yes | Forecast horizon | No in core setup | No | No | Forecast intervals | No clinical subgroup target | ACI | Coverage feedback | No | No | Yes, delay-dependent | Online forecasting | Occupies fixed/ultimately observed delayed ACI | Does not directly cover outcome-selective/permanent clinical label feedback |
| Barber et al., DOI 10.1214/22-AOS2243 | Not specific | General shift | Not specific | Not specific | Not specific | Yes | Conditional validity limits | Yes | No deployment monitor | No | Weighted methods discussed | General conformal theory | No | Establishes limits beyond exchangeability | Clinical maturation structure remains unaddressed |
| Gibbs & Candes, arXiv:2106.00170 | No delay focus | No | No | No | No | Online prediction | No | ACI | Online coverage | No | No | Distribution-shift guarantees | No | Occupies adaptive conformal baseline | Does not identify selected labels |
| Corbin, Baiocchi & Chen, PMID 37350883 | Sometimes deployment labels | Selection classes | Can be mechanism-dependent | Yes/selective subset | Yes | Model evaluation | Subgroups possible but not Q4 core | No | Clinical performance estimates | Injected randomization | Yes when selection probabilities specified | Simulation/evaluation guarantees | Yes | Directly occupies selected-label bias, weighting, randomized validation | Q4 would need a non-generic interaction with maturation and subgroup selective risk |
| Selective-label / bandit feedback literature | Often | Often | Sometimes | Yes | Yes | Policy-selected actions | Sometimes | Sometimes | Partial feedback | Exploration | Inverse propensity | Online guarantees vary | Policy learning | Generic selective feedback is established | Clinical target could add structure only with a new result |
| Clinical selective/conformal prediction (bounded search) | Labels assumed available for evaluation | Not core | Not core | Not core | Sometimes shift weights | Yes | Yes/Mondrian or weighted | Yes | Risk-coverage/deferral | Not usually | Sometimes | Conditional/approximate | Clinical studies | Occupies subgroup selective-risk target | Does not automatically solve maturation at monitor time |
| MAR/MNAR missing-data theory | Delayed observation can be represented | Yes | Yes | Yes | Yes | Not required | Stratification standard | No | Estimation | Validation/random sampling | Standard | Standard asymptotic/finite-sample tools | Not deployment-specific | Occupies M0–M3 identification boundary | Q4 terminology does not create novelty |

## Top threats

1. El Halabi & Brandt 2026 delayed ACI.
2. Corbin, Baiocchi & Chen label-selection evaluation.
3. General conformal prediction beyond exchangeability and subgroup/weighted validity.
4. Selective-label and partial-feedback online learning.
5. MAR/MNAR and randomized validation theory.

## Provisional conclusion

Q4 is not killed by delayed ACI alone: the preprint's core feedback is delayed but ultimately observed and not outcome-selectively missing. It is killed as a project candidate because the remaining distinction is the composition of standard selective-label/MNAR identification, randomized validation, subgroup stratification, and partial-feedback conformal theory. No standalone Q4 theorem was established.

## Sources

See the report's numbered source list.
