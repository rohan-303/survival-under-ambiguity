# Censoring-intervention prior art

| Citation | Year | Problem | Prediction or inference? | Changes censoring mechanism? | Controlled intervention? | Same subjects paired? | Requires true T? | Prediction instability? | Metric instability? | Estimand instability? | Shortcut detection? | Distribution shift? | Formal theorem? | Diagnostic? | Benchmark? | Exact overlap | Remaining distinction |
|---|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Krishnamoorthy et al., *Survival Analysis with Limited Overlap and Censoring Distribution Shift* | 2026 | Censoring-distribution shift and limited overlap | Prediction/inference | Yes, as target setting | Not primarily an analyst re-censoring diagnostic | Not the stated core | Uses observed TTE/TTC structure; not a universal gold-T oracle | Not primary | No | Yes | No | Yes | Method-specific theory | No | Simulation/real-data evaluation | Threatens claims about censoring-shift sensitivity | Does not establish the proposed falsification null for arbitrary learners [1] |
| Xu et al., *Pitfalls of Administrative Censoring...* | 2026 | Administrative-cutoff leakage with time-indexed inputs | Prediction | Administrative mechanism | Diagnostic simulations and design principle | Cohort/time comparisons | No extra gold labels | Yes, leakage behavior | Yes | Yes | Yes, calendar shortcut | Yes | Failure-mode characterization | Yes | Simulation/real cohort | Directly covers calendar-like shortcut detection | Does not obviously cover arbitrary equal-rate paired mechanisms [2] |
| Lillelund, Qi & Greiner, *Overcoming Dependent Censoring...* | 2026 | Evaluation under dependent censoring | Inference/evaluation | Semi-synthetic dependent censoring | Yes, semi-synthetic framework | Preserves covariate structure and known event times | Yes in their semi-synthetic construction | No, metric target | Yes | No | No | Yes | Consistency/asymptotic results for metric | Evaluation method | Multi-dataset benchmark | Threatens claims that re-censoring diagnostic is needed to separate metric bias | Focus is metric estimation, not prediction instability [3] |
| Kvamme & Borgan, *The Brier Score under Administrative Censoring* | 2023 | IPCW Brier problems under administrative censoring | Evaluation | Administrative censoring | Analytical administrative setting | Not a paired intervention benchmark | No additional T | No | Yes | Yes | Indirectly calendar/covariate dependence | Yes | Metric result | Yes | No | Covers B, not A | Leaves prediction-level stability separate [4] |
| Liang et al., *SurvFM...* | 2026 | Censoring-aware RMST target construction | Prediction/benchmark | Yes, paired interventions from shared latent settings | Yes | Yes; shared covariates, event times, splits and seeds | Simulation uses known latent RMST/event times | Not framed as falsification, but compares performance across censoring interventions | Yes | Target-construction stability | Matched covariate-dependent censoring diagnostic | Yes | Method/diagnostic analyses | Yes | 24-setting simulation and 55 datasets | Strongest direct threat: paired censoring interventions and matched mechanisms already exist [5] | Proposed residual: a prediction-level null/falsification functional with explicit common-support and information-loss controls; not established distinct |
| Pfisterer et al., *Evaluating Domain Generalization for Survival Analysis* | 2022 | Survival prediction across clinical domains | Prediction | Domain/censoring heterogeneity may be present | No fixed re-censoring core | Cross-domain comparisons | No additional gold T | Generalization performance, not invariance test | Yes | Yes | No | Yes | Empirical | Benchmark | Yes | Threatens novelty of generic robustness framing | Does not target intervention-level mechanism isolation [6] |
| Conformalized Survival Analysis (primary page access blocked after search) | 2023 | Valid prediction bounds under censoring | Prediction/inference | No intervention core | No | No | No | Coverage under distribution assumptions | Evaluation | Target validity | No | Shift robustness as assumption issue | Formal coverage | Method | No | Reviewed as adjacent prediction-validity work; not used as a novelty claim |

## Top five novelty threats

1. **SurvFM** directly uses paired censoring interventions with shared latent event times and matched covariate-dependent mechanisms.[5]
2. **Xu et al.** already formalize administrative-cutoff leakage and practical detection of censoring-related shortcuts.[2]
3. **Lillelund et al.** provide a semi-synthetic dependent-censoring framework retaining covariate structure and known event times.[3]
4. **Krishnamoorthy et al.** make censoring-distribution shift and limited overlap an explicit survival prediction problem.[1]
5. **Kvamme–Borgan and domain-generalization work** cover metric and cross-domain instability that could otherwise be mistaken for a new stress-test contribution.[4][6]

The search establishes a direct overlap threat, not universal absence of a possible refinement. No claim of firstness is made.

## Sources

[1] https://www.nber.org/papers/w35643
[2] https://arxiv.org/abs/2607.10466
[3] https://arxiv.org/abs/2502.19460
[4] https://jmlr.org/papers/v24/19-1030.html
[5] https://arxiv.org/html/2607.09577v2
[6] https://proceedings.mlr.press/v174/pfisterer22a.html
