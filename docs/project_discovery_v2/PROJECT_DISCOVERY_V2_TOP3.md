# Project Discovery V2 — Top 3 Contracts

## 1. Disagreement-aware LLM judge triage

- **Question:** At a fixed human-review budget, does judge disagreement select genuinely ambiguous or incorrectly scored items better than majority vote and confidence?
- **Hypothesis:** disagreement is useful only after controlling for judge identity, prompt, and rubric effects.
- **Contribution:** an evaluation policy, not another judge.
- **Closest work:** LLM-as-a-judge methods and reliability studies.[3]
- **Experiment:** open judges, fixed preference benchmark, human-labeled holdout, budget curves, subgroup/error analysis.
- **Baselines:** majority vote, single judge, self-consistency, confidence, random review.
- **Risk:** high novelty; low compute; data/annotation medium; publication sufficiency medium-high.
- **Kill:** disagreement does not improve review utility at fixed budget.
- **Negative survival:** a calibrated null result can show disagreement is not a reliable ambiguity signal.

## 2. Unlearning verification beyond behavioral suppression

- **Question:** Can black-box tests distinguish true deletion from behavioral suppression across sequential edits without retraining the full model?
- **Hypothesis:** existing utility/locality metrics can pass while memorized evidence remains extractable.
- **Contribution:** verification protocol with explicit threat model.
- **Closest work:** unlearning methods, federated verification, audit-to-forget.[10][11][12]
- **Experiment:** open small model, canary and natural facts, sequential deletion sets, extraction/utility/locality/privacy matrix.
- **Baselines:** retraining oracle where feasible, standard unlearning, fine-tuning suppression, random deletion.
- **Risk:** novelty very high; implementation medium; compute medium; data low; sufficiency medium.
- **Kill:** existing audits already separate the mechanisms under the same threat model.
- **Negative survival:** exposes non-identifiability of black-box unlearning claims.

## 3. Citation faithfulness under source conflict

- **Question:** Does a contradiction-aware evidence graph identify unsupported citations that answer-level correctness and attribution scores miss?
- **Hypothesis:** source conflict creates structurally unsupported claims even when the final answer is plausible.
- **Contribution:** diagnostic/evaluation principle.
- **Closest work:** attribution, correctness-faithfulness distinction, RAG evaluation.[4][5][16][17]
- **Experiment:** public QA, dated/conflicting sources, open RAG, human edge-level labels.
- **Baselines:** citation precision/recall, answer correctness, RAGAs, attribution scores.
- **Risk:** novelty high; implementation medium; compute low-medium; data medium; sufficiency medium.
- **Kill:** graph adds no predictive value over answer-level attribution.
- **Negative survival:** a benchmark can document metric failure and source-conflict limits.
