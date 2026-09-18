# M7 theorem and benchmark candidates

| Candidate | Claim | Evidence | Prior-art threat | Decision |
|---|---|---|---|---|
| C1 — falsification principle | Fisher-consistent learner must be invariant to valid additional independent censoring on common support | Composition identity and one-line target argument are correct | Tautological consistency implication; stability is not sufficient; prior work covers related sensitivity | `CONDITIONAL`, elementary |
| C2 — matched-mechanism stress test | Same-subject interventions matched on event/censor counts but differing in geometry isolate mechanism dependence | Tiny pilot found an equal-count pair with Cox discrepancy `0.022574` and naive discrepancy `0.045833` | SurvFM already uses paired censoring interventions and matched mechanisms | `CONDITIONAL`, not novel established |
| C3 — censoring-shortcut benchmark | Pure shortcut, true-risk, mixed, and calendar-like features expose nuisance dependence | Naive learner moved more than Cox in pilot; no calibrated benchmark | Xu et al. cover administrative leakage; SurvFM covers matched censoring simulations | `CONDITIONAL`, occupied threat |

## Gate interpretation

No candidate currently supports a specific novelty claim. The residual distinction—prediction-level invariance as a falsification functional with explicit common-support and information-loss controls—was not separated strongly enough from SurvFM's paired/matched intervention design.
