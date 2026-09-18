# Fresh Frontier Reset — Top Three

No candidate is promoted to a new project. These are the three finalists requiring the smallest next gate.

## Q4 — Delayed-label, subgroup-conditional uncertainty

- **Core question:** Can valid deployment-time selective-risk guarantees be maintained with delayed, unequal, and policy-dependent label maturation?
- **Why methods fail:** Standard coverage/calibration does not directly encode asynchronous label availability and subgroup decision harm.
- **Load-bearing contribution:** A theorem/protocol specifying the minimum label maturation, holdout, or randomization required for a valid monitor.
- **Closest threats:** conformal prediction; delayed-feedback monitoring; group fairness/calibration.
- **Exact distinction:** not a generic drift score; it must prove an identifiability/coverage failure or repair condition.
- **Required variables:** prediction timestamp, model version, subgroup, score/set, outcome event and maturation time, censoring/eligibility status, deployment action/abstention.
- **Datasets:** MIMIC-IV/eICU are feasible for delayed outcomes but lack true model-generated intervention logs; use as protocol benchmark, not deployment proof.
- **Compute:** CPU/classical methods sufficient; optional single-GPU model generation not load-bearing.
- **Kill condition:** existing delayed-feedback/conformal work already provides the same guarantee, or no measurable distinction from ordinary temporal calibration.

## Q9 — Patient-level unlearning audit

- **Core question:** Can clinical safety fail after apparently successful patient-level unlearning even when aggregate performance is unchanged?
- **Load-bearing contribution:** Patient-level calibration, uncertainty, and subgroup safety estimands tied to deletion, with retraining oracle as comparator.
- **Exact distinction:** deletion-specific clinical risk contract, not another forgetting score.
- **Required variables:** patient IDs, model version/checkpoint, deletion set, retraining oracle, predictions, labels, subgroup metadata, calibration/decision thresholds.
- **Datasets:** public MIMIC/CheXpert-style data only if a reproducible model and legal patient-level grouping are available; no deployment logs required.
- **Compute:** moderate GPU for model retraining; classical baselines first.
- **Kill condition:** published audits already test the full clinical contract, or no safe deletion oracle can be constructed.

## Q10 — Label-free clinical NLP semantic-drift uncertainty

- **Core question:** Can uncertainty detect clinically meaningful semantic drift before outcome labels arrive, separating terminology drift from population-risk drift?
- **Load-bearing contribution:** Clinical anchor-based diagnostic with prospective annotation trigger and false-alarm/late-alarm comparison.
- **Exact distinction:** clinical semantic decomposition beyond embedding-distribution drift.
- **Required variables:** note timestamp, model version, text representation, uncertainty, anchor concept labels, eventual outcome labels, coding/terminology version.
- **Datasets:** MIMIC-IV notes access or i2b2/PhysioNet corpora; exact label and license compatibility must be verified before Step 00.
- **Compute:** CPU/small GPU inference; no foundation-model training.
- **Kill condition:** generic embedding drift plus uncertainty calibration matches the proposed diagnostic.
