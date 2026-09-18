# Step 00 Candidate 1 Decision

## Status

`CANDIDATE1_CLOSED_WITH_FAIL`

## Gate results

| Gate | Result | Reason |
|---|---|---|
| Theorem Gate | `CONDITIONAL` | Only the stronger decision-regret/validation-sufficiency question remains open; elementary cancellation and reversal are insufficient. |
| Evaluation-Gap Gate | `FAIL` | Mozumder 2025 and competing-risk validation guidance already directly diagnose cause-specific and all-cause miscalibration. |
| Decision-Relevance Gate | `CONDITIONAL` | Oncology competing mortality provides a credible context, but no frozen real action rule was verified. |
| Data Gate | `FAIL` | No compatible, verified multi-site dataset pair was established. MIMIC-IV is single-system; SEER site/endpoint compatibility remains unaudited. |
| Novelty Gate N-C1 | `FAIL` | The proposed primary claim is occupied by existing cause-specific competing-risk validation. The stronger regret theorem is only an open possibility. |
| Sufficiency Gate S-C1 | `CONDITIONAL` | Cause allocation can affect actions, but a demonstrated practice-changing result was not established. |

## Master decision

**`C1-F — FAIL FOR MULTIPLE REASONS`**

This is not `C1-A`. Do not create a new research repository, implementation package, benchmark, or model run from Candidate 1.

## Strongest elementary result

At a fixed horizon, predicted cause risks `(0.30,0.20)` and true cause risks `(0.05,0.45)` have identical all-cause risk `0.50` but different cause allocation. An abstract cause-weighted action can reverse under these two vectors. This proves only that aggregate risk is insufficient for cause-weighted decisions; it is elementary probability and decision theory.

## Strongest non-elementary candidate

A possible future theorem would bound cause-specific decision regret or allocation-trajectory error under explicit all-cause, cause-specific, and joint-score tolerances under transport. It was not derived, and its novelty against existing competing-risk validation remains unresolved. It is therefore `OPEN`, not a surviving contribution.

## Direct answers to the kill questions

- **Does Mozumder 2025 subsume the idea?** It subsumes the central external-validation diagnosis and the recommendation to assess each cause-specific absolute risk alongside all-cause risk. It does not visibly contain the exact proposed decision-regret supremum, but that residual gap is not enough to pass.
- **Does standard cause-specific calibration detect the failure?** Yes, the elementary constructed failure is directly exposed by cause-specific calibration or a joint proper competing-risk score.
- **Do proper scores detect it?** Yes, a joint vector score responds to cause misallocation even when the all-cause sum is fixed.
- **Does decision regret survive?** Abstractly yes under fixed total risk, but the reversal is elementary and no real transported decision result was established.
- **Strongest verified real decision use case:** competing cancer versus cardiovascular/other-cause mortality in cardiotoxic cancer treatment contexts.[1]
- **Best dataset pair:** None verified. SEER is potentially useful but site/field compatibility was not audited; MIMIC-IV is single-system and cannot provide site shift alone.
- **Endpoint compatibility:** SEER partitions `UNKNOWN`; MIMIC-IV temporal split `INCOMPATIBLE` for a site claim; SEER+MIMIC `INCOMPATIBLE` for a matched external-validation task.
- **Strongest novelty threat:** Mozumder et al. 2025 plus van Geloven et al. 2022 and Austin et al. 2022 already occupy the required cause-specific external-validation layer.[1][2][3]

## Archive rule

Candidate 1 is recorded as a failed independent gate. This does not reopen or modify Steps 01–08. The archived repository remains `RESEARCH_LINE_ARCHIVED`.

Sources consulted: [1][2][3]. Additional sources: [4][5][6]. Dataset sources: [7][8]. Comparator sources: [9][10].

## Sources

[1] https://europepmc.org/api/getPdf?pmcid=PMC12519608 — Mozumder et al. 2025 full text
[2] https://www.bmj.com/content/377/bmj-2021-069249 — van Geloven et al. 2022
[3] https://link.springer.com/article/10.1186/s41512-021-00114-6 — Austin et al. 2022 calibration curves
[4] https://pmc.ncbi.nlm.nih.gov/articles/PMC10946485 — Temporal recalibration
[5] https://pmc.ncbi.nlm.nih.gov/articles/PMC11521377 — Competing-risk decision analysis
[6] https://seer.cancer.gov/data — SEER data
[7] https://seer.cancer.gov/data/access.html — SEER access
[8] https://physionet.org/content/mimiciv/3.1 — MIMIC-IV
[9] https://proceedings.mlr.press/v209/jeanselme23a/jeanselme23a.pdf — Neural Fine-Gray
[10] https://proceedings.mlr.press/v193/hu22a.html — Distributionally robust survival
