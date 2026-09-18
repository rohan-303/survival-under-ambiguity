# Candidate 2 Baselines

## Existing prediction infrastructure

`mstate` provides data preparation, descriptives, hazard estimation, and prediction with Aalen–Johansen or simulation for competing-risk and multistate models.[5] Putter et al. provide the foundational multistate modeling framework behind this ecosystem.[8]

## Calibration baselines

- `calibmsm` binary-IPCW, multinomial-IPCW, and pseudo-value calibration;
- calibration curves, slopes, intercepts, and landmarked transition probabilities;
- state-occupation and transition-probability Brier scores;
- dynamic prediction errors and cross-validation;
- observed-versus-expected transition counts and transition-specific hazard checks.

Pate et al. and Spitoni et al. establish the first groups of these baselines.[1][2][4]

## Path-sensitive comparators

A future implementation would need explicit path functionals: time in state, first-visit probability, ordered-sequence probability, or transition-time distribution. No verified off-the-shelf calibration package for a full ordered path distribution was found in this gate. That absence is not itself novelty.

## Baseline Gate

`CONDITIONAL`: classical, calibration, and proper-score baselines are available; a path-functional comparator would require explicit specification, but no model invention is needed for Step 00.

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
