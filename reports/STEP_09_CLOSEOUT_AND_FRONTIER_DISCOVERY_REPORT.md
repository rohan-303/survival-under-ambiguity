# Step 09 — Closeout and Independent Frontier Discovery Report

## 1. Final status

`COMPLETE_WITH_WARNINGS`

Step 09 completed its two authorized purposes: the existing research line was formally closed and an independent literature-grounded frontier search was recorded. No new method, model training, large-data download, or Step 10 implementation was started.

## 2. Starting HEAD

`3311ea6d4df28a7955b202c0834fcfbc5a5641e4`

Preflight verified:

- repository root: `C:/Users/rohan/survival-under-ambiguity`;
- branch: `main`;
- origin: `https://github.com/rohan-303/survival-under-ambiguity.git`;
- upstream: `origin/main`;
- worktree clean before edits;
- `git pull --ff-only`: passed;
- starting HEAD matched the required Step 08 commit.

## 3. Current-project final verdict

The current project does not support a sufficiently novel and sufficient publication claim in its investigated forms. This is a final scientific verdict, not a claim that every mathematical component was invalid.

## 4. Research-line closeout

Steps 01–08 were preserved as an auditable sequence: robust OT/censoring, rare-group fragility, audit-information theory, RMST/joint geometry, adversarial auditing, exchangeable audit transfer, and censoring-intervention falsification. Their valid results, failure reasons, corrections, commits, reports, and reusable assets are recorded in `docs/FINAL_RESEARCH_POSTMORTEM.md` and `docs/NEGATIVE_RESULTS_ASSET_MAP.md`.

The repository is now classified as `RESEARCH_LINE_ARCHIVED`. No branch remains implicitly active.

## 5. Valid surviving technical assets

- exact one-bin Huber/censoring and rare-group width formulas;
- finite-grid survival operators and LP bounds;
- adversarial audit impossibility and sharp residual-budget interval;
- hypergeometric finite-population certification;
- exact censoring-operator composition;
- audit enumeration, re-censoring utilities, learners, tests, and reference scripts;
- source ledgers, prior-art matrices, pivot history, and gate reports.

These are reusable assets, not newly claimed publication contributions.

## 6. Invalidated hypotheses

- OT-plus-censoring composition would provide a distinctive primary core;
- rare-group fragility alone would support a survival-specific paper;
- audit-information geometry would supply sufficient novelty;
- joint RMST geometry would yield the claimed coupling gap;
- limited auditing would guarantee exact identification under unrestricted corruption;
- exchangeable transfer would create a survival-specific theorem;
- re-censoring invariance would yield a novel calibrated falsification method.

## 7. Lessons from Steps 01–08

1. A valid formula is not automatically a novel contribution.
2. Weighted functionals must be checked against their exact measure before interpreting numerical gaps.
3. An impossibility result must be separated from a practical sufficient method.
4. Transfer assumptions can reduce a domain result to a standard sampling theorem.
5. A stability principle is not a correctness converse.
6. Pilot discrepancies are not calibrated diagnostics without a valid-model theorem and information matching.
7. Literature occupation and insufficiency are independent rejection reasons.

## 8. Search methodology

The frontier search used targeted web retrieval followed by primary-source page extraction. Queries covered the eight requested directions plus additional searches for competing-risk transport, multistate calibration, longitudinal observation processes, fairness, endpoint contracts, and foundation-model reliability. Search snippets were used only to locate sources; substantive claims were based on extracted proceedings, journal, official repository, or official dataset pages.

The search emphasized 2024–2026 work while retaining foundational sources needed to identify overlap. Each candidate was tested for independence, load-bearing contribution, closest prior art, sufficiency, feasibility, data access, baseline availability, and a falsifiable kill condition.

## 9. Frontier areas reviewed

F1 selective survival prediction; F2 hidden calibration failure; F3 competing risks under distribution shift; F4 multi-state prediction reliability; F5 longitudinal observation-process shortcuts; F6 missing modalities/measurements; F7 survival foundation-model reliability; F8 clinically meaningful decision stability; plus X1 endpoint-contract sensitivity, X2 fairness across causes/horizons, and X3 external-validation transportability.

The complete map is in `docs/NEXT_PROJECT_FRONTIER_MAP.md`.

## 10. Candidate questions generated

Ten concrete questions were generated:

1. Can global survival calibration hide clinically important time/site regime failures?
2. Can total event-risk calibration remain acceptable while cause-specific risk allocation becomes decision-wrong under site shift?
3. Which transition-level calibration failures remain hidden behind aggregate multistate metrics?
4. Can abstention guarantee useful coverage under competing risks and external shift?
5. Can longitudinal predictors rely on visit frequency or lab-order intensity that fails after a care-process change?
6. Can similar C-index/IBS values lead to different treatment or monitoring actions?
7. Does uncertainty remain calibrated conditional on missing-modality patterns under missingness shift?
8. Can total-risk fairness coexist with unequal cause-specific or horizon-specific fairness?
9. Can plausible endpoint contracts reverse model ranking while standard metrics remain stable?
10. Do survival foundation models preserve calibration, cause allocation, and deferral reliability across datasets?

## 11. Rejected candidates

- Selective competing-risk prediction: conformal survival bands already provide a strong direct prior-art result; a new distinction was not verified.
- Missing-modality uncertainty: overlaps the user's separate ShiftSleep-UQ line and active conformal work.
- Endpoint-contract sensitivity: overlaps administrative leakage, endpoint quality, and the closed Step 08 evaluation concern.
- Survival foundation-model reliability: credible but high compute, high access, and rapidly changing prior-art risk.
- Cause/horizon fairness: substantial fairness-survival prior art; a new estimand was not yet distinct.

Exact reasons are recorded in `docs/NEXT_PROJECT_CANDIDATES.md`.

## 12. Top-three candidates

1. Competing-risk cause allocation under site shift.
2. Multi-state transition reliability under external validation.
3. Observation-process shortcuts in longitudinal event prediction.

Complete research contracts are in `docs/NEXT_PROJECT_TOP3.md`.

## 13. Reviewer attacks

- Candidate 1: “This is ordinary competing-risk calibration plus external validation.” Required response: demonstrate a counterexample where all-cause calibration remains acceptable but cause-specific action ranking reverses.
- Candidate 2: “`calibmsm` already solves multistate calibration.” Required response: demonstrate an external, decision-changing failure not targeted by the existing package and prove aggregate calibration is insufficient.
- Candidate 3: “This is missing-data robustness or censoring shift under a new name.” Required response: define an independent observation-policy estimand and demonstrate a real workflow change with persistence after standard missingness/censoring controls.

No candidate currently has a response strong enough to justify implementation immediately.

## 14. Dataset/access verification

- SEER official portal: `https://seer.cancer.gov/data/`; registry/event/cause fields are plausible, but exact access conditions and release fields must be frozen before use.
- MIMIC-IV official PhysioNet page: `https://physionet.org/content/mimiciv/3.1/`; credentialed access, training, and data-use agreement required.
- `calibmsm` package/example data: the paper reports public package and figshare data/code; useful for a reproduction pilot but not a broad external benchmark.
- EBMT/mstate example data: available as package/example material; a second independent benchmark would still be needed.

No large dataset was downloaded. Access verification is official-page verification, not completed ingestion.

## 15. Baseline/code verification

Verified source-level availability for:

- conformal survival bands: PMLR source page;
- meaningful censored-survival evaluation: PMLR source page;
- multistate calibration: `calibmsm` paper and linked CRAN/GitHub package;
- competing-risk model families: PMLR source page for Neural Fine-Gray;
- official dataset access: SEER and PhysioNet pages.

Full baseline installation, version pinning, endpoint compatibility, and execution were **NOT COMPUTED** because Step 09 forbids implementation and model runs.

## 16. Leader selection

`NO_CLEAR_LEADER`.

The candidates remain plausible but each has an unresolved primary-art or feasibility gate. The strongest provisional next question is Candidate 1, but it is not selected as a leader.

## 17. Project Closeout Gate

`CLOSEOUT_COMPLETE`

Reason: the final postmortem, negative-result asset map, archive classification, candidate map, top-three contracts, decision record, and this report exist; no old failed branch remains ambiguously active.

## 18. New-Direction Gate D

`CONDITIONAL`

Independent candidates with substantive possible novelty, sufficiency, public-data paths, and falsifiable plans exist. None has yet passed the exact-overlap and dataset/baseline gates required for implementation.

## 19. Exact recommendation

Do not create a new repository or implement a method yet. Run a dedicated Step 00 only for Candidate 1: verify the exact all-cause-versus-cause-specific transport claim against primary literature, audit SEER and one credentialed EHR source, freeze the decision estimand and split before outcome inspection, and perform the kill test against existing competing-risk evaluation. If that gate fails, compare Candidates 2 and 3 without reviving Steps 01–08.

## 20. Files changed

- `docs/FINAL_RESEARCH_POSTMORTEM.md`
- `docs/NEGATIVE_RESULTS_ASSET_MAP.md`
- `docs/NEXT_PROJECT_FRONTIER_MAP.md`
- `docs/NEXT_PROJECT_CANDIDATES.md`
- `docs/NEXT_PROJECT_TOP3.md`
- `docs/NEXT_PROJECT_DECISION.md`
- `reports/STEP_09_CLOSEOUT_AND_FRONTIER_DISCOVERY_REPORT.md`

No source code, tests, models, datasets, credentials, or new repository were added.

## 21. Literature sources

- Sesia et al., “Conformal Survival Bands for Risk Screening under Right-Censoring,” PMLR 266 (2025): https://proceedings.mlr.press/v266/sesia25a.html
- Qi et al., “An Effective Meaningful Way to Evaluate Survival Models,” ICML/PMLR 202 (2023): https://proceedings.mlr.press/v202/qi23b.html
- Pate et al., “calibmsm,” PLoS One (2025): https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0320504
- Jeanselme et al., “Neural Fine-Gray,” PMLR 209: https://proceedings.mlr.press/v209/jeanselme23a/jeanselme23a.pdf
- Hu et al., “Distributionally Robust Survival Analysis,” PMLR 193: https://proceedings.mlr.press/v193/hu22a.html
- `SurvivEHR` (2026): https://www.nature.com/articles/s41746-026-02709-z
- “Tabular Foundation Models Can Do Survival Analysis” (2026): https://arxiv.org/html/2601.22259v1
- BMJ, “Uncertainty of risk estimates from clinical prediction models” (2024): https://www.bmj.com/content/388/bmj-2024-080749
- TRIPOD+AI statement: https://www.bmj.com/content/385/bmj-2023-078378
- JMLR active feature acquisition source: https://jmlr.org/papers/volume26/23-1635/23-1635.html
- SEER data portal: https://seer.cancer.gov/data/
- MIMIC-IV PhysioNet: https://physionet.org/content/mimiciv/3.1/

## 22. Deviations

- No deviation from the required closeout scope.
- `NO_CLEAR_LEADER` was selected rather than manufacturing a winner.
- Dataset and baseline execution were intentionally not performed because the specification prohibits implementation and downloads.
- No new tests were added because no scientific implementation was required.

## 23. Limitations

- The search is broad but not an exhaustive systematic review.
- Some 2026 sources are rapidly evolving and require rechecking at any future Step 00.
- Dataset access and field semantics were verified from official pages, not by ingestion.
- Baseline code was identified, not installed or run.
- The three candidates remain hypotheses; the report contains no new scientific result.

## 24. Recommended next step only

**Stop at Step 09.** If the project is resumed, run only the dedicated Candidate 1 Step 00 novelty/access gate described in `docs/NEXT_PROJECT_DECISION.md`. Do not implement, train, download large data, or create a new repository before that gate passes.
