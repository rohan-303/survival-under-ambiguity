# Candidate 1 Baselines and Availability

## Classical baselines

- Cause-specific hazards models for each event cause;
- Fine–Gray subdistribution hazards model;
- Aalen–Johansen observed cumulative-incidence estimator;
- flexible parametric cause-specific models;
- competing-risk Brier/IPA and calibration curves.

These are established methodological families in the competing-risk validation guidance and Mozumder et al.[1][2]

## Recent comparator

Neural Fine-Gray is an available recent competing-risk modeling comparator, but it is a model baseline rather than a load-bearing novelty contribution.[9] Distributionally robust survival analysis is an adjacent robustness/fairness threat, not a substitute for external-validation theory.[10]

## Evaluation baselines

A future protocol would need, at minimum:

1. all-cause calibration and Brier;
2. per-cause CIF calibration-in-the-large, slope, and curves;
3. joint competing-risk Brier or proper score;
4. cause-specific discrimination;
5. decision-curve/net-benefit analysis where a real action threshold is defensible;
6. temporal and genuine site external-validation splits.

## Availability verdict

The classical baseline families are sufficiently established to be feasible without new model invention. The problem is not baseline absence; it is proving that a new evaluation/theorem adds something beyond the existing validation contract. Full installation, package versions, endpoint adapters, and execution were intentionally **NOT COMPUTED** in Step 00.

## Baseline Gate

`CONDITIONAL`: baseline families are available in principle, but exact implementation availability and endpoint compatibility must be verified only after a candidate survives the theorem and data gates.

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
