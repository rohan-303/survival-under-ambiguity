# Candidate 1 Prior Art

## Executive finding

The candidate's basic premise is already substantially covered. Mozumder et al. (2025) explicitly study external validation of cause-specific absolute risk, recommend assessing all-cause and each cause-specific absolute risk, simulate external baseline-hazard changes, and use cause-specific calibration plots, calibration-in-the-large, slopes, Brier score, and IPA.[1] This directly defeats the weak claim that aggregate validation can hide cause-specific error and that the remedy is merely to add cause-specific calibration.

van Geloven et al. provide a competing-risk validation guide covering prediction targets, pseudo-observations, calibration, and performance measures.[2] Austin et al. provide graphical calibration curves and the integrated calibration index for competing-risk models.[3] Temporal recalibration work addresses changing risk relationships over time, so a baseline-shift framing is not automatically new.[4]

## Mozumder 2025 kill test

The full text was retrieved through the Europe PMC PDF endpoint. Its abstract and methods state that the work:

- focuses on external validation using cause-specific hazards;
- assesses components specific to each cause-specific model and cause-specific absolute risks;
- simulates multiple external-validation scenarios;
- presents calibration plots, calibration slopes, calibration-in-the-large, Brier score, and index of prediction accuracy;
- concludes that a miscalibrated model for one cause can affect predicted absolute risks for each cause, including all-cause risk.[1]

The article does **not** appear to formulate the exact proposed `a_k=F_k/F_all` allocation vector, a sharp hidden-failure set, or a decision-regret supremum. But it already establishes the central external-validation diagnosis and explicitly recommends simultaneous all-cause/cause-specific assessment.[1]

## Prior-art matrix

| Threat | Exact overlap | Exact distinction still possible | Verdict |
|---|---|---|---|
| Mozumder et al. 2025 | External competing-risk calibration under baseline-hazard shift; all-cause and cause-specific absolute risks; Brier and calibration measures | A nontrivial decision-regret bound or temporal allocation-crossing theorem | Weak candidate unless stronger theorem survives |
| van Geloven et al. 2022 | Modern competing-risk validation guidance and appropriate measures | A new formal sufficiency theorem, if not already implied | Direct guidance overlap |
| Austin et al. 2022 | Cause-specific calibration curves and ICI | Decision consequences or transport-specific guarantees | Metric overlap |
| Temporal recalibration literature | External temporal change and recalibration | A site-level allocation trajectory with action reversal | Requires substantive distinction |
| Competing-risk decision analysis | Decision/net-benefit consequences under competing events | A bound connecting validation constraints to regret | Decision overlap |
| Neural Fine-Gray | Recent competing-risk modeling comparator | Evaluation-only, model-agnostic contribution | Baseline, not novelty |
| Robust survival/fairness work | Distributional robustness in survival | Cause-allocation decision guarantee | Strong adjacent threat |

## Proper-score and multiclass threats

At a fixed horizon, the outcome is one of cause 1, ..., cause K, or event-free. A vector probability score such as a competing-risk Brier score evaluates the joint vector and therefore penalizes misallocation even when the all-cause sum is unchanged. The candidate cannot claim that proper scoring is blind to cause allocation. The only possible gap would be that routine practice reports only aggregate or one-cause summaries, but “use the full vector proper score” is weak novelty unless the omission is shown to be widespread and decision-consequential.

The static multiclass analogy is a serious threat. A new simplex metric would not be sufficient. Any surviving theory must use time-varying CIF trajectories, censoring-aware estimation, or a decision guarantee that static multiclass calibration does not provide.

## Search conclusion

No source located in this gate establishes the exact proposed decision-regret supremum under compensating site shifts. However, the direct diagnosis is occupied, and the remaining distinction is only **POTENTIALLY_NOVEL / OPEN**, not a pass. Candidate 1 must not proceed to implementation without a dedicated theorem gate.

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
