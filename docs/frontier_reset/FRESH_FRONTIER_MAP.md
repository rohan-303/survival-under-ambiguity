# Fresh Trustworthy Clinical-ML Frontier Map

## Status and evidence boundary

This is a discovery map, not a novelty claim. Search boundary: primary/official records reachable through OpenAlex, arXiv, PubMed-linked publishers, and official dataset pages; emphasis 2024–2026, with foundational methods where needed. Search results were inspected at title/abstract/full-text level where accessible. Exact absence claims are not made.

## Frontier families

| Family | Established | Open pressure point | Practical importance | Data/compute | Primary threat |
|---|---|---|---|---|---|
| Deployment feedback and performative prediction | Deployment changes treatment, labels, and future data; feedback-aware monitoring is active | Untreated-risk performance and label provenance under model-version feedback | Monitoring, retraining, regulation | Usually requires deployment logs; simulation alone weak | Performative prediction and causal prediction may already cover it |
| Counterfactual prediction under treatment policies | Potential outcomes, dynamic treatment regimes, and off-policy evaluation are established | What estimand should a post-deployment monitor report when treatment is model-mediated? | Correct interpretation of “performance” | MIMIC/eICU treatment data, but no model alerts | Causal prediction literature |
| Delayed-label monitoring | Drift, calibration, and unlabeled monitoring are active | Early warning with delayed, selective, policy-dependent labels | Prevent silent failure | Public EHR timestamps; deployment logs preferred | Ordinary drift detection |
| Foundation-model portability | Internal advantage can disappear externally; portability paradox reported | Portable uncertainty/selective risk rather than AUROC | Deployment eligibility | Public imaging/EHR; inference feasible, training expensive | External validation already crowded |
| Human-AI deferral | Selective prediction and human complementarity are active | Clinician heterogeneity, workload, and queueing change system utility | Routing and staffing | Human-AI studies or simulated clinicians; real logs scarce | Generic learning-to-defer |
| Label provenance and circular evaluation | Labels may be clinician-, rule-, or model-assisted | Evaluation estimands under mixed provenance and version dependence | Audit and retraining | Public datasets rarely record provenance | Label-noise and leakage literature |
| Clinical uncertainty under subgroup shift | Calibration and conformal methods are active | Group-conditional risk guarantees when groups are small and labels delayed | Safe abstention | Public datasets feasible | Conformal/fairness prior art |
| Temporal reproducibility of clinical ML | Temporal/site split best practice is known | Versioned data pipelines and code-system changes create hidden non-reproducibility | Auditability | MIMIC versions, PhysioNet; low compute | Data drift/versioning studies |
| Causal transport of treatment-effect models | Transportability/generalizability theory exists | Decision-safe transport with changing treatment availability | Clinical policy transfer | Multi-site observational data; strong assumptions | Causal transport literature |
| Data deletion and machine unlearning for clinical models | Unlearning methods and audits are active | Patient-level deletion with calibration and subgroup effects preserved | Privacy/compliance | Public models/datasets; compute moderate | Generic unlearning |
| Clinical NLP label semantics | Prompt/label variation affects evaluation | Concept-drift-resistant clinical terminology and uncertainty | EHR phenotyping | MIMIC notes access, i2b2/PhysioNet; access constraints | NLP robustness |
| Imaging acquisition shift | Scanner/protocol shift is well established | Detectable reliability failure without labels and without suppressing rare disease signal | Radiology deployment | CheXpert, MIMIC-CXR, VinDr-CXR; GPU inference | Domain generalization |
| Data valuation and acquisition safety | Active learning and missing-data acquisition are established | Which extra measurement improves decision safety under budget, not AUC? | Test ordering and resource allocation | MIMIC/eICU; causal/action confounding | Active learning and value-of-information |
| Abstention and downstream harm | Selective prediction metrics are known | Coverage guarantees versus asymmetric clinical harm and unequal access | Deployment thresholding | Public data plus explicit utility model | Decision theory and fairness |
