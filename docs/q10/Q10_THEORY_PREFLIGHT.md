# Q10 Theory Preflight

## 1. Frozen setting

A fixed clinical-NLP model `f` is trained on labeled source data `D0`. At time `t`, a target batch `Dt` contains clinical text but no target task labels. A monitor computes `St` and must warn about later degradation in one frozen metric, selected here as macro-F1 for a fixed text-classification task. The warning target is `1{F1(Dt) < F1(D0)-delta}` with a declared lead time before labels are available.

## 2. Drift taxonomy

- **Lexical drift:** token, abbreviation, spelling, or terminology frequencies change.
- **Semantic drift:** contextual meanings or representation neighborhoods change.
- **Task-relevant drift:** the shift changes the model's error rate or the conditional relation between text and label.

These are not interchangeable. A large semantic displacement can be harmless; a small change in a clinically decisive phrase can be damaging.

## 3. Identifiability boundary

Unlabeled target `P(X)` does not identify target performance when `P(Y|X)` is unrestricted. Two target worlds can share identical text distributions but assign different labels, producing different F1 for the same fixed model. This is the standard unsupervised-domain-adaptation boundary.[6]

**Classification: KNOWN/GENERIC.** Semantic drift is a function of the observed target covariate distribution, so it cannot remove this boundary without additional assumptions.

## 4. Semantic non-sufficiency

- **Case A:** embeddings and terminology move strongly because templates or synonyms change, while the clinically relevant label rule is stable. Performance remains acceptable.
- **Case B:** average embeddings remain stable while a rare clinical concept changes meaning or documentation convention. Performance can collapse on that concept.

**Classification: ELEMENTARY/KNOWN.** These counterexamples defeat “more semantic drift implies more failure.”

## 5. Task-conditioned drift

A plausible hypothesis is to project target movement onto source regions or concepts that contribute to the fixed task, then compare it with generic representation distance, prediction entropy, and SUDO. This is **POTENTIALLY NOVEL** only as a falsifiable empirical comparison; no theorem or evidence here establishes it.

## 6. Uncertainty interaction and silent failure

High drift/high uncertainty is not the only dangerous regime. High drift/low uncertainty could expose overconfident failure, while low apparent drift/high uncertainty may be benign ambiguity. Whether task-conditioned drift detects failures missed by confidence is **OPEN**, not demonstrated.

## 7. Candidate results

| Candidate | Classification | Reason |
|---|---|---|
| T1 unlabeled impossibility | KNOWN | Standard identifiability limitation. |
| T2 task-conditioned drift bound | OPEN / high threat | Domain-adaptation bounds already relate representation divergence to target risk under assumptions; a new bound must be genuinely tighter and clinical-text-specific.[6] |
| T3 silent-failure detector | OPEN | Requires prospective, label-held-out validation against uncertainty/SUDO. |
| B1 temporal early-warning benchmark | CONDITIONAL | Could be useful, but Clinical-ShiftEval is a direct benchmark threat.[2] |
| B2 controlled semantic perturbation benchmark | REFUTED as novelty candidate | Synthetic shift construction overlaps existing shift-explanation work. |

## Claim classification

Q10 has a coherent question but no established load-bearing contribution. The strongest honest statement is: task-conditioned semantic drift is a hypothesis for label-free warning under explicit assumptions, not a validated monitor.
