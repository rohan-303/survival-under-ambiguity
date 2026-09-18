# Candidate 2 Step 00 — Pathway Reliability Gate Report

## 1. Status

`COMPLETE_WITH_WARNINGS — CANDIDATE 2 FAILED`

This was a pre-project gate. No new repository, model, large dataset, or method was created.

## 2. Starting HEAD

`1e0c7907cca66ed16cfd4c07a9e00fe6757653d5`

Preflight passed: repository root, `main`, expected HEAD, origin, upstream, clean worktree, and `git pull --ff-only`.

## 3. Candidate question

Can a multistate prediction model appear acceptably calibrated for state-occupation or landmark transition probabilities while being materially wrong about intermediate pathways, transition timing, dwell times, or path-dependent decisions under external validation?

## 4. `calibmsm` deep comparison

Pate et al. 2024 introduce calibration plots for transition probabilities using pseudo-values, BLR-IPCW, and MLR-IPCW, with landmarking and simulation under censoring.[1] The 2025 `calibmsm` package implements calibration of transition probabilities between states with binary/multinomial IPCW methods and pseudo-values, including landmark predictions, slopes, and intercepts.[2][3]

The prediction object is destination-state probabilities conditional on a source state and landmark. It is not an ordered trajectory distribution. Therefore a path or dwell functional is not directly calibrated by the package. However, a fair analyst would use every relevant source state, destination state, and multiple clinically meaningful landmarks. Many pathway failures would then be visible through occupancy/timing changes.

## 5. Proper-scoring-rule comparison

Spitoni, Lammens, and Putter study prediction errors for state-occupation and transition probabilities using Brier and Kullback–Leibler scores, prove properness, handle censoring through inverse weighting and pseudo-values, and extend to dynamic prediction errors.[4] These scores evaluate endpoint distributions, not necessarily ordered paths with identical endpoint laws.

This leaves a conceptual path-score gap, but not a demonstrated practical or novel gap. A new metric would be generic unless it yields a theorem or decision guarantee.

## 6. Transition-intensity/model-checking comparison

`mstate` provides hazard estimation and Aalen–Johansen or simulation-based prediction infrastructure.[5] Transition-specific hazard checks, observed-versus-expected transition counts, and standard Markov/semi-Markov model diagnostics are existing tools. No source retrieved in this bounded search supports claiming that transition-intensity model checking is absent.

## 7. Pathway definition

A path over `[s,t]` is the ordered state sequence together with transition times. It differs from state occupancy and from `P_{jk}(s,t)`, which is agnostic to the intermediate route. Path functionals considered were first visit, time in an adverse state, ordered sequence, transition-time distribution, and recovery-then-relapse.

## 8. Elementary path counterexample

Process A follows `1 -> 2 -> 4`; process B follows `1 -> 3 -> 4`. Both end in state 4 with probability one, but the probability of visiting state 2 differs.

Classification: **ELEMENTARY**.

## 9. Dwell-time counterexample

The discrete trajectories `(1,2,2,4)` and `(1,2,4,4)` end in state 4 but spend different amounts of unit time in state 2.

Classification: **ELEMENTARY**.

## 10. Multiple-landmark kill test

Landmarks at intermediate times can expose occupancy and timing differences. If the full transition operator is known for all start/end times under a regular Markov model, it is linked to the transition intensities and contains substantially more information than a finite landmark table. Thus unrestricted Markov path nonidentifiability is not a valid claim.

The residual ambiguity is limited to sparse validation or history-dependent/semi-Markov settings. Neither produced a non-elementary result in this gate.

## 11. Markov identification result

- Finite landmark transition calibration: path functionals can remain underdetermined.
- Full transition operator under regular Markov assumptions: much stronger identification; path ambiguity cannot be asserted without qualification.
- Semi-Markov/history-dependent models: more path ambiguity is possible, but complexity and model-checking burden increase.

Verdict: no Markov/semi-Markov regime passed as a clean primary theory.

## 12. Semi-Markov/history-dependent result

Duration dependence, recurrent-state history, and clock-reset behavior can change trajectory laws while selected transition probabilities agree. This is a plausible residual gap, but introducing it solely to create novelty would be an over-complexity failure. No bounds or external validation result were derived.

## 13. Site-shift mechanisms

- **S1 pathway substitution:** feasible conceptually; not empirically verified.
- **S2 dwell-time shift:** feasible conceptually; could alter resource burden while preserving an endpoint.
- **S3 pathway-specific covariate shift:** unresolved.
- **S4 compensated intensity shift:** algebraically possible; existing Markov process theory is a threat.

No model or simulation was run.

## 14. Path-dependent functionals

State occupancy and direct transition probabilities are standard. First-visit probability may be represented by state-graph augmentation. Expected time in state requires occupancy integration. Ordered sequence and transition-time distributions are not direct `calibmsm` targets, but their practical estimation and model-checking requirements were not solved here.

## 15. Decision-reversal result

Equal endpoint occupancy can coexist with different adverse-state dwell burden or sequence probability. An abstract action penalizing adverse exposure can therefore reverse. This is elementary decision theory, not a validated clinical result.

## 16. Fair strongest-current-validation test

The fair comparator was not one baseline calibration plot. It included all source/destination transitions, multiple landmarks, binary and multinomial calibration, and pseudo-value/IPCW methods.[1][2]
It also included state-occupation and transition proper scores, transition counts, and intensity diagnostics.[4][5]

Under this comparator, endpoint and many timing failures are exposed. A path-specific failure may remain, but no material residual failure was demonstrated.

## 17. Path-Specific Evaluation Gap Gate

`CONDITIONAL`

`calibmsm` does not directly score full paths, but the remaining gap is unproven after competent current validation.

## 18. Theorem Gate

`CONDITIONAL`

A finite-landmark path-functional bound is an open question. The executed theory is elementary.

## 19. Decision-Relevance Gate

`CONDITIONAL`

Transplant recovery/adverse-event/relapse/death pathways provide credible relevance, but no frozen real decision or resource rule was verified.[2]

## 20. Data Gate

`CONDITIONAL`

The MIMIC-IV/eICU-CRD pair is plausible, but state graph, site labels, ascertainment, access, and cross-dataset compatibility remain unresolved.[6][7]

## 21. Multistate-Specificity Gate

`CONDITIONAL`

Continuous time and path order can matter, but the strongest residual problem may generalize to sequence/process calibration unless a multistate-specific theorem is found.

## 22. Novelty Gate N-C2

`FAIL`

No precise claim beyond existing calibration, proper scores, and model-checking practice was established.

## 23. Sufficiency Gate S-C2

`CONDITIONAL`

A successful path-reliability result could change validation or resource planning, but this gate did not establish one.

## 24. Strongest prior-art threat

Pate et al. 2024/2025 and `calibmsm` directly occupy transition calibration.[1][2][3]
Spitoni et al. occupy proper dynamic prediction errors; `mstate` supplies established prediction infrastructure.[4][5]

## 25. Exact surviving contribution

None established. The only remaining candidate is a future theorem controlling path-functional error under finite landmark validation, explicit Markov/semi-Markov assumptions, and a real decision functional.

## 26. Dataset pair

MIMIC-IV plus eICU-CRD is the best plausible pair identified, but not verified as a compatible external-validation pair.[6][7]
`calibmsm` example data are reproducible but not an external site pair.[2][10]

## 27. Endpoint compatibility

| Pair | Status |
|---|---|
| `calibmsm` example + MIMIC-IV | `INCOMPATIBLE` |
| MIMIC-IV + eICU-CRD | `UNKNOWN` |
| eICU internal hospital/unit split | `UNKNOWN` because identifiers are removed |
| independent EBMT/transplant pair | `UNKNOWN` |

## 28. Baseline availability

Classical multistate modeling, `mstate`, and `calibmsm` are available in primary literature and software.[1][2][3]
State/transition Brier and KL scores and dynamic prediction errors are also established.[4][5] Full installation and execution were not performed.

Baseline Gate: **CONDITIONAL**.

## 29. Master decision

`C2-G — FAIL FOR MULTIPLE REASONS`

Reasons: elementary core examples, no non-elementary theorem, direct transition-calibration/proper-score prior art, unresolved external dataset compatibility, and no verified path-dependent decision contract.

## 30. Files created

- `discovery/candidate2/path_checks.py`
- `docs/candidate2/CANDIDATE2_PRIOR_ART.md`
- `docs/candidate2/CANDIDATE2_PATH_THEORY.md`
- `docs/candidate2/CANDIDATE2_CALIBMSM_KILL_TEST.md`
- `docs/candidate2/CANDIDATE2_DECISION_USE_CASE.md`
- `docs/candidate2/CANDIDATE2_DATA_ACCESS.md`
- `docs/candidate2/CANDIDATE2_BASELINES.md`
- `docs/candidate2/STEP00_CANDIDATE2_DECISION.md`
- `reports/CANDIDATE2_STEP00_PATHWAY_RELIABILITY_GATE_REPORT.md`

## 31. Checks

- repository preflight and `git pull --ff-only`: passed;
- tiny path/dwell checks: to be run before commit;
- existing `pytest`: to be run before commit;
- compilation and citation verification: to be run before commit;
- no models, large datasets, or new repository: preserved by scope.

## 32. Deviations

No scientific-scope deviations. The bounded search used primary journal pages, Crossref metadata/abstracts, CRAN package pages, official PhysioNet pages, and the official package/example data link. No claim was based solely on a search snippet.

## 33. Limitations

- This is not a systematic review.
- No full transition-intensity theorem was derived.
- No model fitting, data ingestion, or external validation was performed.
- eICU/MIMIC state compatibility was not inspected at row level.
- Absence of a discovered path-calibration package is not proof of novelty.

## 34. Recommended next step only

**Do not create Candidate 2’s project.** Preserve this failed gate. Do not reopen Candidate 1 or Steps 01–08. If research discovery continues, evaluate the next archived frontier candidate with a fresh Step 00 rather than assuming a survivor.

Sources consulted: [1][2][3].
Additional sources: [4][5][6].
Dataset sources: [7][8].
Comparator sources: [9][10].

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
