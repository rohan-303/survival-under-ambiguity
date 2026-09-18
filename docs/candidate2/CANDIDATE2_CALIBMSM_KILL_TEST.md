# Candidate 2 `calibmsm` Kill Test

## What `calibmsm` validates

The package assesses calibration of an existing multistate model's transition probabilities using binary or multinomial regression with inverse-probability-of-censoring weights, or pseudo-values from the Aalen–Johansen estimator. It uses landmarking and can assess predictions at any landmark time.[2][3] The 2024 paper reports pseudo-value, BLR-IPCW, and MLR-IPCW calibration approaches and simulation performance under censoring.[1]

The prediction object is a collection of destination-state probabilities conditional on source state and landmark. It is not an ordered trajectory distribution.

## Fair comparison matrix

| Failure type | Baseline use | Every relevant source state | Multiple landmarks | Strongest fair verdict |
|---|---|---|---|---|
| Endpoint occupancy error | Detects | Detects | Detects | `calibmsm` directly detects |
| Direct transition-probability error | Detects | Detects | Detects | `calibmsm` directly detects |
| Different intermediate path, same endpoint | May miss | May still miss if only endpoint probabilities are reported | Can expose occupancy/timing differences | Not automatically solved; not yet novel |
| Different dwell time, same endpoint | May miss | May miss | Dense landmarks can expose integrated occupancy | Conditional gap only |
| Sequence-specific decision error | Not directly | Not directly unless states are expanded | May expose correlates | Requires path-functional validation |
| Non-Markov history dependence | Not directly | Not directly | Selected landmarks may miss it | High-risk residual gap |

## Competent analyst standard

The comparison is not one baseline calibration plot. A competent analyst would assess every relevant source state, destination state, and clinically chosen landmark; use multinomial calibration where appropriate; inspect calibration slopes/intercepts; and use pseudo-value or IPCW methods. This would detect many proposed pathway failures before any new path metric is needed.[1][2][3]

## Kill result

`calibmsm` does not directly calibrate ordered paths or dwell-time distributions, but the remaining gap is only meaningful if a path-sensitive quantity remains materially wrong after this full validation contract and after state-occupation/transition proper scores. That has not been shown.

Gate implication: **Path-Specific Evaluation Gap = CONDITIONAL**, not PASS.

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
