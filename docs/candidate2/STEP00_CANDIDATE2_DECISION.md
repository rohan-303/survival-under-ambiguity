# Step 00 Candidate 2 Decision

## Status

`CANDIDATE2_CLOSED_WITH_FAIL`

## Gate results

| Gate | Result | Reason |
|---|---|---|
| Path-Specific Evaluation Gap | `CONDITIONAL` | `calibmsm` targets transition probabilities, not full paths/dwell times, but dense landmarks and standard scores can expose many failures. |
| Theorem Gate | `CONDITIONAL` | A finite-landmark path-functional bound is an open question; the elementary path example is insufficient. |
| Decision-Relevance Gate | `CONDITIONAL` | Intermediate burden can matter in transplant/relapse/resource settings, but no frozen real decision contract was verified. |
| Data Gate | `CONDITIONAL` | eICU plus MIMIC is plausible but state/site compatibility and identifiers remain unresolved. |
| Multistate-Specificity Gate | `CONDITIONAL` | Timing and state paths matter, but generic sequence/process calibration remains a threat. |
| Novelty Gate N-C2 | `FAIL` | No precise contribution beyond existing calibration, proper scores, and model-checking practice was established. |
| Sufficiency Gate S-C2 | `CONDITIONAL` | A valid path-reliability result could alter validation, but no such result was established. |

## Master decision

**`C2-G — FAIL FOR MULTIPLE REASONS`**

Do not create a new repository, implementation package, benchmark, or model run from Candidate 2.

## Strongest elementary result

Two processes can end in the same state with identical endpoint occupancy while visiting different intermediate states. Likewise, trajectories can share an endpoint while spending different amounts of time in an adverse state. This is elementary path nonidentifiability from sparse endpoint summaries.

## Strongest non-elementary theorem candidate

A possible theorem would bound error in a specified path functional under finite transition-probability calibration tolerances, graph constraints, intensity bounds, and smoothness assumptions. It was not derived, and its novelty against existing multistate model-checking theory remains unresolved.

## Direct answers to kill questions

- **Does `calibmsm` catch the constructed failure?** It directly catches endpoint transition-probability errors. It does not directly evaluate an ordered path or dwell-time distribution. The residual gap is conditional, not a demonstrated evaluation failure.
- **Do proper scores catch it?** State-occupation and transition-probability Brier/KL scores catch endpoint distribution errors, but need not identify ordered paths with identical endpoint distributions.[4]
- **Do multiple landmarks catch it?** They can expose occupancy and timing differences; the finite fixture does not establish that all realistic landmark schedules suffice. Full transition operators under regular Markov assumptions are a stronger identification regime.
- **Markov versus semi-Markov verdict:** Markov ambiguity is only a sparse-validation issue; semi-Markov/history-dependent models preserve more path ambiguity but impose higher complexity and feasibility risk. No regime passed.
- **Strongest real decision use case:** recovery/adverse-event/relapse/death pathway burden after transplantation.[2]
- **Best dataset pair:** MIMIC-IV plus eICU-CRD is the most plausible future pair for an ICU state graph, but it is not verified as compatible.
- **Endpoint compatibility:** `UNKNOWN` for MIMIC/eICU; `INCOMPATIBLE` for `calibmsm` example plus MIMIC as an external pair.
- **Strongest prior-art threat:** Pate et al. 2024/2025 plus Spitoni et al. cover transition calibration and proper dynamic prediction errors.[1][2][4]
- **Exact surviving contribution:** None established.

## Archive rule

Candidate 2 is recorded as a failed independent gate. This does not reopen Steps 01–08 or Candidate 1. The repository remains `RESEARCH_LINE_ARCHIVED`.

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
