# Final Research Postmortem

**Repository state:** `RESEARCH_LINE_ARCHIVED`
**Closeout scope:** Steps 01–08
**Starting closeout HEAD:** `3311ea6d4df28a7955b202c0834fcfbc5a5641e4`

## Original hypothesis

The project began with CORT-Surv / *Survival under Ambiguity*: derive sharp uncertainty sets for event-time quantities when survival records are censored and labels or recorded outcomes may be contaminated, then study robust synthetic worlds and trustworthy evaluation. The intended contribution combined partial identification, censoring, contamination, and distributional robustness.

The central scientific discipline was to distinguish latent event time, censoring time, observed follow-up, and recorded labels, and to reject a direction when its theorem was generic, already known, insufficient for a paper, or not survival-specific.

## Research pivots

1. **Robust OT plus censoring:** tested robust synthetic-survival generation and Huber-style ambiguity. Closed after the core became a combination of existing robust/OT and censoring machinery without a sufficiently distinctive contribution.
2. **Rare-group fragility:** derived the effect of contamination and trusted-label information in rare subgroups. The formula was valid, but the phenomenon was a direct consequence of contamination geometry and prevalence, not a sufficient survival-specific paper core.
3. **Audit-information theory:** studied how audit regimes change finite-grid identification. Exact LP machinery was useful, but the primary insight was a generic convex partial-identification result.
4. **RMST/joint functional theory:** investigated whether joint survival constraints create a useful RMST-width gap. The apparent gap was caused by comparing weighted RMST width with an unweighted pointwise-width sum. After correction, no meaningful gap remained.
5. **Adversarial auditing:** proved that unrestricted arbitrary corruption leaves positive worst-case ambiguity whenever at least one record remains unaudited, and that universal zero width requires auditing every record. The result was valid but became an impossibility/minimal-assumption statement rather than a sufficient survival method.
6. **Exchangeable audit transfer:** froze exchangeable corruption locations within trusted strata. Hypergeometric certification was exact, but the survival result reduced to standard finite-population acceptance sampling followed by censoring rescaling.
7. **Censoring-intervention falsification:** formalized additional re-censoring and paired intervention infrastructure. Composition was exact, but the invariance principle was elementary, prior art occupied the primary formulation, and the pilot lacked a valid-learner theorem, information-equivalent matching, and calibration.

## What survived

These results are retained as valid technical assets, not as automatically novel claims:

- the one-bin Huber/censoring diameter;
- the trusted-label rare-subgroup diameter formula;
- exact finite-grid survival operators and LP bounds;
- the adversarial finite-population audit impossibility result;
- the sharp post-audit interval under a residual corruption budget;
- exact hypergeometric finite-population certification;
- the distinction between latent event time `T`, censoring time `C`, observed `Y=min(T,C)`, and event indicator `Delta`;
- the exact re-censoring composition identity;
- deterministic finite-discrete observation and re-censoring operators;
- small Kaplan–Meier, Cox-style, and negative-control learners;
- exhaustive reference checks, audit enumeration, and regression tests;
- literature/source ledgers and gate-based pivot records.

None of these is called novel merely because it survived implementation or checking.

## What failed and why

| Branch | Failure reason | Ending commit/report |
|---|---|---|
| Robust OT + censoring | Composition novelty and insufficiently distinctive survival contribution | `9440396c`; Step 02 report |
| Rare-group fragility | Valid prevalence/contamination consequence, but insufficient standalone novelty and survival specificity | `14a2fdd`; Step 03 report |
| Audit-information theory | Generic convex/LP identification framework; insufficient load-bearing survival novelty | `5ceaa3f`; Step 04 report |
| RMST/joint geometry | Corrected interpretation removed the claimed coupling gap; novelty and sufficiency failed | `9999415`; Step 05 report |
| Adversarial auditing | Impossibility was valid, but limited audits were insufficient without transfer assumptions | `a659fc7`; Step 06 report |
| Exchangeable audit transfer | Reduced to hypergeometric acceptance sampling plus censoring rescaling; transfer, specificity, novelty, and sufficiency failed | `ecff179`; Step 07 report |
| Re-censoring falsification | Exact principle was coherent, but prior art occupied it and the pilot did not establish a calibrated falsification method | `3311ea6`; Step 08 report |

## Corrected mistakes

The Step 04/05 RMST interpretation error must remain visible. An early comparison treated an RMST width as though it could be compared with an unweighted sum of pointwise survival widths. RMST is a weighted integral over time, so the comparison was invalid. Step 05 corrected the calculation and interpretation using the proper time weights and endpoint constraints. The apparent gap disappeared, and the joint-theory branch was closed. This correction invalidated the attractive intermediate narrative rather than being hidden as an implementation detail.

Other recorded repairs included LP indexing/flattening, explicit audit-subset enumeration, direct-script import paths, citation-ledger reconstruction, and record-based rather than cutoff-based censor indicators.

## Reusable infrastructure

- `src/survival_ambiguity/identification/`: finite-grid operators, functionals, LP bounds, joint-survival utilities;
- `src/survival_ambiguity/audit/`: finite-population audit models, enumeration, hypergeometric bounds, allocation, survival certificates;
- `src/survival_ambiguity/censoring_interventions/`: observation operators, additional censoring, common-support masking, deterministic learners;
- `scripts/step07_reference_checks.py` and `scripts/step08_reference_checks.py`;
- tests for exactness, composition, coverage, learners, and adversarial cases;
- generated JSON reference artifacts under `results/step08/`;
- project charter, notation, claims/evidence policy, pivot history, closed-line register, theorem candidates, prior-art matrices, and gate reports;
- citation and source-verification workflow.

## Final verdict

> **The current project does not support a sufficiently novel and sufficient publication claim in its investigated forms.**

The repository is archived as a research history and reusable technical asset collection. No Step 09 implementation, Step 10 implementation, model training, large-data acquisition, or new repository is authorized by this closeout.
