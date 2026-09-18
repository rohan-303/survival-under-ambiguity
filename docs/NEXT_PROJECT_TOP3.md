# Next Project Top Three

The following are discovery contracts, not frozen protocols.

## Candidate 1 — Competing-risk cause allocation under site shift

### Core question
Can total event-risk calibration remain acceptable while cause-specific risk allocation becomes decision-wrong under site or cause-prevalence shift?

### Why existing methods may fail
Standard evaluation often reports discrimination and calibration for one endpoint or aggregates causes. A model can preserve all-cause incidence while reallocating risk across causes, which can change treatment selection or monitoring decisions.

### Load-bearing contribution
A decision-linked decomposition that evaluates total cumulative incidence, cause-specific cumulative incidence, calibration, and action ranking separately under prespecified site/temporal transport splits.

### Closest prior work
1. Jeanselme et al., *Neural Fine-Gray*, PMLR 209 (2023), https://proceedings.mlr.press/v209/jeanselme23a/jeanselme23a.pdf — competing-risk modeling; not the same transport/decision audit.
2. Hu et al., *Distributionally Robust Survival Analysis*, PMLR 193 (2022), https://proceedings.mlr.press/v193/hu22a.html — robust/fair survival objective; not the same decomposition.
3. *SurvivEHR* (2026), https://www.nature.com/articles/s41746-026-02709-z — recent competing-risk foundation model; strongest benchmark/model reliability threat.

### Exact novelty claim requiring verification
No claim is currently established. The candidate would need to show that existing competing-risk evaluation does not already test the proposed total-versus-cause decision instability under genuine external shift.

### Theory target
A transport decomposition or impossibility/example showing that all-cause calibration does not control cause-specific calibration or action ranking.

### Experimental design
Freeze cause-specific horizons and action thresholds; train classical cause-specific and Fine–Gray baselines on one site/era; evaluate on held-out sites/eras; compare total-risk calibration, cause allocation, calibration slopes, and decision curves. Use negative controls where cause labels are permuted only within risk sets.

### Public datasets
SEER official data portal (https://seer.cancer.gov/data/); MIMIC-IV official PhysioNet page (https://physionet.org/content/mimiciv/3.1/), credentialed access. A future protocol must verify exact competing-risk fields and split availability.

### Baselines
Cause-specific Cox, Fine–Gray, random survival forest or gradient boosting, and one recent neural competing-risk model. `Neural Fine-Gray` supplies an available comparator; code for every selected baseline must be checked before freezing.

### Kill condition
If all-cause calibration failure always tracks cause-specific failure, or existing papers already provide the same decomposition under external shift, the candidate is killed.

### Estimated research risk
MEDIUM.

### Adversarial reviewer attack
“This is ordinary competing-risk calibration plus external validation.”

### Required response
Pre-register a counterexample/evaluation where total-risk calibration and discrimination remain acceptable while cause-specific action ranking reverses, and prove that the distinction is not a subgroup or censoring perturbation artifact.

## Candidate 2 — Multi-state transition reliability under external validation

### Core question
Which transition-level calibration failures remain hidden when a multi-state model is judged only with aggregate endpoint metrics?

### Why existing methods may fail
Multi-state models produce transition probabilities at landmarks, but aggregate endpoint summaries can conceal a single clinically important transition failure. `calibmsm` shows calibration assessment is possible and that evaluation is uncommon; it also creates the strongest overlap threat.

### Load-bearing contribution
A transition/landmark reliability audit tied to one or more clinical decisions, with explicit separation of transition calibration from endpoint calibration.

### Closest prior work
1. Pate et al., *calibmsm*, PLoS One (2025), https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0320504 — direct calibration tooling and overlap.
2. BMJ, *Uncertainty of risk estimates from clinical prediction models* (2024), https://www.bmj.com/content/388/bmj-2024-080749 — clinical uncertainty framing.
3. `mstate`/EBMT examples and related multistate prediction literature — established modeling ecosystem; exact comparator set requires a fresh search.

### Exact novelty claim requiring verification
Only a narrower claim may survive: external-transport and action-level failure can remain hidden after transition calibration tooling exists. This is unresolved, not asserted.

### Theory target
Construct an example in which aggregate state occupancy is calibrated while one transition probability is miscalibrated enough to reverse a transition-specific decision.

### Experimental design
Use landmarked transition predictions, preselect a transition and threshold, evaluate calibration curves/slopes, transition-specific Brier/log scores, and action ranking across temporal/site splits. Compare with aggregate endpoint evaluation.

### Public datasets
The `calibmsm` worked example and package data (code/data links are provided by the paper); MIMIC-IV for a larger longitudinal cohort, subject to credentialed access. A second dataset would be required before implementation.

### Baselines
Cause/state-specific Cox or multinomial landmark models, `mstate`/`flexmsm`-style models, and `calibmsm` evaluation. No neural model is needed initially.

### Kill condition
If transition-level calibration adds no information beyond endpoint calibration or if the candidate reduces to the existing `calibmsm` workflow, kill it.

### Estimated research risk
MEDIUM.

### Adversarial reviewer attack
“`calibmsm` already solves multistate calibration; you have only added landmarks and plots.”

### Required response
Demonstrate an externally validated, decision-changing failure that `calibmsm` does not target, and provide a formal construction proving aggregate calibration is insufficient.

## Candidate 3 — Observation-process shortcuts in longitudinal event prediction

### Core question
Can a longitudinal event predictor remain accurate while depending on visit frequency, lab ordering, or monitoring intensity that fails after a care-process change?

### Why existing methods may fail
Observation intensity is often predictive because it reflects clinical concern, access, and workflow. A model may therefore exploit care-process variables that are unstable under scheduling, staffing, or policy changes. This is not the Step 08 censoring intervention: the object is the longitudinal observation process and its operational mechanism, not artificial re-censoring of survival records.

### Load-bearing contribution
A reproducible observation-process audit with care-process perturbation or naturally occurring schedule changes, separating legitimate time-varying signal from workflow shortcut dependence.

### Closest prior work
1. JMLR 26, “Evaluation of Active Feature Acquisition Methods for Time-varying …”, https://jmlr.org/papers/volume26/23-1635/23-1635.html — active acquisition; likely overlap in observation decisions.
2. MIMIC-IV official data, https://physionet.org/content/mimiciv/3.1/ — source of charting/measurement times and outcomes, not a method paper.
3. TRIPOD+AI, BMJ (2024), https://www.bmj.com/content/385/bmj-2023-078378 — reporting/validation standard and a threat to claims of methodological novelty.

### Exact novelty claim requiring verification
A substantive claim would require evidence that existing missingness/irregular-sampling audits do not provide a valid, longitudinal, outcome-preserving care-process stress test.

### Theory target
An estimand separating outcome signal from observation-policy signal under an explicit observation-policy change; otherwise this remains a benchmark protocol rather than theory.

### Experimental design
Freeze an event-prediction task and observation variables; compare full histories with observation-policy-normalized or schedule-matched histories; use temporal/site splits and negative controls. Do not use latent event times or re-censoring interventions.

### Public datasets
MIMIC-IV and eICU are plausible but access/field semantics require verification. A dataset must retain timestamps, repeated measurements, observation indicators, and an outcome window.

### Baselines
A model without observation metadata, a standard time-series model, and a model with observation features; compare external/temporal transport and decision metrics.

### Kill condition
If removing observation-process features causes no transport change, or if differences disappear after ordinary covariate adjustment, kill the candidate.

### Estimated research risk
HIGH.

### Adversarial reviewer attack
“This is missing-data robustness or censoring-distribution shift under a new name.”

### Required response
Define observation-process variables and intervention independently of censoring, demonstrate a real care-workflow change, and show that the failure persists after standard missingness and censoring controls.
