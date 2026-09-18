# Candidate 2 Prior Art

## Main finding

The candidate is not equivalent to simply adding another calibration plot, but its strongest claim is not yet a publishable contribution. Pate et al. (2024) introduce calibration plots for transition probabilities using pseudo-values, BLR-IPCW, and MLR-IPCW, with landmarking and multinomial calibration.[1] The 2025 `calibmsm` package operationalizes calibration of transition probabilities between states at landmark times, including binary, multinomial, and pseudo-value approaches.[2][3]

These tools evaluate endpoint transition probabilities, not an explicit ordered-path distribution or dwell-time functional. That leaves a real conceptual distinction. It does **not** establish novelty: competent use at many landmarks, transition-specific scores, and classical multistate model checks can expose many pathway failures.

## Direct threats

| Source | What it establishes | Candidate overlap |
|---|---|---|
| Pate et al. 2024 | Calibration curves for multistate transition probabilities; pseudo-value, BLR-IPCW, MLR-IPCW; simulation and applied example | Direct calibration threat |
| Pate et al. 2025 / `calibmsm` | Landmark calibration for transitions between states; calibration slopes/intercepts and package implementation | Direct implementation threat |
| Spitoni, Lammens & Putter | Proper Brier and KL scores for state occupation and transition probabilities, including censored and dynamic prediction errors | Proper-score threat |
| `mstate` | Mature data preparation, hazard estimation, and Aalen–Johansen/simulation prediction infrastructure | Standard modeling and prediction baseline |
| Putter et al. 2007 | Foundational multistate competing-risk transition-probability framework | Mathematical prior art |
| Health-economic multistate modeling | State occupancy, duration, and transition quantities already support resource/economic analyses | Path/dwell decision threat |

## What the literature does not establish in this gate

No retrieved primary source was found that directly calibrates the complete ordered trajectory distribution or a sequence-specific path functional in the same way `calibmsm` calibrates transition probabilities. This is an unresolved gap, not evidence of novelty. The candidate must show that the gap changes practice after strong transition calibration and proper-score controls.

## Markov identification threat

For a sufficiently regular time-inhomogeneous Markov process, knowledge of the full transition operator for all start/end times is closely tied to the transition intensity through forward/backward equations. Therefore path ambiguity cannot be claimed as fundamental in the full-information Markov setting. The plausible gap is sparse landmark validation, or non-Markov/semi-Markov history dependence. Both require explicit assumptions and a nontrivial bound.

## Verdict

The candidate survives only as a **CONDITIONAL** theorem/evaluation question:

> Under a finite landmark-validation contract, what path-functional error can remain while transition-probability calibration and endpoint proper scores are acceptable?

The direct “calibmsm misses paths” claim is too weak and must not be used as the novelty claim.

Sources consulted: [1][2][3]. Additional sources: [4][5][6]. Dataset sources: [7][8]. Comparator sources: [9][10].

## Sources

[1] https://doi.org/10.1002/sim.10094 — Pate et al. 2024 calibration plots
[2] https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0320504 — Pate et al. 2025 calibmsm
[3] https://cran.r-project.org/package=calibmsm — CRAN calibmsm
[4] https://doi.org/10.1002/bimj.201600191 — Spitoni et al. prediction errors
[5] https://cran.r-project.org/package=mstate — CRAN mstate
[6] https://physionet.org/content/mimiciv/3.1 — MIMIC-IV
[7] https://physionet.org/content/eicu-crd/2.0 — eICU-CRD
[8] https://doi.org/10.1002/sim.2712 — Putter et al. 2007 multistate
[9] https://pmc.ncbi.nlm.nih.gov/articles/PMC11521377 — Competing-risk decision analysis
[10] https://figshare.com/articles/dataset/Data_required_for_running_vignettes_with_calibmsm_R_package/27635844 — calibmsm example data
