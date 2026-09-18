# Project Discovery V2 — Frontiers

## Scope and boundary

This is a fresh search after the previous clinical discovery cycle closed at `NO_SURVIVING_FRONTIER_RESET_CANDIDATE`. Previous candidates were not revived or mutated. No data, models, paid APIs, or dependencies were added.

## A–J supplied frontiers

1. LLM reliability and reasoning
2. AI-agent reliability and security
3. model editing and unlearning
4. alignment and safety
5. AI security
6. retrieval/RAG reliability
7. multimodal reliability
8. foundation-model evaluation
9. data quality and benchmark integrity
10. PQC/AI-security intersection

## Additional frontiers independently added

11. **Evaluator reliability:** when LLM judges disagree, can disagreement-aware aggregation identify cases requiring human review better than a single judge? Direct threat: LLM-as-a-judge work.[3]
12. **Training-data influence and provenance:** can influence estimates predict which data removals change a capability without retraining every deletion set? Direct threat: training-data influence survey.[15]
13. **Human delegation boundary:** can an intervention policy reduce harmful over-delegation to AI without reducing appropriate delegation? Direct threat: human-AI collaboration meta-analysis.[13]
14. **Continual/test-time adaptation safety:** when does unlabeled adaptation improve average accuracy while silently worsening rare but important slices? Requires an evaluation protocol, not another adaptation method.
15. **Interactive evaluation validity:** do model scores change materially when the evaluator can ask clarifying questions, and can static benchmarks measure that loss? Direct threat: agent-evaluation surveys.[14]
16. **Scientific reproducibility of AI evaluation:** can a compact perturbation protocol predict which reported LLM results fail across seeds, prompts, and implementations? Direct threat: benchmark-instability literature.
17. **Data-contract failure:** can provenance and transformation metadata predict downstream benchmark regressions better than aggregate data-quality scores? Direct threat: data valuation/influence work.[15]
18. **Capability boundary localization:** can minimal prompt or context edits locate abrupt capability cliffs more reliably than broad stress tests? Direct threat: long-context and robustness benchmarks.[9]
19. **Safety-evaluation measurement:** can refusal/capability trade-offs be decomposed into intent recognition, action execution, and refusal calibration rather than one safety score? Direct threat: jailbreak and alignment evaluation.[18]
20. **Evidence-graph robustness:** can contradiction-aware evidence graphs detect citation failures that answer-level faithfulness metrics miss? Direct threats: attribution and RAG evaluation.[4][5][16][17]

The additional frontiers are candidates for questions, not claims of novelty.
