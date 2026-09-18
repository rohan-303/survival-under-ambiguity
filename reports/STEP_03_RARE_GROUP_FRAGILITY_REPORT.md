# Step 03 Rare-Group Fragility Report

## 1. Final status

**COMPLETE_WITH_WARNINGS**

The rare-group contamination models, G-A derivation, recoverability frontier, G-C/G-D comparisons, G-B formalization, finite multi-group and multi-bin checks, targeted literature kill test, theorem-candidate ladder, and M2 direction decision were completed. Warnings: G-B does not have one universal closed form because its estimand and label channel matter; multi-bin results remain LP formulations rather than a scalar theorem; and the literature search remains targeted rather than exhaustive.

## 2. Starting HEAD

- Repository: `C:/Users/rohan/survival-under-ambiguity`
- Starting HEAD: `9440396cdabd1254a7564a221ef26eccd9263af7`
- Branch: `main`
- Remote: `https://github.com/rohan-303/survival-under-ambiguity.git`
- Starting worktree: clean; tracking `origin/main`
- `git pull --ff-only`: passed; already up to date.

## 3. Scope frozen for Step 03

Primary theory: rare-subgroup recoverability under right censoring, global contamination, subgroup prevalence, subgroup-specific follow-up, and label assumptions.

Secondary theory: finite multi-bin survival-function and RMST generalization.

Out of scope: OT as primary identification geometry, neural generation, synthetic scenarios, real datasets, high-dimensional covariates, informative censoring, finite-sample confidence regions, and causal effects.

## 4. Model G-A definition

G-A uses a trusted subgroup label, fixed clean prevalence `pi`, arbitrary global whole-row Huber contamination of mass `epsilon`, and a contaminant that may allocate its mass across subgroups. The target is clean subgroup survival/event probability.

## 5. G-A sharp results

For a one-bin rare subgroup with follow-up `g_1`, changing only its conditional event probability changes the clean recorded-law TV distance by `pi*g_1*|p_1-p'_1|`. Exact Huber-neighborhood overlap therefore gives

`diam(p_1)=min(1,epsilon/[(1-epsilon)pi*g_1])`.

This is an **ELEMENTARY_DERIVATION**, not a novelty claim. The majority group has the same formula with its own effective mass `(1-pi)g_0`; rare-group asymmetry is quantitative only through effective observable mass.

## 6. Recoverability frontier

Complete population nonidentification occurs when

`epsilon >= pi*g_1/(1+pi*g_1)`.

Equivalent thresholds are:

- `pi <= epsilon/[(1-epsilon)g_1]` for fixed epsilon and follow-up;
- `g_1 <= epsilon/[(1-epsilon)pi]` for fixed epsilon and prevalence.

Away from saturation, the diameter increases with epsilon and decreases with both pi and g_1. At pi or g_1 equal to zero, the conditional estimand is undefined or uninformative and is not treated as a valid identified subgroup target.

## 7. Majority/minority comparison

The result is not simply “minorities are worse.” A majority group with sufficiently poor follow-up can have a smaller effective mass than a rare group with complete follow-up. The correct comparison is between `pi_g*g_g` values.

## 8. Model G-B definition and results

### G-B1: whole-row Huber replacement

The contaminant may choose both subgroup label and outcome. For observed prevalence `r`, the clean prevalence interval is

`max(0,(r-epsilon)/(1-epsilon)) <= pi <= min(1,r/(1-epsilon))`.

If observed prevalence is not fixed, clean prevalence has no nontrivial universal interval. A clean subgroup survival target requires a latent-membership estimand and additional restrictions. No universal conditional-survival formula was asserted.

### G-B2: label-only corruption

The clean outcome is retained while the label passes through a specified corruption channel. A known symmetric flip rate `eta<1/2` yields `pi=(r-eta)/(1-2eta)` before feasibility checks. Unknown or arbitrary label corruption produces partial identification. The subgroup survival formula remains **OPEN** until the channel and latent estimand are frozen.

## 9. Model G-C definition and results

G-C constrains contamination to preserve the subgroup marginal exactly. The rare group cannot receive a disproportionate share of global contamination. Its one-bin diameter is

`min(1,epsilon/[(1-epsilon)g_1])`,

without the `1/pi` amplification. This is a stronger, different assumption from G-A.

## 10. Model G-D definition and results

G-D imposes conditional rates `eta_g <= bar_epsilon_g` and global mass `sum_g pi_g eta_g <= epsilon`. The effective group rate is

`eta_g^max=min(bar_epsilon_g,epsilon/pi_g)`,

and the diameter is

`min(1,eta_g^max/[(1-eta_g^max)g_g])`.

This formally quantifies how group-specific audit information can restore subgroup identification relative to a global-only guarantee.

## 11. Multi-group findings

For trusted labels and fixed prevalences, changing group `j` by conditional amount `d_j` costs `pi_j*g_j*d_j` in observed TV for the one-bin model. The global pairwise budget is

`sum_j pi_j*g_j*d_j <= epsilon/(1-epsilon)`.

The worst single-group target is therefore concentrated on the smallest effective information mass. A weighted multi-group objective is a finite resource-allocation LP; no broader greedy theorem was claimed.

## 12. Multi-bin findings

The subgroup operator is block-structured with blocks `pi_g A_{q,g}`. Exact fixed-observed-law subgroup survival and RMST extrema remain LPs. The one-bin scalar substitution `g_g -> G_{C,g}(t)` is not a universal theorem; the full censoring operator and functional weights must be retained. Six deterministic multi-bin LP examples were generated.

## 13. Literature kill test

The targeted search found robust subgroup analysis for heterogeneous censored data, but its focus is subgroup estimation under censored AFT models rather than exact Huber contamination allocation.[10] Work on latent subgroup classification uncertainty demonstrates that uncertain memberships affect subgroup inference, but it is a causal sensitivity framework rather than this survival population-identification problem.[11]

Earlier targeted sources cover classical censoring bounds and robust OT.[1][2][3]
Survival DRO is a separate survival-specific threat.[4]
Other sources cover OT partial identification, generative ambiguity sets, and dependent-censoring bounds.[5][6][7]
Survival sensitivity and the unresolved DropCens package lineage remain additional threats or access gaps.[8][9]

These sources strengthen the literature threat but do not subsume the exact G-A/G-C/G-D comparison based on the sources inspected. The broader threat remains that G-A is an elementary consequence of general Huber geometry.

## 14. Theorem candidate ranking

1. **T4 — Global versus groupwise audit information:** strongest practical candidate.
2. **T6 — Multi-bin survival/RMST extension:** strongest survival-specific mathematical candidate.
3. **T3 — Label-contaminated subgroup identification:** potentially important but currently under-specified.
4. **T5 — Multi-group adversarial allocation:** useful one-bin resource LP, currently elementary.
5. **T1/T2 — Trusted-label diameter/frontier:** correct foundational lemmas but likely insufficient alone.

All candidates survive removal of OT and synthetic generation; none is labeled novel.

## 15. Rare-Group Theory Gate R

**CONDITIONAL.**

The G-A phenomenon is exact and the G-C/G-D comparisons produce a meaningful audit-information interpretation. However, the current core may still be a straightforward Huber rescaling, and G-B/multi-bin generalization remains unresolved.

## 16. Updated Novelty Gate N

**CONDITIONAL.**

The strongest plausible contribution is a sharp theorem comparing global, marginal-preserving, per-group-capped, and label-contaminated survival ambiguity. Existing robust subgroup, latent-label, censored subgroup, and general Huber theory remain substantial threats.

## 17. Updated Sufficiency Gate S

**CONDITIONAL.**

The audit-to-abstention interpretation could materially affect subgroup survival reporting, but the current one-bin result alone is not enough. A sufficient result needs a multi-bin functional consequence or a sharp decision-stability rule beyond “small groups have less information.”

## 18. OT policy

`OT_DEFERRED_FROM_PRIMARY_THEORY`. Step 02’s `OT_NOT_JUSTIFIED_YET` status is carried forward. No OT theory was implemented in Step 03.

## 19. M2 primary direction

**PATH R3 — GLOBAL-VS-GROUPWISE AUDIT INFORMATION BECOMES PRIMARY.**

T1/T2 remain lemmas. The primary future question is what contamination information—global, marginal-preserving, or group-specific—is sufficient to restore meaningful subgroup survival recoverability.

## 20. Files created/modified

- `scripts/step03_rare_group_preflight.py`
- `results/step03/rare_group_checks.json`
- `results/step03/phase_diagram.csv`
- `docs/RARE_GROUP_FRAGILITY_THEORY.md`
- `docs/M2_THEOREM_CANDIDATES.md`
- `docs/M2_SUFFICIENCY_ASSESSMENT.md`
- `docs/M2_DIRECTION_DECISION.md`
- `reports/STEP_03_RARE_GROUP_FRAGILITY_REPORT.md`

## 21. Tests and commands

- `git pull --ff-only` — passed; repository was current.
- `python scripts/step03_rare_group_preflight.py` — passed; generated 120 phase rows, 12 multi-group rows, and 6 multi-bin LP rows.
- `python -m pytest -q` — passed, 3 tests.
- `python -m compileall -q src scripts tests` — passed.
- `git diff --check` — passed before commit.
- Python: `3.11.15`.
- SciPy: `1.17.1`, reused for finite LP checks.
- No random seed or real dataset was used.

## 22. Numerical verification

The analytic G-A formula passed deterministic boundary and monotonicity checks over controlled epsilon, prevalence, and follow-up grids. The phase table contains 120 rows. G-C and G-D formulas were checked on controlled examples. Multi-group effective-mass ordering and multi-bin finite LP constructions completed without mismatch.

These are **[CHECKED]** computations, not proofs of the general literature claim or novelty.

## 23. Deviations

- Step 01 contract files remain at repository root; Step 03 artifacts follow the requested `docs/` and `results/step03/` locations.
- G-B was split into G-B1 whole-row replacement and G-B2 label-only corruption because they define different statistical problems.
- No universal G-B conditional-survival formula was invented.
- Literature coverage was targeted, and accessible sources were used where primary access permitted.

## 24. Known limitations

- G-A/G-C/G-D results are population-level one-bin derivations.
- G-B depends on a future explicit latent-membership and label-corruption contract.
- Multi-bin results are formulations and finite checks, not closed-form theorems.
- The literature search does not establish novelty.
- No finite-sample confidence region, estimated-censoring analysis, real-data validation, or decision certification was performed.

## 25. Recommended Step 04 only

Freeze the G-B label channel and the exact observed-data estimand, then compare T4/T6 against general Huber subgroup and censored-subgroup identification theory before attempting any finite-sample or synthetic-data implementation. **Not executed.**

## Sources

[1] https://www.pnas.org/doi/10.1073/pnas.73.1.11
[2] https://proceedings.mlr.press/v151/nietert22a.html
[3] https://proceedings.mlr.press/v139/mukherjee21a/mukherjee21a.pdf
[4] https://proceedings.mlr.press/v287/jin25a.html
[5] https://arxiv.org/abs/2506.00257
[6] https://proceedings.iclr.cc/paper_files/paper/2026/hash/9a0ec010802c72b238e41490fa03e4d2-Abstract-Conference.html
[7] https://arxiv.org/html/2503.11210
[8] https://hal.science/hal-05330588v1/file/2510.16560v1.pdf
[9] https://cran.r-project.org/web/packages/available_packages_by_name.html
[10] https://arxiv.org/html/2607.11389
[11] https://pmc.ncbi.nlm.nih.gov/articles/PMC9508766
