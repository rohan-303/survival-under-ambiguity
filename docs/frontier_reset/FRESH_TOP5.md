# Fresh Frontier Reset — Top Five

## 1. Q4 — Delayed-label, subgroup-conditional uncertainty under deployment shift

**Question:** Can a monitor maintain valid selective-risk/calibration guarantees when outcome labels mature asynchronously and subgroup sizes differ across sites?

**Why current methods may fail:** Ordinary conformal/selective prediction assumes a fixed exchangeability regime and observed labels; ordinary drift monitoring may flag covariate movement without certifying decision risk.

**Load-bearing contribution:** An identification/guarantee separating label maturity, subgroup scarcity, and genuine reliability degradation, with explicit abstention consequences.

**Closest threats:** conformal prediction, group-conditional calibration, delayed feedback monitoring. Exact distinction must be a valid deployment-time guarantee, not another drift score.

**Required experiment/data:** MIMIC-IV/eICU or PhysioNet temporal cohorts; synthetic delayed-label mechanism only for theorem validation; subgroup and time splits; baseline conformal and calibration monitors.

**Attack:** “This is conformal prediction plus delayed labels.” To survive, it needs a theorem or falsification result showing why standard coverage is invalid and what minimal label/holdout design repairs it.

**Feasibility:** Medium; no actual deployed model required if framed as a protocol/theory benchmark. Prior-art risk high.

## 2. Q9 — Patient-level unlearning audit beyond aggregate performance

**Question:** Can deletion of individual clinical records preserve aggregate discrimination while changing calibration, subgroup risk, or uncertainty in ways current unlearning audits miss?

**Load-bearing contribution:** A clinical safety audit protocol with deletion-specific estimands and failure cases, not a new unlearning algorithm.

**Closest threats:** machine-unlearning definitions, membership-inference audits, certified deletion. Exact distinction is clinical decision safety after deletion.

**Required experiment/data:** Public clinical model and dataset with patient grouping; compare retraining oracle, unlearning method, and no-deletion model; inspect calibration/subgroups/uncertainty.

**Attack:** “Unlearning audit metrics already exist.” Survival requires a clinically grounded counterexample where parameter-level deletion criteria pass but patient-level risk contract fails.

**Feasibility:** Medium; public data and moderate GPU. Prior-art risk high.

## 3. Q10 — Label-free clinical NLP semantic-drift uncertainty monitor

**Question:** Can uncertainty detect clinical terminology/concept drift before labels arrive while distinguishing vocabulary change from population risk change?

**Load-bearing contribution:** A pre-label diagnostic with negative controls and a decision rule for when annotation is required.

**Closest threats:** NLP drift detection, OOD detection, language-model uncertainty, clinical concept drift.

**Required experiment/data:** MIMIC-IV notes or i2b2/PhysioNet if access allows; time-sliced notes, frozen anchor concepts, delayed labels; smaller encoder/LLM inference only.

**Attack:** “This is generic embedding drift.” Survival requires a clinical-semantic decomposition and demonstrated reduction in false alarms/late alarms against generic drift monitors.

**Feasibility:** Medium, but notes access and annotation are risks.

## 4. Q12 — Decision-focused value of the next measurement

**Question:** Can a measurement-acquisition policy reduce clinical decision loss under a cost budget when the measured value changes both prediction and treatment choice?

**Load-bearing contribution:** Decision-focused value-of-information estimand under action confounding, not another active-learning score.

**Closest threats:** active learning, optimal experimental design, value of information, adaptive testing.

**Required experiment/data:** MIMIC/eICU measurements, treatment proxies, explicit utility; causal sensitivity analysis; no deep model needed.

**Attack:** “This is active learning with medical vocabulary.” Survival needs a decision-theoretic result under clinical-action confounding and a clinically meaningful policy comparison.

**Feasibility:** Medium-low; observational actions and utility are difficult.

## 5. Q6 — Human deferral under workload and heterogeneous expertise

**Question:** When does deferral improve system utility after clinician skill, time, disagreement, and queueing are modeled?

**Load-bearing contribution:** A clinically grounded system-level estimand or impossibility result for deferral, not a new router.

**Closest threats:** learning-to-defer, human-AI complementarity, triage optimization.

**Required experiment/data:** Human-AI decision data or a validated clinician-performance dataset; public retrospective clinical data alone are insufficient.

**Attack:** “The human model is synthetic and the result is not clinically transportable.” Survival requires real or externally supported human-performance data.

**Feasibility:** Low without collaboration; prior-art risk high.
