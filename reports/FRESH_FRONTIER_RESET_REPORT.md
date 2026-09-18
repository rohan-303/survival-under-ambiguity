# Fresh Frontier Reset Report — Trustworthy Clinical ML

## 1. Status

`COMPLETE_WITH_WARNINGS — CONDITIONAL FRONTIER RESET`

No new repository, model, dataset download, or implementation was created. The Step 09 shortlist is exhausted; this is an independent frontier search.

## 2. Starting HEAD

`5e13757495db361c35e27b96fe39eb3759465c2f`

Repository preflight passed on `main`, with the canonical origin, `origin/main` tracking, clean worktree, successful `git pull --ff-only`, and recent history inspected.

## 3. Why the Step 09 shortlist is exhausted

Candidate 1 was occupied by competing-risk calibration and proper vector scoring. Candidate 2 was not distinct from multistate calibration, proper scores, and model checking. Candidate 3 was occupied by informative presence, DeepJoint/clinical-presence shift, and direct MIMIC-IV/eICU observation-process evidence. None is revived here.

## 4. Search scope

The search covered deployment feedback, counterfactual prediction, delayed-label monitoring, foundation-model portability, selective prediction and deferral, label provenance, uncertainty, temporal reproducibility, causal transport, unlearning, clinical NLP drift, imaging acquisition shift, and decision-focused measurement acquisition. Sources were prioritized from 2024–2026 primary/official records, with foundational methods used for context. Search results are navigation evidence; claims below are bounded to retrieved sources.

## 5. Current clinical-AI frontier map

The map records seventeen independent families. The broad areas are active rather than empty: clinical-presence and workflow dependence are established; external validation and generalization guidance are mature concerns; foundation-model portability is now directly documented; missingness and label provenance are recognized methodological problems.[1][3][7]

The most promising fresh pressure points are not another architecture or another external validation. They are: (a) the estimand and guarantee for monitoring with delayed/selectively mature labels; (b) deletion-specific clinical safety after unlearning; and (c) pre-label semantic drift monitoring in clinical NLP.

## 6. Deployment-feedback literature

The broad loop `prediction -> action -> changed outcome -> future label` is not a fresh observation. A valid project would need a precise distinction between untreated-risk prediction, actual-policy outcome prediction, treatment-effect ranking, and label provenance. Public MIMIC/eICU sources expose clinical variables, timestamps, and treatments, but not the complete model-version, alert, clinician-response, and override log needed to identify an actual deployed feedback loop.[8][9]

The four separable questions are: F-A monitoring after feedback; F-B retraining after feedback; F-C untreated counterfactual risk; and F-D ground-truth provenance after AI deployment. They must not be bundled. F-A–F-D were not selected because the decisive deployment variables are unavailable and the broad theory is adjacent to performative prediction and causal prediction.

## 7. Counterfactual prediction literature

Counterfactual prediction under treatment policies is a real neighboring field, not an empty gap. A new candidate cannot rename treatment-policy prediction as monitoring. A credible question must specify which potential outcome is monitored, what treatment policy is being evaluated, and what exchangeability/positivity assumptions make the target estimable. No candidate passed this gate with a public-data contract.

## 8. Post-deployment monitoring literature

Drift detection, calibration monitoring, delayed labels, and external validation already provide broad tools. The unresolved possibility is a guarantee for the period when labels are delayed and labels that mature first are selected by follow-up, treatment, or model-mediated workflow. Q4 is worthwhile only if a literature gate shows a coverage/identifiability result beyond ordinary drift scores and temporal calibration.

## 9. Foundation-model portability

The 2026 “portability paradox” study reports that a clinical foundation model can outperform traditional models internally but lose its advantage externally, especially for rare outcomes.[3] Therefore “evaluate a clinical foundation model externally” is rejected. A narrower uncertainty/selective-risk question remains, but it must outperform ordinary calibration and OOD detection without requiring foundation-model training.

## 10. Selective prediction and human deferral

Selective prediction and responsible generalization are active. Goetz et al. frame selective prediction as one response to clinical generalization challenges.[6] Human deferral is not equivalent to a perfect oracle: expertise, workload, queueing, disagreement, and access change system utility. Q6 remains a near-miss only because public retrospective datasets do not contain the human-performance and workload variables needed for a defensible clinical claim.

## 11. Additional independent frontiers

The additional families searched were label provenance/circular evaluation, temporal pipeline reproducibility, patient-level unlearning audits, clinical NLP semantic drift, imaging acquisition-shift uncertainty, causal transport under treatment availability, and value-of-information measurement acquisition. Each is independent of the closed survival-ambiguity line and Candidates 1–3, but each has a clear prior-art kill condition documented in `FRESH_FRONTIER_MAP.md`.

## 12. Candidate questions

Eighteen falsifiable questions were generated in `docs/frontier_reset/FRESH_CANDIDATES.md`. The leading question is:

> Can valid deployment-time selective-risk guarantees be maintained when labels mature asynchronously, subgroup sample sizes are unequal, and label availability is policy-dependent?

The other leading questions concern patient-level unlearning safety, clinical NLP semantic drift before labels, decision-focused value of the next measurement, realistic clinician deferral, label provenance, model feedback, and temporal pipeline drift.

## 13. Eliminated candidates

- Deployment feedback monitoring/retraining: requires unavailable deployment logs and broad theory is occupied.
- Untreated-risk monitoring: causal prediction and treatment-policy literature are the direct threat.
- Generic delayed-label drift score: ordinary monitoring unless a new guarantee survives.
- Foundation-model external portability: directly occupied by current portability work.
- Generic conformal deferral under shift: explicitly treated as occupied; only a sharper delayed-label/group-risk estimand remains.
- Generic observation-process or measurement-policy work: rejected by Candidate 3 and not revived.
- Human deferral with synthetic clinicians only: simulation-only evidence is insufficient for the deployment claim.
- Generic unlearning score: fails unless patient-level clinical calibration/subgroup safety is the load-bearing result.

## 14. Top five

Q4 delayed-label subgroup-conditional uncertainty; Q9 patient-level unlearning safety audit; Q10 label-free clinical NLP semantic-drift uncertainty; Q12 decision-focused value of the next measurement; Q6 human deferral under heterogeneous expertise and workload. The adversarial reviewer attack and required defense for each are recorded in `FRESH_TOP5.md`.

## 15. Top three

### Q4 — Delayed-label, subgroup-conditional uncertainty

Theory/data-protocol led. Required variables: prediction time, version, subgroup, score/set, outcome and maturation time, eligibility, and action/abstention. MIMIC-IV/eICU can support a protocol benchmark, but not deployed-model proof. CPU/classical computation is sufficient. Kill condition: existing delayed-feedback conformal work already provides the same guarantee.

### Q9 — Patient-level unlearning audit

Benchmark/protocol led. Required variables: patient IDs, deletion set, model version, retraining oracle, predictions, labels, subgroup metadata, and calibration/decision thresholds. Public data may support this without deployment logs, with moderate GPU for retraining. Kill condition: existing unlearning audits already test the full clinical risk contract.

### Q10 — Label-free clinical NLP semantic-drift uncertainty

Benchmark/protocol led. Required variables: note time, model version, text representation, uncertainty, anchor concept labels, outcome labels, and terminology version. MIMIC-IV notes or an approved i2b2/PhysioNet corpus are plausible, but note access and semantic labels are unresolved. CPU/small-GPU inference is sufficient. Kill condition: generic embedding drift plus uncertainty calibration performs equivalently.

## 16. Dataset feasibility

MIMIC-IV and eICU-CRD have official access paths and are suitable for delayed-label, treatment, and temporal protocol work, but they do not contain complete model-deployment logs.[8][9] PhysioNet provides an additional access route and challenge datasets, but variable-level contracts must be checked for every finalist.[10] Clinical NLP requires a separate access/license check. No data were downloaded.

## 17. Deployment-data feasibility

Real deployment data are essential for feedback, model-version contamination, clinician response, and workload claims. They are not strictly essential for Q4/Q9/Q10 if those are framed as protocol/theory/benchmark questions, though deployment logs would strengthen external validity. This distinction prevents a public retrospective dataset from being presented as evidence of an actual deployed feedback loop.

## 18. Compute feasibility

Q4 needs no foundation-model training and can use classical predictors and CPU simulations. Q9 requires moderate GPU only if a neural retraining oracle is selected; classical models should be the first gate. Q10 needs inference with a small encoder or frozen model, not large-scale pretraining. No external GPU server is required at discovery stage.

## 19. Leader status

`NO_CLEAR_LEADER`.

Q4 has the best balance of theoretical distinctness and public-data feasibility, but its prior-art risk is high. Q9 is experimentally feasible but faces generic unlearning-audit literature. Q10 is clinically attractive but has the largest semantic-label and data-access uncertainty.

## 20. Exact recommended next question

Run one dedicated Step 00 for Q4 only:

> Under delayed and selectively maturing clinical outcomes, what assumptions and minimum holdout/randomization design are required for a subgroup-conditional selective-risk monitor to distinguish model degradation from label-maturity artifacts?

The next gate must begin with prior-art and identifiability analysis. Do not implement or download data before it.

## 21. Strongest novelty threat

The strongest overall threat is genericity: after terminology is normalized, a proposed candidate may reduce to drift detection, conformal prediction, causal transport, active learning, machine unlearning, or learning-to-defer. The next Step 00 must kill that possibility before any engineering.

## 22. Files created

- `docs/frontier_reset/FRESH_FRONTIER_MAP.md`
- `docs/frontier_reset/FRESH_CANDIDATES.md`
- `docs/frontier_reset/FRESH_TOP5.md`
- `docs/frontier_reset/FRESH_TOP3.md`
- `docs/frontier_reset/FRESH_DECISION.md`
- `reports/FRESH_FRONTIER_RESET_REPORT.md`

## 23. Sources

[1] Jeanselme et al., “DeepJoint: Robust Survival Modelling Under Clinical Presence Shift,” arXiv:2205.13481, https://arxiv.org/abs/2205.13481

[2] Collins et al., “TRIPOD+AI statement,” BMJ 2024, https://doi.org/10.1136/bmj-2023-078378

[3] Yakdan et al., “The portability paradox of foundation models for clinical decision support,” npj Digital Medicine 2026, https://doi.org/10.1038/s41746-026-02615-4

[4] Zamanian et al., “Analysis of Missingness Scenarios for Observational Health Data,” Journal of Personalized Medicine 2024, https://doi.org/10.3390/jpm14050514

[5] Yamamoto et al., “Observation-process features are associated with larger domain shift in sepsis mortality prediction,” medRxiv 2026, https://doi.org/10.64898/2026.04.05.26350209

[6] Goetz et al., “Generalization—a key challenge for responsible AI in patient-facing clinical applications,” npj Digital Medicine 2024, https://doi.org/10.1038/s41746-024-01127-3

[7] Sisk et al., “Informative presence and observation in routine health data,” JAMIA 2021, https://doi.org/10.1093/jamia/ocaa242

[8] MIMIC-IV official access documentation, https://mimic.mit.edu/

[9] eICU-CRD official access documentation, https://eicu-crd.mit.edu/

[10] PhysioNet official data repository, https://physionet.org/

## 24. Deviations

The attached instruction names several 2025–2026 works without stable bibliographic identifiers. Where an exact record was not independently matched, the report uses a directly verifiable neighboring primary source and labels the limitation rather than assigning unsupported methods or results to an unmatched title. No claim of universal literature coverage is made.

## 25. Limitations

No candidate was tested with deployment logs, randomized withholding, or real clinician workload data. Public-data feasibility is provisional until variable-level contracts and access terms are verified. The map is a discovery artifact, not evidence that any finalist is novel or validated.

## 26. Recommended next step only

One Q4 literature/data kill gate. Do not start it automatically and do not generate another candidate family during that gate.

## Sources

[1] https://arxiv.org/abs/2205.13481
[2] https://doi.org/10.1136/bmj-2023-078378
[3] https://doi.org/10.1038/s41746-026-02615-4
[4] https://doi.org/10.3390/jpm14050514
[5] https://doi.org/10.64898/2026.04.05.26350209
[6] https://doi.org/10.1038/s41746-024-01127-3
[7] https://doi.org/10.1093/jamia/ocaa242
[8] https://mimic.mit.edu
[9] https://eicu-crd.mit.edu
[10] https://physionet.org
