# Candidate 2 Decision Use Case

## Candidate use case

The most credible use case is path-dependent burden in recovery/relapse/death or adverse-event pathways after treatment. The `calibmsm` worked example concerns recovery, adverse events, relapse, and survival after transplantation.[2] A model can have acceptable final-state or transition probabilities while misrepresenting time spent in an adverse state or the probability of recovery followed by relapse.

## Decision model

Let an abstract action depend on a path functional such as expected time in an adverse state or probability of an adverse transition before recovery. Define `d*=argmin_d E[L(d,P)|X]`. Two processes with identical endpoint occupancy can have different expected path loss and therefore different preferred actions.

## Decision-reversal result

The path fixtures show equal endpoint state 4 occupancy but different intermediate-state visits and dwell counts. An action penalizing adverse-state exposure can therefore reverse. This is elementary decision theory, not clinical evidence.

## Existing decision-analysis threat

Competing-risk decision analysis already studies how competing events affect risk-benefit decisions.[9] Health-economic multistate models also routinely use state occupancy and time-in-state quantities. Candidate 2 cannot claim that intermediate burden matters without a specific under-measured reliability result.

## Gate assessment

Decision-Relevance Gate: **CONDITIONAL**. The transplant/recovery/relapse setting is credible, but no verified deployment decision, resource rule, or external cohort was established in this gate.

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
