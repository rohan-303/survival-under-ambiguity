# Theorem-Level Literature Landscape

Search date: 2026-09-18. This is a targeted kill-test, not a claim of exhaustive coverage. Primary-source pages/PDFs were retrieved where accessible; OpenReview access for the GAS-DRO paper was bot-gated, so the official ICLR abstract was used.

| Citation | Year / status | Problem and target | Observation/censoring | Ambiguity / geometry | Key result and sharpness | Rare group / generation | Exact overlap and remaining difference | Read depth | Primary source |
|---|---|---|---|---|---|---|---|---|---|
| Peterson, “Bounds for a joint distribution function with fixed subdistribution functions: Application to competing risks” | 1976, PNAS | Bounds on joint/marginal survival under competing risks | Competing-risk subdistribution information | No Huber contamination; survival bounds | Classical sharp bounds for compatible joint distributions; relevant clean partial-identification threat | No rare-group theorem; no generator | Threatens any claim that clean censoring bounds are new. Does not combine exact recorded-law Huber contamination with the present finite operator in the sources inspected. | Abstract/metadata and cited discussion | [1] |
| Mukherjee et al., “Outlier-Robust Optimal Transport” | 2021, ICML/PMLR | Robust OT under outliers | General distributions, not censoring-specific | Outlier-robust OT / partial-mass coupling | Robust OT formulation for outliers; not a survival identified-set theorem | Generative modeling application | Threatens central OT novelty; leaves survival functional sharpness and observation-operator composition open. | Official paper PDF/metadata | [3] |
| Nietert, Cummings, Goldfeld, “Outlier-Robust Optimal Transport: Duality, Structure, and Statistical Analysis” | 2022, AISTATS/PMLR | Robust Wasserstein distance under Huber contamination | General metric spaces | Removes epsilon outlier mass; robust Wasserstein | Derives duality, structure, statistical guarantees, and minimax robust-estimation connection | Generative-model application; no survival subgroup result | Strongest OT/Huber overlap. A survival-specific result must be more than applying their robust distance to censored records. | Official PMLR page and HTML | [2] |
| Jin, Wise, Paschalidis, “Distributionally Robust Learning in Survival Analysis” | 2025, CHIL/PMLR | Robust Cox prediction | Right-censored survival prediction | Wasserstein ambiguity set; finite-sample behavior | DRL-Cox prediction and conic reformulation; not a sharp latent identified set | No rare-subgroup identification theorem; no compatible-world generator | Closest survival-DRO threat. Difference: predictive model robustness versus population partial identification of latent survival functionals. | Official PMLR page and arXiv abstract | [4] |
| Lin, Gao, Blanchet, Glynn, “Causal Partial Identification via Conditional Optimal Transport” | 2026, AISTATS / arXiv | Causal joint-potential-outcome bounds | Missing counterfactual outcome, not censoring | Conditional/adapted Wasserstein geometry | Continuity and consistent estimation under stronger topology; not censoring contamination | No survival-specific subgroup result; no generator | Threatens generic “OT + partial identification” framing. Difference: causal counterfactual coupling rather than censored event-time observation plus Huber contamination. | arXiv abstract and metadata | [5] |
| Wen and Yang, “Distributionally Robust Optimization via Generative Ambiguity Modeling” | 2026, ICLR | DRO ambiguity-set construction | No censoring-specific operator | Generative ambiguity sets / GAS-DRO | Stationary convergence and OOD experiments according to official abstract | Generation is central; not survival identification | Threatens any claim that multiple generated plausible distributions are novel by themselves. | Official ICLR abstract; OpenReview bot-gated | [6] |
| Beyhum and Van Keilegom, “Bounds for the regression parameters in dependently censored survival models” | 2025, arXiv/preprint | Partially identified Cox/other regression effects | Censoring dependence left unrestricted | Peterson bounds plus moment inequalities | Bounds and finite-sample inference for regression parameters | No Huber contamination or OT; no generator | Strong survival partial-identification threat. Difference: regression effects and dependent censoring rather than contamination of recorded law and sharp functional diameter. | Full HTML abstract/introduction | [7] |
| Baitairian et al., “Doubly valid and doubly sharp sensitivity analysis to unobserved confounding for survival outcomes” | 2025 preprint / MLHC 2026 listing | Sensitivity to unobserved confounding | Survival outcomes; not the same censoring-contamination model | Sensitivity model, not Huber/OT | “Doubly valid/doubly sharp” survival sensitivity line is a direct threat to broad sharpness language | No compatible-world generator identified in accessible sources | Difference: unobserved confounding and causal sensitivity, not arbitrary recorded-data contamination. Exact theorem comparison remains unresolved. | Search result, accessible preprint landing/PDF metadata, conference listing | [8] |
| DropCens, CRAN package listing | 2026 package listing | Distributionally robust progressive Type-II censoring inference | Progressive Type-II censoring | Package appears Wasserstein-robust by description; intellectual origin not established from registry alone | Registry is not theorem evidence | No evidence of compatible-world generation or rare subgroup theorem | Requires source tracing before any claim. Not used as primary intellectual evidence. | Registry discovery only | [9] |

## Strongest novelty threats

1. **Known Huber/TV plus observation-operator composition.** The one-bin result is an elementary composition of exact Huber overlap and a censoring-channel contraction; it should not be presented as novel without a narrower theorem that adds survival-specific insight.
2. **Classical and modern censoring partial identification.** Peterson-style bounds and recent dependent-censoring work make clean survival nonidentification a mature area.[1][7]
3. **Robust OT under Huber contamination.** Nietert et al. provide a direct robust-Wasserstein/Hüber connection; an OT contribution must survive a close theorem comparison.[2]
4. **Survival DRO.** Jin et al. already study Wasserstein ambiguity in censored survival prediction, narrowing the space for generic “robust survival under Wasserstein uncertainty” claims.[4]
5. **OT partial identification and generated ambiguity sets.** Conditional OT partial identification and GAS-DRO independently cover two parts of the proposed framing.[5][6]

## What remains potentially distinctive

The most plausible remaining target is not “censoring plus contamination” in the abstract. It is a **fully specified subgroup-allocation theorem**: under a trusted subgroup label, fixed clean prevalence, globally bounded arbitrary recorded-data contamination, and subgroup-specific censoring, characterize the exact sharp identified diameter and compare it with label-contaminated and marginal-preserving alternatives. Even this may be a straightforward corollary of general Huber geometry, so novelty remains **CONDITIONAL**, not established.

A second possible target is an exact restricted-class frontier that changes a threshold or decision-stability regime rather than merely shrinking an LP feasible set. No such result was established in Step 02.

## Search limitations

The search was targeted rather than exhaustive. The Peterson primary source was identified through the PNAS record; the NBER paper was used only as a readable secondary discussion. OpenReview was bot-gated for GAS-DRO, so the official ICLR abstract was used. DropCens was located through CRAN listings but no primary methodological paper was verified. These limitations prevent a PASS novelty decision.

## Sources

[1] https://www.pnas.org/doi/10.1073/pnas.73.1.11
[2] https://proceedings.mlr.press/v151/nietert22a.html
[3] https://proceedings.mlr.press/v139/mukherjee21a/mukherjee21a.pdf
[4] https://proceedings.mlr.press/v287/jin25a.html
[5] https://arxiv.org/abs/2506.00257
[6] https://proceedings.iclr.cc/paper_files/paper/2026/hash/9a0ec010802c72b238e41490fa03e4d2-Abstract-Conference.html
[7] https://arxiv.org/html/2503.11210
[8] https://hal.science/hal-05330588v1/file/2510.16560v1.pdf
[9] https://cran.r-project.org/web/packages/available_packages_by_name.html
