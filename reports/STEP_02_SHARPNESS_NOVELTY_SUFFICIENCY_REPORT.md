# Step 02 Sharpness, Novelty, and Sufficiency Report

## 1. Final status

**COMPLETE_WITH_WARNINGS**

The exact finite-model derivations, deterministic finite verification, targeted theorem-level literature preflight, preliminary gates, and M1 direction decision were completed. Warnings: the literature search was targeted rather than exhaustive; some requested primary sources were inaccessible or only partially accessible; the restricted-class pilot is grid-based rather than an exact restricted-class theorem; and Model G-B was not assigned a closed form.

## 2. Starting repository state

- Repository: `C:/Users/rohan/survival-under-ambiguity`
- Starting HEAD: `ffa05c18657541791e3a0389360e0a9eb1df9989`
- Branch: `main`
- Remote: `https://github.com/rohan-303/survival-under-ambiguity.git`
- Starting worktree: clean and tracking `origin/main`
- `git pull --ff-only`: passed; already up to date.
- Bootstrap commit verified in history.

## 3. Mathematical results

### Exact Huber compatibility — [DERIVED]

For `R=(1-epsilon)P+epsilon Q` on a finite alphabet, a candidate `P` is compatible iff `(1-epsilon)P_i <= R_i` for every cell, `P` is a probability law, and nonnegativity holds. The implied `Q` is nonnegative and automatically has mass one. This exact set is contained in `TV(P,R)<=epsilon` but is not generally equal to it.

### Pairwise neighborhood overlap — [DERIVED]

Equal-epsilon Huber neighborhoods of `P0` and `P1` intersect iff

`TV(P0,P1) <= epsilon/(1-epsilon)`

for `0 <= epsilon < 1`. This is a pairwise overlap statement, not a fixed-observed-law TV-ball characterization.

### One-bin censoring — [DERIVED; CHECKED]

Under `A_g(p)=(1-g,gp,g(1-p))`,
`TV(A_g(p),A_g(p'))=g|p-p'|` exactly.

### One-bin contaminated diameter — [DERIVED]

Under the stated population model, the sharp latent event-probability diameter is

`min{1, epsilon/[(1-epsilon)g]}`.

It is zero at `epsilon=0`, one when `g=0`, and saturates when `epsilon >= g/(1+g)`. This is population nonidentification, not a finite-sample confidence bound.

### Multi-bin formulation — [DERIVED; CHECKED]

A finite censoring matrix `A_q` was constructed with event rows, censoring rows, terminal tail, and event-before-censor tie convention. Exact fixed-`R` extrema for linear survival/RMST functionals are LPs under `(1-epsilon)A_q p <= R`, `p>=0`, `1^T p=1`.

### Rare subgroup — [DERIVED]

For Model G-A—trusted subgroup label, fixed clean prevalence `pi`, arbitrary global contamination allocation—the conditional rare-group diameter is

`min{1, epsilon/[(1-epsilon) pi g_1]}`.

Thus the charter intuition has the required `(1-epsilon)` correction under this model and saturates at one. If contamination must preserve the subgroup marginal, the `pi` amplification disappears. Model G-B, where labels may be contaminated, remains **OPEN** because the target estimand and misclassification restriction must be specified.

### Restricted class — [CHECKED, not proved]

A monotone discrete-hazard class was enumerated on a step-0.05 grid with 643 candidates. The pilot did not eliminate ambiguity: the maximum fixed-observed-law width for the selected survival functional was approximately 0.25 at epsilon 0.2. This is not an exact restricted-class result.

## 4. Huber geometry result

The exact mixture-compatible set is coordinatewise:
`(1-epsilon)P_i <= R_i`.
It implies `TV(P,R)<=epsilon`, but a TV ball is a relaxation. The pairwise equal-epsilon neighborhood-overlap threshold is instead `TV(P0,P1)<=epsilon/(1-epsilon)`. These three statements are distinct and are documented in `docs/SHARPNESS_PREFLIGHT.md`.

## 5. One-bin sharp result

The closed form was established under the fixed-time event, independent follow-up, three-category recorded-law construction, arbitrary contaminant, and `0 <= epsilon < 1` assumptions:

`diam(p)=min{1, epsilon/[(1-epsilon)g]}`.

## 6. Multi-bin findings

The finite-grid problem becomes an exact LP over a censoring channel. Fixed-observed-law widths depend on the functional and channel, while pairwise widths are not generally captured by the one-bin expression. The pilot showed nonzero survival and RMST ambiguity but did not establish a new phase transition.

## 7. Rare-subgroup findings

The `epsilon/(pi*g)` intuition was **derived with correction** to `epsilon/[(1-epsilon)pi*g]` for Model G-A. It is not universal: marginal-preserving contamination removes the prevalence amplification, and label-contaminated Model G-B requires a different estimand/model.

## 8. Restricted-class findings

The monotone-hazard pilot produced a nontrivial but not yet distinctive narrowing. It did not show a changed threshold or a theorem-level interaction. Sufficiency remains conditional.

## 9. TV-versus-OT findings

Preliminary verdict: **OT_NOT_JUSTIFIED_YET**.

Robust OT literature supplies geometry-aware robust discrepancies, but using them here imposes transport-cost assumptions beyond arbitrary Huber contamination. On binary support, Wasserstein and TV can coincide; on widely separated support, OT is tighter only because it penalizes long transport. OT should remain a secondary comparison, not the primary theory.

## 10. Literature results

The closest threats are:

1. Peterson-style sharp clean censoring/competing-risk bounds.[1]
2. Nietert et al. robust Wasserstein theory under Huber contamination.[2]
3. Mukherjee et al. outlier-robust OT.[3]
4. Jin et al. Wasserstein DRO for censored survival prediction.[4]
5. Lin et al. conditional OT partial identification.[5]
6. Wen and Yang generative ambiguity sets.[6]
7. Recent partially identified dependent-censoring regression and survival sensitivity work.[7][8]

The exact matrix and remaining differences are in `docs/THEOREM_LANDSCAPE.md`. The search did not establish that the proposed subgroup theorem is already published, but it also did not establish novelty.

## 11. Novelty Gate N

**CONDITIONAL.**

The most plausible remaining contribution is an exact subgroup-allocation theorem distinguishing trusted labels, fixed clean prevalence, label-contaminated observations, and marginal-preserving contamination. It may still be a straightforward corollary of general Huber geometry, so PASS is not justified.

## 12. Sufficiency Gate S

**CONDITIONAL.**

The rare-group saturation regime could affect subgroup reporting, but no analyst-facing decision-stability procedure or finite-sample certification has yet been demonstrated. The current unrestricted and restricted pilots are not sufficient for PASS.

## 13. M1 research path

**PATH B — CONTINUE BUT PIVOT THEORY.**

Secondary consequence: **PATH C — DROP OT FROM PRIMARY THEORY** unless a later valid survival-specific result justifies it.

## 14. Files created or modified

- `scripts/step02_sharpness_preflight.py`
- `results/step02/sharpness_checks.json`
- `docs/SHARPNESS_PREFLIGHT.md`
- `docs/THEOREM_LANDSCAPE.md`
- `docs/M1_GATE_DECISION.md`
- `reports/STEP_02_SHARPNESS_NOVELTY_SUFFICIENCY_REPORT.md`

No existing project outside this repository was modified. No large dataset, paper archive, model, credential, or cache was staged.

## 15. Commands/tests executed

- `git pull --ff-only` — passed; up to date.
- `python scripts/step02_sharpness_preflight.py` — passed; generated 6 one-bin checks, 6 multi-bin fixed-R rows, 3 pairwise LP rows, and a 643-candidate restricted grid.
- `python -m pytest -q` — passed, 1 test.
- `python -m compileall -q src scripts tests` — passed.
- `git diff --check` — passed.
- Python: `3.11.15`.
- SciPy: `1.17.1`, used for deterministic tiny LPs.
- No random seed was used.

## 16. Deviations from prompt

- Step 01 documents were at repository root rather than under `docs/`; they were read without silently relocating or overwriting them. Step 02 artifacts were placed under `docs/` as requested.
- Peterson’s primary paper was identified from the PNAS record, while a readable NBER discussion was used for contextual verification.
- OpenReview access for GAS-DRO was bot-gated; the official ICLR abstract was used instead.
- DropCens was located through CRAN package listings,[9] but its primary methodological paper was not verified; it is treated only as an unresolved threat.
- Model G-B and exact restricted-class optimization remain open rather than being guessed.

## 17. Known limitations

- Literature coverage is targeted, not exhaustive.
- The rare-group formula is model-specific and population-level.
- The restricted-class calculation is grid-based.
- The OT examples compare assumptions rather than prove an OT survival theorem.
- No finite-sample inference, estimated-censoring error analysis, or decision certification was implemented.

## 18. Recommended Step 03

Freeze a precise rare-subgroup contamination taxonomy and perform a theorem-level comparison against general Huber partial-identification results, then derive the exact Model G-B and marginal-preserving identified sets before any synthetic-data or neural-model work. **Not executed.**

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
