# Negative-Results Asset Map

This map preserves valid negative results without implying that every result should become a paper.

| Question tested | Valid result | Proof/check status | Commit | Report | Reusable code | Plausible future use |
|---|---|---|---|---|---|---|
| Can robust OT plus censoring provide the primary contribution? | The construction is coherent, but the proposed combination did not establish distinct novelty or sufficiency. | Analytic preflight and gate review completed. | `9440396c` | Step 02 | finite-grid/robust utilities | Teaching artifact; background appendix |
| How does contamination width behave in a rare subgroup? | `diam(p_g)=min{1, epsilon/((1-epsilon) pi g_1)}` under the frozen trusted-label setup. | Derived and checked in reference scripts/tests. | `14a2fdd` | Step 03 | identification utilities | Technical note or lecture example |
| Does audit information produce a distinctive survival identification theory? | Exact LP bounds exist, but the core is generic convex partial identification. | Finite-grid exhaustive/reference checks. | `5ceaa3f` | Step 04 | `identification/` | Reusable benchmark utility; appendix |
| Does joint survival geometry create a strong RMST-width advantage? | No meaningful gap after correct RMST weighting; the original apparent gap was an interpretation error. | Corrected calculation and tests. | `9999415` | Step 05 | joint-survival utilities | Negative-methods case study |
| Can limited audits guarantee exact identification under arbitrary corruption? | No. With at least one arbitrary corruption and one unaudited row, worst-case ambiguity remains; zero width requires full audit. | Exhaustive finite-population enumeration and theorem reasoning. | `a659fc7` | Step 06 | audit models/enumerators | Technical note; impossibility teaching artifact |
| Can a residual post-audit interval be sharp? | Yes, under the stated finite-population oracle and residual budget. | Matched exhaustive enumeration. | `a659fc7` | Step 06 | audit interval code | Appendix or benchmark utility |
| Does exchangeable corruption location yield survival-specific transfer? | Hypergeometric certification is exact, but the survival extension is acceptance sampling plus censoring rescaling. | Coverage checks across tested finite cases. | `ecff179` | Step 07 | `audit/hypergeom_bounds.py` | Teaching/benchmark utility |
| Does re-censoring composition produce a new falsification theorem? | Composition is exact; common-support invariance is a consistency implication, not a converse or calibrated falsifier. | Operators, tests, and deterministic pilot. | `3311ea6` | Step 08 | `censoring_interventions/` | Evaluation control or appendix |
| Can equal-count paired interventions isolate censoring geometry? | In the pilot, both arms had 75 events and 165 censored records while geometry differed. | Reference script and JSON artifact verified. | `3311ea6` | Step 08 | paired intervention utilities | Benchmark control, not standalone method |

## Asset-selection guidance

- **Most defensible technical note:** adversarial audit impossibility plus the sharp residual-budget interval, if framed explicitly as a finite-population result and not as a complete survival method.
- **Most useful teaching artifact:** the RMST correction and the audit-oracle distinction between latent and recorded quantities.
- **Most reusable code:** finite-grid LP/reference checks and the record-level censoring operators.
- **Not recommended as a standalone publication:** the rare-group formula, hypergeometric rescaling, or re-censoring invariance alone.
- **Not computed:** no new external validation, real-data experiment, calibrated selective-prediction study, or model-training result was performed during closeout.
