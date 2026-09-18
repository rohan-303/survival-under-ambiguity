# Project Discovery V2 Report

## 1. Status

**`NO_PROJECT_SELECTED`**. This was a fresh project-selection round after the archived clinical cycle ended at `NO_SURVIVING_FRONTIER_RESET_CANDIDATE`. No previous candidate was revived. No implementation, model training, dataset download, or paid API campaign occurred.

## 2. Search scope and evidence boundary

The search covered LLM reliability, agents, model editing, alignment, AI security, RAG, multimodal reliability, foundation-model evaluation, benchmark integrity, and PQC/AI security, plus ten additional frontiers: evaluator reliability, training-data influence, human delegation, test-time adaptation safety, interactive evaluation, evaluation reproducibility, data contracts, capability cliffs, safety measurement, and evidence-graph robustness. Primary and official pages were prioritized where accessible; the record is a bounded discovery search, not a systematic review.

## 3. Additional frontiers

The ten additional frontiers are documented in `docs/project_discovery_v2/PROJECT_DISCOVERY_V2_FRONTIERS.md`. Their common requirement is a measurable change in an evaluation, security, data, or deployment decision—not an architecture-only improvement.

## 4. Candidate inventory

Twenty-two falsifiable questions were generated. The complete inventory is in `PROJECT_DISCOVERY_V2_ALL_CANDIDATES.md`. The candidates include reasoning consistency, confidence calibration, tool-intent/execution mismatch, memory-poison recovery, sequential editing interference, unlearning verification, safety calibration, semantic entropy, injection propagation, source conflict, citation faithfulness, retrieval freshness, multimodal modality over-trust, selective modality abstention, contamination-sensitive ranking, contamination-risk prediction, judge disagreement triage, provenance/regression prediction, human delegation, context cliffs, test-time adaptation rare-slice risk, and evidence-graph diagnostics.

## 5. Shortlist decisions

The first shortlist of ten is in `PROJECT_DISCOVERY_V2_TOP10.md`; the top five and their decisive tests are in `PROJECT_DISCOVERY_V2_TOP5.md`; complete contracts for the top three are in `PROJECT_DISCOVERY_V2_TOP3.md`.

## 6. Literature threats

Tool-integrated prompt injection is already benchmarked by InjecAgent.[1]

Memory poisoning has a direct 2026 benchmark threat.[2]

LLM-as-a-judge is an active evaluation literature with recent EMNLP work.[3]

Citation correctness and faithfulness are explicitly distinguished in current RAG work.[4]

Attribution methods and automated RAG evaluation are also available.[5][16][17]

Benchmark contamination has dedicated NAACL research.[6]

Confidence and calibration of LLMs are active topics.[7][8]

Long-context positional failure is established in Lost in the Middle.[9]

Unlearning verification and audit-to-forget have direct security literature.[10][11][12]

Human-AI delegation has a recent meta-analysis.[13]

Agent evaluation is a mature survey area.[14]

Training-data influence is also surveyed.[15]

These sources do not prove every candidate is closed. They show why each top candidate needs a sharper gate than the discovery round can honestly provide. Alignment and jailbreak evaluation also already occupy the safety-measurement space, adding another direct threat to refusal-calibration candidates.[18]

## 7. Top-three adversarial review

### Judge disagreement triage

**Reviewer 2 rejection:** disagreement may measure judge prompt noise or rubric ambiguity rather than item ambiguity, and a human-review gain may disappear under a stronger judge ensemble. The one decisive test is a fixed-budget human-labeled holdout comparing disagreement against majority vote, confidence, and random selection.[3]

### Unlearning verification

**Reviewer 2 rejection:** black-box extraction tests may be weak proxies for deletion, while retraining or access to internal states is required for a meaningful guarantee. The decisive test is a threat-model-specific comparison against retraining and existing verification methods across sequential deletions.[10][11][12]

### Citation faithfulness under source conflict

**Reviewer 2 rejection:** an evidence graph may be only a more elaborate attribution score, and source conflict may be resolved by answer-level correctness.

The decisive test is human edge-level annotation showing incremental predictive value over attribution and correctness.[4][5]

RAGAs and citation precision/recall remain required comparators.[16][17]

## 8. Risk classification

| Candidate | Novelty | Implementation | Compute | Data | Sufficiency |
|---|---|---|---|---|---|
| Judge disagreement triage | HIGH | LOW | LOW | MEDIUM | MEDIUM-HIGH |
| Unlearning verification | VERY_HIGH | MEDIUM | MEDIUM | LOW | MEDIUM |
| Citation conflict | HIGH | MEDIUM | LOW-MEDIUM | MEDIUM | MEDIUM |

The diversity requirement is met: evaluation policy, security verification, and benchmark/diagnostic work. None reaches the selection bar.

## 9. Winner decision

**No winner. `NO_PROJECT_SELECTED`.** Selecting one would convert unresolved novelty threats into an invented approval. The correct action is to preserve the shortlist and begin a new, explicitly authorized gate later rather than implement prematurely.

## 10. Required final fields

- **Project Discovery V2 status:** complete with no selection.
- **Winner status:** no project selected.
- **Selected winner:** none.
- **Runner-up 1:** disagreement-aware LLM judge triage.
- **Runner-up 2:** unlearning verification beyond suppression.
- **Strongest rejected near-miss:** citation faithfulness under source conflict.
- **Winner research question:** not applicable.
- **Winner load-bearing contribution:** not applicable.
- **Strongest novelty threat:** occupied evaluation/security literatures, especially judge reliability, unlearning verification, and citation attribution.
- **Why a candidate remains distinct:** not established to the required standard.
- **Datasets:** public preference/QA/RAG benchmarks and synthetic controlled traces are plausible for near-misses; none was selected or downloaded.
- **Models:** open instruction-tuned LLMs are plausible; no model was selected or run.
- **Compute:** near-misses are laptop/single-GPU feasible; this does not establish publication sufficiency.
- **Expected project type:** none selected; top three span evaluation policy, security verification, and diagnostic benchmark.
- **Expected paper shape:** not authorized; each near-miss could form an evaluation paper only after a dedicated gate.
- **Research risk:** all top three have high or very high novelty risk.
- **Next step:** stop; do not begin Step 00 automatically and do not create a project.

## 11. Implementation statement

Implementation has **NOT** begun.

## Sources

[1] https://doi.org/10.18653/v1/2024.findings-acl.624
[2] https://doi.org/10.5281/zenodo.21379140
[3] https://doi.org/10.18653/v1/2025.emnlp-main.138
[4] https://doi.org/10.1145/3731120.3744592
[5] https://doi.org/10.18653/v1/2024.emnlp-main.347
[6] https://doi.org/10.18653/v1/2024.naacl-long.482
[7] https://doi.org/10.1038/s42256-024-00976-7
[8] https://doi.org/10.18653/v1/2024.naacl-long.366
[9] https://doi.org/10.1162/tacl_a_00638
[10] https://doi.org/10.1109/tdsc.2024.3382321
[11] https://doi.org/10.14722/ndss.2024.24252
[12] https://doi.org/10.1609/aaai.v38i11.29092
[13] https://doi.org/10.1038/s41562-024-02024-1
[14] https://doi.org/10.1007/s11704-024-40231-1
[15] https://doi.org/10.1007/s10994-023-06495-7
[16] https://doi.org/10.18653/v1/2023.emnlp-main.398
[17] https://doi.org/10.18653/v1/2024.eacl-demo.16
[18] https://doi.org/10.48550/arxiv.2307.02483
