# M2 Theorem Candidates

All candidates remain provisional. None is labeled novel.

## T1 — Trusted-label one-bin diameter

- **Assumptions:** G-A; fixed clean prevalence `pi`; arbitrary global whole-row contamination; known one-bin follow-up `g`.
- **Current status:** proved locally as an elementary derivation from Huber overlap.
- **Result:** `min(1,epsilon/[(1-epsilon)pi g])`.
- **Literature threat:** likely a direct composition of general Huber geometry and an observation-channel contraction.
- **Scientific significance:** exposes an exact population failure regime, but by itself may only formalize “less observable group mass means less information.”
- **Difficulty:** low.
- **Survives removing OT/generation:** yes.

## T2 — Exact trusted-label recoverability frontier

- **Assumptions:** G-A with one-bin event probability.
- **Current status:** proved locally; frontier `epsilon=pi*g/(1+pi*g)`.
- **Literature threat:** same as T1; phase-transition algebra may be known or immediate.
- **Scientific significance:** potentially useful as an audit/reporting threshold.
- **Difficulty:** low.
- **Survives removing OT/generation:** yes.

## T3 — Label-contaminated subgroup identification

- **Assumptions:** G-B1 whole-row replacement or G-B2 declared label channel; clean subgroup target explicitly defined.
- **Current status:** prevalence interval derived for G-B1; conditional survival formula open.
- **Literature threat:** latent subgroup misclassification and sensitivity-analysis literature; general mixture proportion identification.
- **Scientific significance:** could be meaningful if a sharp additional threshold or nonmultiplicative interaction appears.
- **Difficulty:** medium/high.
- **Survives removing OT/generation:** yes.

## T4 — Global versus groupwise audit information

- **Assumptions:** compare G-A, G-C, and G-D with the same one-bin survival target.
- **Current status:** local formulas derived; no theorem-level literature comparison completed.
- **Literature threat:** robust subgroup/minimax risk and groupwise contamination work may contain analogues.
- **Scientific significance:** translates data-quality audits into exact recoverability changes; stronger than T1 if the comparison changes decisions.
- **Difficulty:** medium.
- **Survives removing OT/generation:** yes.

## T5 — Multi-group adversarial allocation

- **Assumptions:** trusted labels, fixed prevalences, one global Huber budget, multiple groups.
- **Current status:** one-bin resource LP and smallest-effective-mass ordering derived.
- **Literature threat:** general robust subgroup risk and group distributionally robust optimization.
- **Scientific significance:** may yield a usable allocation/abstention rule, but the ordering is elementary in the binary event model.
- **Difficulty:** medium.
- **Survives removing OT/generation:** yes.

## T6 — Multi-bin survival-functional generalization

- **Assumptions:** subgroup-specific discrete censoring operators; finite event grid; exact Huber compatibility.
- **Current status:** LP formulation available; no scalar closed form claimed.
- **Literature threat:** censored-data partial identification and robust inverse-problem theory.
- **Scientific significance:** strongest survival-specific route if it reveals a horizon-dependent operator modulus not reducible to `pi*g`.
- **Difficulty:** medium/high.
- **Survives removing OT/generation:** yes.

## Ranking and gate assessment

- **Best foundational lemma:** T1/T2, but likely not sufficient as a paper center.
- **Best practical theorem candidate:** T4, if audit information produces a sharp and decision-relevant comparison.
- **Best mathematically difficult candidate:** T3 or T6.
- **Strongest candidate after removing OT and generation:** T4 + T6 as a combined survival/audit theory, subject to novelty verification.

The current evidence supports continuation only as a conditional theory program. Step 04 should not begin until one candidate is selected and its closest general theorem sources are checked.
