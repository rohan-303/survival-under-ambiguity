# Next Project Candidates

These are discovery candidates only. None authorizes implementation.

## Surviving candidates before top-three selection

### C1 — Hidden regime calibration under external shift
**Question:** Can a survival model appear globally calibrated while being materially miscalibrated in clinically important time-by-risk or site-by-risk regimes under external shift?
**Load-bearing contribution:** a pre-specified, multiplicity-controlled diagnostic that separates global calibration from clinically weighted conditional calibration.
**Independence:** independent of Steps 01–08; it concerns calibration and transport, not ambiguity bounds, auditing corruption, or re-censoring.

### C2 — Competing-risk cause allocation under site shift
**Question:** Can total event-risk calibration remain acceptable while cause-specific risk allocation becomes decision-wrong under site or cause-prevalence shift?
**Load-bearing contribution:** a decision-relevant evaluation decomposition for total incidence versus cause allocation, with transport diagnostics.
**Independence:** independent; the target is competing-risk transport and decisions.

### C3 — Multi-state transition reliability under external validation
**Question:** Which transition-level calibration failures remain hidden when a multi-state model is judged using only aggregate endpoint discrimination and overall calibration?
**Load-bearing contribution:** a transition- and landmark-specific reliability audit tied to clinical decisions.
**Independence:** independent, although it must distinguish itself from `calibmsm`.

### C4 — Selective prediction for competing risks
**Question:** Under competing risks and external shift, can an abstaining predictor guarantee useful risk coverage without masking cause-specific failures?
**Load-bearing contribution:** a selective-risk/coverage estimand with censoring and competing-risk semantics.
**Independence:** independent of old work, but close to conformal survival bands.

### C5 — Observation-process shortcut audit
**Question:** Can longitudinal event predictors remain accurate while relying on visit frequency, lab ordering, or monitoring intensity that fails after a care-process change?
**Load-bearing contribution:** an observation-process stress protocol that distinguishes legitimate time-varying signal from care-process shortcut dependence.
**Independence:** independent if it does not use censoring intervention or re-censoring language.

### C6 — Decision ranking versus survival metric ranking
**Question:** Can models with similar C-index/IBS produce materially different treatment or monitoring decisions across clinically relevant thresholds and horizons?
**Load-bearing contribution:** a pre-registered decision-stability evaluation showing when conventional metric ranking is action-unstable.
**Independence:** independent; it evaluates decisions rather than censoring ambiguity.

### C7 — Missing-modality uncertainty under external shift
**Question:** Does uncertainty remain calibrated conditional on missing-modality patterns when the missingness mechanism changes across sites?
**Load-bearing contribution:** a missingness-conditional selective-risk audit with external validation.
**Independence:** conceptually independent, but conflicts with the separate ShiftSleep-UQ project and is therefore not preferred.

### C8 — Fairness across causes and horizons
**Question:** Can a model satisfy total-risk fairness while producing unequal cause-specific risks or unequal calibration over time for clinically relevant groups?
**Load-bearing contribution:** a cause- and horizon-specific fairness estimand tied to decisions rather than a new loss.
**Independence:** independent, but fairness prior art is extensive.

### C9 — Endpoint-contract sensitivity
**Question:** How often do plausible endpoint-window or administrative-label contracts reverse model ranking or clinical decisions while standard survival metrics remain stable?
**Load-bearing contribution:** an endpoint-contract audit with prespecified clinical action thresholds.
**Independence:** independent in principle, but measurement-error and label-quality literature create a strong overlap threat.

### C10 — Survival foundation-model reliability
**Question:** Do pretrained survival models preserve calibration, cause allocation, and deferral reliability across datasets, or do broad pretraining claims hide transport failures?
**Load-bearing contribution:** a reliability benchmark, not another architecture.
**Independence:** independent, but compute and fast-moving prior art make it high risk.

## Rejected candidates

| Candidate | Decision | Exact reason |
|---|---|---|
| C4 selective competing-risk prediction | Rejected from top three | Conformal survival bands already provide individual survival bands and risk-screening guarantees under right-censoring (Sesia et al., PMLR 266, 2025). A distinction would require a nontrivial competing-risk/site-shift theorem not yet verified. |
| C7 missing-modality uncertainty | Rejected from top three | It overlaps materially with the user's separate ShiftSleep-UQ line and with active conformal/missing-modality work. It would risk duplicating an existing project rather than opening an independent frontier. |
| C9 endpoint-contract sensitivity | Rejected from top three | Strong overlap with endpoint/label quality, administrative leakage, and survival metric evaluation. The distinction from the closed Step 08 line is not yet sharp enough. |
| C10 foundation-model reliability | Rejected from top three | Credible, but requires substantial GPU/model-access expenditure and rapidly changing prior art. It is a benchmark commitment, not the clearest low-compute next question. |
| C8 fairness across causes/horizons | Rejected from top three | Meaningful, but closest prior work already contains distributionally robust survival fairness objectives; the exact estimand would need more than conjunction novelty. |
| C1 hidden regime calibration | Retained | Strong practical sufficiency and low compute, but must defeat the objection that it is merely subgroup calibration. |
| C2 competing-risk transport | Retained | Clear clinical decision consequence and independent setting; requires careful separation from ordinary external validation. |
| C3 multistate reliability | Retained | Public calibration tooling shows the problem is real, while transition-level transport/decision stability may remain open. |
| C5 observation-process shortcuts | Retained | Independent from censoring if framed as care-process dependence and tested on longitudinal records; feasibility/access remain material risks. |
| C6 decision ranking stability | Retained | Directly challenges whether standard metrics answer deployment questions; needs a clinically credible decision contract. |

## Independence rule

No candidate's novelty may depend on a rebranding of OT robustness, censoring perturbation, RMST identification, survival auditing, rare-group fragility, contamination, hypergeometric certification, or the Step 08 re-censoring principle. Generic survival code and public datasets may be reused; the load-bearing question must not be inherited from Steps 01–08.
