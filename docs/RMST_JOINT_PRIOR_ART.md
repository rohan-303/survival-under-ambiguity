# RMST joint prior-art comparison

| Citation | Uncertainty source | Censoring model | Target | Pointwise survival bounds? | Direct RMST bounds? | Sharp? | Joint survival law required? | Joint attainability discussed? | Pointwise-vs-integrated gap? | Closed form? | Optimization? | Finite-sample inference? | Exact overlap with this project | Remaining difference |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lee, Park & Lee (2024), *Sensitivity analysis for unmeasured confounding in estimating the difference in RMST*, DOI [1] | Unmeasured confounding sensitivity | Survival outcomes; not the exact Huber recorded-law contract | RMST difference | Not established from accessible abstract/page | Yes, RMST difference is the target | Sensitivity-analysis sharpness is model-specific | Requires a coherent survival/data-generating law | No exact match found in accessible metadata | No exact pointwise-integration gap theorem identified | Not established | Yes/semiparametric sensitivity machinery | Yes/estimation focus | Same clinical RMST motivation, different hidden-confounding model | Our exact contamination-after-censoring polytope is different, but the direct-RMST precedent is a major threat to broad novelty |
| Baitairian et al. (2026), *Doubly valid and doubly sharp sensitivity analysis to unobserved confounding for survival outcomes*, arXiv metadata found via recent-statistics listing [2] | Unobserved confounding | Survival outcomes | Sharp survival/RMST sensitivity | Metadata indicates survival sensitivity; appendix could not be reliably retrieved in this environment | Exact RMST treatment not verified | Title claims doubly sharp, but theorem details remain access-blocked | Unknown from verified source text | Unresolved | Unresolved | Unresolved | Unresolved | Likely methodological inference focus | Potentially close in “sharp RMST under survival uncertainty” motivation | Strongest unresolved prior-art threat; do not claim novelty until the actual theorem/appendix is verified |
| Zhao et al. (2015), *On the Restricted Mean Survival Time Curve in Survival Analysis* [3] | Sampling uncertainty in RMST curve | Right-censored survival inference | RMST as a function of restriction time | Not partial-identification bounds | No contamination partial-identification interval | Sampling theory, not this population set | Curve dependence is studied statistically | Not our attainability question | No exact gap theorem | No | Estimation/inference | Yes | Same RMST-curve object | Our population identified-set geometry is distinct, but curve/joint-`tau` claims must not be presented as new generally |
| Zhong & Schaubel (2022), *Restricted Mean Survival Time as a Function of Restriction Time* [4] | Sampling/estimation | Censored survival data | RMST curve | No partial-identification rectangle | Estimation of RMST curve | Statistical inference | Joint curve covariance/estimation, not latent compatible-world geometry | Not our question | No exact gap theorem | No | Estimation | Yes | Same curve target | Threatens broad RMST-curve framing, not exact Huber compatibility |
| Manski/Rosen-style partial-identification support-function literature [5] | Partial identification | Generic | Linear functionals of convex identified sets | Generic set projections | Generic support-function bounds | Generic sharpness | Yes, convex identified set | Generic exposed-face conditions | Generic coordinate-envelope inequality | Often | Optimization/duality | Sometimes | Directly supports the support-function and rectangle inequalities | Those representations cannot be claimed as novel; any contribution must be survival/censoring-specific |
| Prior Step 04 robust censored-survival and partial-identification sources [6–8] | Censoring, robustness, misclassification | Censored survival or contaminated data | Survival distributions / robust inference | Varies | Varies | Varies | Varies | Varies | No exact verified match | Varies | Varies | Varies | Establishes broad overlap threats | Remaining difference is only the exact contract, operator, and theorem if one survives |

## Access and evidence notes

[1] https://journals.sagepub.com/doi/abs/10.1177/09622802241280782

[2] The title and authors were returned by the arXiv recent-statistics listing, but the discovered identifier did not resolve to that title through the available extractor. The paper is therefore recorded as an unresolved threat, not as a verified theorem source.

[3] https://pubmed.ncbi.nlm.nih.gov/26302239/ and https://pmc.ncbi.nlm.nih.gov/articles/PMC5114026/

[4] https://pubmed.ncbi.nlm.nih.gov/33616953/ and https://pmc.ncbi.nlm.nih.gov/articles/PMC8184877/

[5] Kaido, Molinari and Stoye, *A Dual Approach to Inference for Partially Identified Econometric Models*: https://www.bu.edu/econ/files/2014/05/Kaido-A-dual-approach-Feb-2012.pdf

[6] Peterson et al. classical censoring bounds: https://www.pnas.org/doi/10.1073/pnas.73.1.11

[7] Robust inference with censored survival data: https://onlinelibrary.wiley.com/doi/full/10.1111/sjos.12570

[8] Partial identification with misclassified data: https://www.sciencedirect.com/science/article/abs/pii/S0304407607002564

No source was used to claim exact theorem overlap without verified text. The prior-art result is therefore conservative: the project cannot claim novelty, and the Baitairian comparison remains explicitly unresolved rather than guessed.
