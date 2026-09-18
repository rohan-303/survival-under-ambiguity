# Q10 SUDO Kill Test

SUDO explicitly targets clinical AI evaluation without ground-truth annotations and includes clinical notes. It uses pseudo-label discrepancy and source ground truth to identify unreliable predictions, rank models, and assess subgroup bias on unlabeled data.[1]

## Comparison

| Requirement | SUDO | Q10 proposal |
|---|---|---|
| Source labels | Yes | Yes |
| Unlabeled target text | Yes | Yes |
| Target performance proxy | Yes | Intended |
| Clinical-note applicability | Yes | Yes |
| Semantic-drift mechanism | Not required | Central |
| Temporal lead-time warning | Not established by the retrieved paper | Required |
| Task-specific failure prediction | Directly targeted | Required to beat SUDO |

## Decision

SUDO subsumes the generic label-free performance-monitoring objective. Q10 could survive only by proving that task-conditioned semantic information provides earlier or more reliable warning than SUDO, uncertainty, and simple output-shift baselines under a frozen temporal protocol. No such separation is established in Step 00.

**Gate result:** Q10 cannot claim novelty from label-free evaluation alone.
