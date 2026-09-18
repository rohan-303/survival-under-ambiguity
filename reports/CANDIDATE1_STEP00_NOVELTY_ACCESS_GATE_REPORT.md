# Candidate 1 Step 00 — Novelty, Identifiability, Decision, and Data-Access Gate Report

## 1. Status

`COMPLETE_WITH_WARNINGS — CANDIDATE 1 FAILED`

This was a pre-project gate. No new repository, model, large dataset, or method was created.

## 2. Starting HEAD

`3eb66a27ab3476bfd48f4e1d1e98e562c2c34684`

Preflight passed: repository root, `main`, expected HEAD, origin, upstream, clean worktree, and `git pull --ff-only`.

## 3. Candidate question

Can a competing-risk prediction model remain apparently acceptable on aggregate/all-cause risk after transport to a new site while becoming clinically wrong in how it allocates risk across competing causes?

## 4. Mozumder 2025 kill-test result

Mozumder et al. explicitly study external validation of cause-specific absolute risk using cause-specific hazards models. They recommend assessing cause-specific model components, cause-specific absolute risks, all-cause risk, calibration plots, calibration-in-the-large, slopes, Brier score, and IPA, and simulate external baseline-hazard changes.[1] Their results state that miscalibration in one cause can affect cause-specific and all-cause absolute-risk predictions.

This directly occupies the weak candidate claim that aggregate validation is insufficient and cause-specific validation is needed. It does not visibly contain the exact proposed decision-regret supremum, but the direct evaluation-gap claim fails.

## 5. External-validation literature result

van Geloven et al. provide modern competing-risk validation guidance, including targets, calibration, pseudo-observations, and performance measures.[2] Austin et al. provide graphical calibration curves and ICI for competing-risk models.[3] Temporal recalibration literature covers changing external risk relationships.[4] The prior-art result is therefore not an unserved “site-shift causes calibration problems” observation.

## 6. Elementary cancellation result

Predicted cause risks `(0.30,0.20)` and true risks `(0.05,0.45)` both sum to `0.50`, while their allocation vectors differ. Aggregate risk does not identify cause allocation.

Classification: **ELEMENTARY**.

## 7. Decision-reversal result

With an abstract action A that incurs cause-2 loss and action B that incurs cause-1 loss, the preferred action reverses between the predicted and true vectors despite equal total risk.

Classification: **ELEMENTARY decision theory**. It does not establish clinical magnitude or an evaluation gap.

## 8. Proper-scoring-rule kill test

At a fixed horizon, competing-risk outcomes form a cause/event-free probability vector. Joint Brier or other proper vector scores penalize cause misallocation even when all-cause risk is unchanged. Therefore the candidate cannot claim that standard proper competing-risk scores are blind to the phenomenon.

The remaining critique would be that practitioners sometimes report inadequate aggregate metrics. That is insufficient novelty unless a widespread, decision-changing failure is demonstrated.

## 9. Multiclass/vector-calibration threat

The allocation vector is a simplex object analogous to multiclass probabilities at a fixed horizon. A new allocation metric alone would be generic conjunction novelty. Survival-specific value would require nontrivial temporal CIF structure, censoring-aware guarantees, or a decision bound not implied by vector calibration.

## 10. Temporal survival-specificity result

A tiny example keeps total risk at `0.30` while the dominant cause crosses from cause 1 to cause 2 across two horizons. This confirms that allocation trajectories can matter over time. No evidence was found that existing time-dependent competing-risk calibration and validation cannot detect such crossings.

Classification: **ELEMENTARY / OPEN**, not a surviving novelty result.

## 11. Site-shift mechanisms

- **S1 compensating cause-baseline shift:** algebraically feasible, but existing external-validation calibration work already studies cause-specific baseline-hazard changes.[1]
- **S2 covariate-specific cause swap:** feasible in theory, but no stronger theorem or verified dataset was established.
- **S3 total risk and cause allocation both shift:** useful as a future control, not analyzed here.

No full simulation or model execution was permitted.

## 12. Real decision use case

The strongest verified context is oncology: partitioning cancer mortality from cardiovascular and other-cause mortality can matter when considering cardiotoxic cancer treatment.[1] Competing-risk decision analysis is itself established, so this supports only conditional decision relevance.[5]

## 13. SEER access/field audit

SEER’s official page reports population-based cancer registry coverage, tumor and demographic fields, treatment information, and vital-status follow-up.[6] The access page documents registration/SEER*Stat access for Research Data and additional authentication/agreement requirements for Research Plus/NCCR data.[7]

SEER remains **POTENTIALLY_COMPATIBLE**, but this gate did not verify a harmonized site variable, exact cause definitions, or a defensible site-shift partition for the proposed task.

## 14. MIMIC suitability verdict

MIMIC-IV is credentialed and comes from Beth Israel Deaconess Medical Center, with ICU and emergency-department data.[8] It is a single hospital system. A temporal split is not site shift. It therefore cannot satisfy the primary site-shift claim by itself.

Verdict: **INCOMPATIBLE as a standalone site-shift source**.

## 15. Second external dataset search

Searches covered oncology, transplant, cardiovascular, kidney failure/death, and ICU cohorts. No second individual-level dataset pair with verified compatible endpoint definitions, comparable index/horizon, sufficient causes, and genuine site separation was established.

Verdict: **No PASS-level pair found**.

## 16. Endpoint-compatibility result

| Configuration | Compatibility |
|---|---|
| SEER registry partitions | `UNKNOWN` |
| MIMIC-IV temporal split | `INCOMPATIBLE` for site-shift claim |
| SEER + MIMIC-IV | `INCOMPATIBLE` for matched external validation |
| Restricted external oncology/transplant pairs | `UNKNOWN` |

## 17. Baseline availability

Cause-specific hazards, Fine–Gray, Aalen–Johansen, flexible parametric models, competing-risk Brier/IPA, and calibration curves are established baseline families.[1][2] Neural Fine–Gray is a recent comparator.[9] Full installation and execution were not performed.

Baseline Gate: **CONDITIONAL**.

## 18. Strongest prior-art threat

Mozumder et al. 2025 is the strongest direct threat. van Geloven et al. and Austin et al. reinforce that cause-specific calibration is already part of the recommended validation toolkit.[1][2][3]

## 19. Exact surviving contribution

None established.

The only potentially stronger question is an **open** theorem linking explicit aggregate/cause-specific/joint validation tolerances under transport to time-dependent cause-specific decision regret. It was not derived and cannot be claimed as a contribution.

## 20. Theorem Gate

`CONDITIONAL`

Elementary results fail. A possible regret/sufficiency theorem remains open but unverified and potentially occupied.

## 21. Evaluation-Gap Gate

`FAIL`

Existing competing-risk external-validation guidance and Mozumder 2025 directly address the proposed aggregate-versus-cause-specific failure.

## 22. Decision-Relevance Gate

`CONDITIONAL`

The oncology competing-mortality context is credible, but no real action rule and transported decision result were verified.

## 23. Data Gate

`FAIL`

No compatible, verified multi-site pair was established. SEER is plausible but unaudited for this contract; MIMIC-IV is single-site/system.

## 24. Novelty Gate N-C1

`FAIL`

The primary claim is already occupied; the remaining theorem idea is only open.

## 25. Sufficiency Gate S-C1

`CONDITIONAL`

A successful cause-allocation/decision result could affect validation practice, but this was not demonstrated and the direct evaluation gap failed.

## 26. Master decision

`C1-F — FAIL FOR MULTIPLE REASONS`

Reasons: direct prior-art occupation, proper-score detection, elementary core theory, and failure to establish a compatible external-site dataset pair.

## 27. Files created

- `discovery/candidate1/elementary_checks.py`
- `docs/candidate1/CANDIDATE1_PRIOR_ART.md`
- `docs/candidate1/CANDIDATE1_THEORY_PREFLIGHT.md`
- `docs/candidate1/CANDIDATE1_DECISION_USE_CASE.md`
- `docs/candidate1/CANDIDATE1_DATA_ACCESS.md`
- `docs/candidate1/CANDIDATE1_BASELINES.md`
- `docs/candidate1/STEP00_CANDIDATE1_DECISION.md`
- `reports/CANDIDATE1_STEP00_NOVELTY_ACCESS_GATE_REPORT.md`

## 28. Commands/checks

- repository preflight and `git pull --ff-only`: passed;
- tiny mathematical checks: passed;
- `python -m pytest -q`: passed after artifact creation;
- `python -m compileall -q src scripts tests`: passed;
- `git diff --check`: passed before commit;
- no large data download, model training, or new repository: verified by scope.

## 29. Deviations

No scientific-scope deviations. The PMC page was bot-protected, so the open-access article was retrieved through the Europe PMC PDF endpoint and Crossref metadata rather than the PMC HTML page. No claim was based only on a search snippet.

## 30. Limitations

- This was a bounded Step 00 search, not a systematic review.
- The exact decision-regret theorem was not attempted beyond elementary checks.
- SEER endpoint/site fields were not downloaded or inspected.
- MIMIC-IV cause definitions were not derived from data.
- Baseline packages were not installed or run.
- Absence of a discovered dataset pair is not proof that none exists.

## 31. Recommended next step only

**Do not create Candidate 1’s project.** Preserve the failure and return to the archived Step 09 frontier map. If continuing research discovery, evaluate Candidate 2 (multi-state transition reliability) with a separate Step 00, without reopening Steps 01–08 and without treating Candidate 2 as preselected.

Sources consulted: [1][2][3]. Additional sources: [4][5][6]. Dataset sources: [7][8]. Comparator sources: [9][10].

## Sources

[1] https://europepmc.org/api/getPdf?pmcid=PMC12519608 — Mozumder et al. 2025 full text
[2] https://www.bmj.com/content/377/bmj-2021-069249 — van Geloven et al. 2022
[3] https://link.springer.com/article/10.1186/s41512-021-00114-6 — Austin et al. 2022 calibration curves
[4] https://pmc.ncbi.nlm.nih.gov/articles/PMC10946485 — Temporal recalibration
[5] https://pmc.ncbi.nlm.nih.gov/articles/PMC11521377 — Competing-risk decision analysis
[6] https://seer.cancer.gov/data — SEER data
[7] https://seer.cancer.gov/data/access.html — SEER access
[8] https://physionet.org/content/mimiciv/3.1 — MIMIC-IV
[9] https://proceedings.mlr.press/v209/jeanselme23a/jeanselme23a.pdf — Neural Fine-Gray
[10] https://proceedings.mlr.press/v193/hu22a.html — Distributionally robust survival
