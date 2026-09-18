# Candidate 2 Path Theory

## Definitions

- **State occupancy:** `P(X(t)=k)` or conditional occupancy given a landmark state/history.
- **Transition probability:** `P_{jk}(s,t)=P(X(t)=k | X(s)=j)`.
- **Transition intensity:** instantaneous rate for an allowed transition, conditional on the model history.
- **Dwell/sojourn time:** time spent in a state before leaving it.
- **Pathway:** ordered visited states together with transition times over `[s,t]`.
- **Landmark prediction:** prediction conditional on information available at landmark `s` for a future time `t`.

`calibmsm` targets transition-probability calibration, not a full path-distribution calibration object.[2][3]

## Elementary path counterexample

Process A follows `1 -> 2 -> 4`; process B follows `1 -> 3 -> 4`. Both end in state 4 with probability one at the chosen horizon, but the probability of visiting state 2 differs. A sparse endpoint transition check cannot distinguish them.

Status: **ELEMENTARY**.

## Dwell-time counterexample

The discrete trajectories `(1,2,2,4)` and `(1,2,4,4)` end in state 4 and have different time spent in state 2. A single endpoint occupancy probability does not identify dwell burden.

Status: **ELEMENTARY**.

## Multiple-landmark kill test

Additional landmarks can expose differences in occupancy or transition probabilities. If all state-to-state transition probabilities are known for all start/end times under a regular Markov model, the transition operator contains substantially more information than a finite landmark table and is linked to the intensity matrix through standard evolution equations. Therefore the candidate cannot claim unrestricted Markov path nonidentifiability.

For a finite set of landmarks, path differences can remain. The tiny fixture does not prove that they remain after competent dense validation.

Status: **CONDITIONAL / OPEN**.

## Semi-Markov/history-dependent regime

Duration dependence, recurrent-state history, or clock-reset behavior can make future transitions depend on more than the current state. Such models can share selected transition probabilities while differing in trajectory distribution. However, moving to this regime increases assumptions, data requirements, and model-checking burden. It is not justified merely to manufacture novelty.

Status: **OPEN, high risk**.

## Path-functional hierarchy

| Functional | Standard transition calibration detects directly? | Comment |
|---|---|---|
| State occupancy at `t` | Yes | Direct destination probability |
| Transition probability `j -> k` | Yes | Direct `calibmsm` target |
| Probability of visiting adverse state before `t` | Sometimes | Can be derived with an absorbing-state augmentation; not always in a reported prediction object |
| Expected time in state | Not necessarily | Needs occupancy integration or a duration functional |
| Ordered sequence probability | Not directly | Requires path/sequence information |
| Transition-time distribution | Not directly from one endpoint | May be exposed by dense landmarks/intensity checks |
| Recovery-then-relapse sequence | Not directly from one endpoint | May be represented by an expanded state graph |

No new metric is proposed in Step 00.

## Strongest theorem candidate

A possible theorem would bound error in a specified path functional under finite transition-probability calibration tolerances, with explicit graph, intensity, and smoothness assumptions. This is stronger than the elementary path example but was not derived.

Theorem status: **CONDITIONAL**, not a contribution.

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
