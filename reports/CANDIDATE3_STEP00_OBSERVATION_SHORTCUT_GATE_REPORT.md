# Candidate 3 Step 00 — Observation Shortcut Gate Report

## 1. Status

`COMPLETE_WITH_WARNINGS — CANDIDATE 3 FAILED`

This was a pre-project gate. No new repository, model, large dataset, or method was created.

## 2. Starting HEAD

`54f1badb1fac309a5cc80fc697cfc6cc169cd05b`

Preflight passed on `main`; origin and upstream were correct; `git pull --ff-only` reported already up to date.

## 3. Candidate question

Can longitudinal prediction models use visit frequency or laboratory-order intensity to perform well internally but fail after a care-process change, and can a controlled observation-policy intervention separate stable physiology from mutable workflow dependence?

## 4. Broad-hypothesis verdict

`YES — SUBSTANTIALLY ESTABLISHED.` This is not a surviving frontier. Sisk et al. review informative presence and observation. DeepJoint explicitly models longitudinal, inter-observation, and missingness processes and evaluates weekday/weekend clinical-presence shift. The 2026 MIMIC-IV/eICU-CRD preprint directly reports the proposed count-feature domain-shift failure, including external AUROC and calibration degradation.

## 5. Data-generating objects

`L(t)`, `V(t)`, and `M_j(t)` were separated. Visit presence is not equivalent to conditional test ordering. Last-value and variability features can encode observation intensity. The policy map `O=A_pi(L)` is useful notation but not an identified causal object in ordinary EHR data.

## 6. Prior-art comparisons

### Informative presence and observation

Sisk et al. define informative presence as informative patient-data presence/absence and informative observation as its longitudinal counterpart. Their review covers derived predictors, modeling under informative presence, and latent structures; 24 of 36 included articles used missing indicators or summary measures as predictors. This directly occupies the proposed signal.

### DeepJoint 2022

Jeanselme et al. define clinical presence through observation times, test order, and missingness, then jointly model longitudinal evolution, inter-observation times, missingness patterns, and survival. The MIMIC-III laboratory experiment includes weekday/weekend transfer evaluation. The paper states that simple count features can be vulnerable under observation-process covariate shift. This is the strongest direct threat.

### Clinical Presence Shift 2025/2026 comparison

The exact later title supplied in the instruction was not independently matched in the bounded bibliographic indexes. The verifiable DeepJoint preprint already contains the claimed architecture-level and shift-level overlap. The report therefore does not attribute unverified details to the unmatched title.

### 2026 cross-database study

Yamamoto et al., medRxiv DOI `10.64898/2026.04.05.26350209`, evaluates MIMIC-IV to eICU-CRD sepsis mortality prediction. The indexed abstract reports more than 60,000 patients, physiologic summaries and measurement counts, internal AUROC improvement from 0.819 to 0.834 for richer summaries, external AUROC changes of -0.047 versus -0.082, and worsening external calibration as feature complexity increases. This directly establishes the broad candidate failure mode. It is a preprint, so those results remain preliminary, but they are sufficient as a novelty threat.

### Missingness-policy shift

Zamanian et al., DOI `10.3390/jpm14050514`, analyze ten missingness scenarios arising from measurement, recording, preprocessing, physicians, patients, facilities, and data scientists, and emphasize estimand, identification, estimation, and sensitivity analysis. Observation-policy change is not an unoccupied missingness concept.

### Visit versus measurement process

The separation is real and useful: `V(t)` determines encounters, while `M_j(t)` determines variables recorded conditional on an encounter. DeepJoint’s longitudinal/inter-observation/missingness decomposition already provides a close operational decomposition. A two-stage shift table alone is descriptive, not a novel result.

## 7. Policy intervention and theorem attempt

For passive recording intervention, `O_pi=A_pi(L)` and `O_pi'=A_pi'(L)` differ while latent physiology and treatment are fixed. An ideal predictor based on sufficient latent state is invariant. This is a direct consequence of the assumptions. Fitted-model instability does not prove shortcut reliance because masking can remove information, timestamps can carry legitimate disease dynamics, and monitoring can alter treatment.

Matched-information interventions—same counts, variables, and summaries but different selection/timing—are not automatically coherent or identifiable. Selection can be severity-dependent; timestamps can change the meaning of temporal features; synthetic records may not correspond to any policy. No one-sided shortcut certificate was derived.

## 8. Step 08 independence

The setting differs from Step 08 because censoring changes outcome follow-up whereas observation policy changes predictor acquisition. However, both proposed arguments rely on generic invariance under a nuisance intervention, and both face an information-loss confound. Without an observation-specific identification result, independence is only conditional, not a novelty basis.

## 9. External calibration and target-data-free diagnosis

External calibration can detect transport failure but not necessarily attribute it. A target-data-free process-drift warning could be operationally useful, but process-distribution discrepancy does not identify outcome degradation. The 2026 study already shows the empirical association between observation-feature complexity and cross-database degradation. No verified theorem showed that a new source-only diagnostic predicts failure beyond that evidence.

## 10. Real-data and natural-policy feasibility

MIMIC-IV/eICU-CRD is already occupied by the closest 2026 study. HiRID, AmsterdamUMCdb, and eICU internal hospital comparisons are plausible but require verified harmonization, access, site identifiers, and policy labels. No documented laboratory-order or monitoring-policy natural experiment with stable population and adequate overlap was verified. Weekday/weekend is not a policy-identifying natural experiment and is already used by DeepJoint.

## 11. Decision relevance

A developer could restrict workflow features, require local validation after monitoring changes, or abstain outside observation support. Those actions are reasonable, but they are recommendations already implied by clinical-presence and external-validation literature. No new deployment contract was established.

## 12. Gates

- **Original Hypothesis Gate:** `FAIL`
- **Policy-Intervention Theory Gate:** `CONDITIONAL`
- **Evaluation-Gap Gate:** `CONDITIONAL`
- **Deployment-Utility Gate:** `CONDITIONAL`
- **Data Gate:** `CONDITIONAL`
- **Independence Gate:** `CONDITIONAL`
- **Novelty Gate N-C3:** `FAIL`
- **Sufficiency Gate S-C3:** `FAIL`

## 13. Strongest threat and exact surviving contribution

Strongest threat: DeepJoint plus the 2026 MIMIC-IV/eICU-CRD study. Strongest formal result: under a passive observation-map intervention, a sufficient latent-state predictor is invariant; this is elementary and does not identify a fitted model’s dependence. Matched-information interventions did not survive the information-loss and policy-overlap checks.

Exact surviving contribution: none established.

## 14. Master decision

**`C3-H — FAIL FOR MULTIPLE REASONS`**

`NO_SURVIVING_STEP09_CANDIDATE`

## 15. Files created

- `docs/candidate3/CANDIDATE3_PRIOR_ART.md`
- `docs/candidate3/CANDIDATE3_OBSERVATION_PROCESS_MODEL.md`
- `docs/candidate3/CANDIDATE3_CLINICAL_PRESENCE_KILL_TEST.md`
- `docs/candidate3/CANDIDATE3_POLICY_INTERVENTION_THEORY.md`
- `docs/candidate3/CANDIDATE3_DATA_ACCESS.md`
- `docs/candidate3/CANDIDATE3_DEPLOYMENT_USE_CASE.md`
- `docs/candidate3/STEP00_CANDIDATE3_DECISION.md`
- `reports/CANDIDATE3_STEP00_OBSERVATION_SHORTCUT_GATE_REPORT.md`

## 16. Checks

Validation is run after document creation and commit. No models or datasets were downloaded.

## 17. Deviations and limitations

The exact later clinical-presence title supplied in the instruction was not independently matched in bounded indexes; its overlap was not asserted beyond the directly verified DeepJoint source. The 2026 cross-database result is a medRxiv preprint, not a peer-reviewed publication. No causal policy effect is claimed.

## 18. Recommended next step only

Do not create Candidate 4 by mutating this shortlist. If discovery continues, begin a completely fresh frontier search outside the Step 09 candidates.

## Sources

1. Sisk et al., “Informative presence and observation in routine health data,” DOI `10.1093/jamia/ocaa242`: https://doi.org/10.1093/jamia/ocaa242
2. Jeanselme et al., “DeepJoint,” arXiv:2205.13481: https://arxiv.org/abs/2205.13481
3. Zamanian et al., “Analysis of Missingness Scenarios for Observational Health Data,” DOI `10.3390/jpm14050514`: https://doi.org/10.3390/jpm14050514
4. Yamamoto et al., “Observation-process features are associated with larger domain shift in sepsis mortality prediction,” DOI `10.64898/2026.04.05.26350209`: https://doi.org/10.64898/2026.04.05.26350209
