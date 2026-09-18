# Project Discovery V2 Decision

## Final status

**`NO_PROJECT_SELECTED`**

## Additional delegated sweep

A later independent sweep added 14 unverified frontier/question directions. They broaden the inventory but were not independently literature-audited and do not alter the decision. Selecting a winner would still be premature.

## Winner status

No candidate met the required combined bar of demonstrated novelty, clear load-bearing contribution, feasible evidence path, and paper sufficiency. This is a discovery outcome, not a failure to generate ideas.

## Runner-up 1

Disagreement-aware LLM judge triage. It has the clearest operational decision and low compute, but LLM-as-a-judge reliability is crowded and the exact human-review gain was not verified.[3]

## Runner-up 2

Unlearning verification beyond behavioral suppression. It is important and falsifiable, but direct prior art in unlearning verification and audit-to-forget makes novelty risk very high.[10][11][12]

## Strongest rejected near-miss

Citation faithfulness under source conflict. It has a clear metric gap, but attribution, citation generation, and RAG evaluation already occupy much of the space.[4][5][16][17]

## Why no candidate survived

The search produced 22 concrete questions across the supplied frontier families and ten additional frontiers. Every top candidate had a decisive unresolved prior-art or evidence threat. None could honestly be promoted to a new project without a dedicated Step 00, and the specification asks for one project that is already sufficiently selected for a paper lifecycle.

## Strongest novelty threats

The recurring threats were: InjecAgent and agent-evaluation work for tool security[1][14]; SOTA judge reliability for evaluation triage[3]; unlearning verification and audit-to-forget[10][11][12]; attribution/faithfulness work for RAG[4][5][16][17]; contamination studies for benchmark integrity[6]; and long-context reliability work for context cliffs.[9]

## Exact load-bearing contribution

None established. The candidates had plausible contribution forms—evaluation policy, verification protocol, benchmark, or diagnostic—but no contribution survived the bounded novelty audit with enough evidence to authorize implementation.

## Expected stacks for near-misses

- Judge triage: open instruction-tuned LLMs, preference benchmarks, a small human-labeled holdout, CPU/single-GPU inference.
- Unlearning verification: open 1–7B model, canary/natural facts, sequential edit sets, one or two GPUs.
- Citation conflict: open RAG pipeline, public dated QA/corpus data, one GPU; no large-scale training.

## Next gate

Do not begin Step 00 automatically. Start a future discovery cycle from a new frontier search, or authorize one explicitly chosen candidate for a separate gate.

## Implementation status

Implementation has **NOT** begun. No new repository, dependencies, datasets, model weights, training runs, or paid API campaign were created.
