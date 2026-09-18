# M4 theorem candidates

All candidates are provisional; none is labeled `NOVEL`.

| Candidate | Assumptions / proof status | Threat | Meaning | Status |
|---|---|---|---|---|
| J1 — Polytope/support-function representation | Exact Huber finite-grid compatibility; fully derived | Generic convex analysis and partial identification | Correct computational foundation | `ELEMENTARY_DERIVATION` |
| J2 — Common-optimizer equality criterion | Compact finite LP; derived from equality in a weighted sum | Generic convex optimization | Diagnoses when pointwise endpoints can be combined | `ELEMENTARY_DERIVATION` |
| J3 — Closed-form K=2 RMST coupling gap | No-censoring K=2 solved by capped-simplex allocation; general censored K=2 open | Generic LP and robust inverse-problem theory | Edge-case benchmark only | `CHECKED`, not paper-level |
| J4 — Sharp worst-case pointwise-overstatement theorem | No positive gap found in the structured grid; no theorem | The candidate may be false or vacuous under this operator | Would quantify reporting error if true | `OPEN`, currently weak |
| J5 — Censoring-dependent coupling theorem | No monotonicity or positive phase found | Could be absent under the finite Huber operator | Potential survival-specific result | `OPEN`, unsupported |
| J6 — Specialized triangular-operator algorithm | Operator examined; no correct algorithm beyond LP | Matrix structure may not support greedy elimination | Could improve transparency/complexity | `OPEN`, no evidence |
| J7 — RMST-curve joint identified set | Same linear map supports multiple tau; no new theorem | RMST curve literature and generic support functions | Joint compatible RMST worlds | `OPEN`, prior-art sensitive |
| J8 — Shared-contamination two-group RMST contrast | Not implemented | Audit/global contamination theory | Descriptive group contrast uncertainty | `OPEN`, secondary |

The strongest honest conclusion is that J1/J2 are generic, J3 is an edge-case verification, and J4–J7 have not produced a survival-specific theorem. All candidates survive removal of OT and synthetic generation, but that does not make them novel or sufficient.
