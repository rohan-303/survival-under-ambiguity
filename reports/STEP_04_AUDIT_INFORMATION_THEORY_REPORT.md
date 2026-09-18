# STEP 04 — AUDIT-INFORMATION THEORY REPORT

## 1. Final status

**COMPLETE_WITH_WARNINGS**

The finite-grid grouped survival model, audit regimes, exact-Huber LP reference solver, one-bin analytic/LP checks, RMST diagnostics, dual certificate form, literature kill test, counterexample findings, and M3 direction decision were completed. Warnings: the strongest audit-width gain is not established as a nontrivial fixed-observed-law theorem; A2/A3 can be contract-feasibility restrictions rather than width reductions; A4-bounded remains open; and no result is labeled novel.

## 2. Starting HEAD

- Repository: `C:/Users/rohan/survival-under-ambiguity`
- Starting HEAD: `14a2fdd7a3ee5ea4dc60fef5a12809bba8257127`
- Branch: `main`
- Remote: `https://github.com/rohan-303/survival-under-ambiguity.git`
- Starting worktree: clean; expected tracking `origin/main`
- Repository preflight: passed; `git pull --ff-only` passed before edits.

## 3. Scope

Population-level finite-grid theory only. No neural networks, synthetic generation, optimal transport primary theory, finite-sample inference, estimated censoring, dependent censoring, privacy, causal inference, or real-data experiments.

## 4. Finite-grid grouped survival model

For groups `g=1,...,J`, clean prevalence `pi_g`, conditional event masses `p_g`, and known subgroup censoring operators `A_g`, the clean recorded law is the block vector `(pi_g A_g p_g)_g`. Event cells use the tie convention `T <= C`; each operator is column-stochastic and includes a terminal tail state. The implementation validates probability conservation.

## 5. Audit regimes A0–A5

- A0: arbitrary joint contaminant and unknown clean subgroup marginal.
- A1: externally known clean `pi`, arbitrary contaminant.
- A2: clean and contaminant group marginals both equal `pi`.
- A3: conditional contaminant rate in group `g` is bounded by `bar_epsilon_g`.
- A4-known: known label confusion matrix before contamination.
- A4-bounded: bounded confusion entries; not implemented.
- A5: optional joint intersection; not used to force narrower intervals.

The exact definitions and distinctions appear in `docs/AUDIT_INFORMATION_THEORY.md`.

## 6. Information partial order

On a common data-contract domain, A2 is a restriction of A1. But A2 is infeasible when the observed group marginal differs from `pi`, while A1 may remain feasible. A4 changes the observation operator and is not generally comparable with outcome-contamination caps. Therefore the correct structure is a partial order with domain dependence, not a total hierarchy.

## 7. One-bin sharp results

The trusted-label/global-contamination result remains:

`diam = min(1, epsilon / ((1-epsilon) pi_g g_g))`.

Under marginal-preserving contamination, the `1/pi_g` amplification disappears:

`diam = min(1, epsilon / ((1-epsilon) g_g))`.

For a group cap, the local contract-level rate is `eta_g^max=min(bar_epsilon_g,epsilon/pi_g)` and the corresponding elementary diameter is `min(1,eta_g^max/((1-eta_g^max)g_g))`.

These formulas are local elementary derivations, not novelty claims.

## 8. Audit-restoration thresholds

The global-only complete-nonidentification threshold is `epsilon >= pi_g*g_g/(1+pi_g*g_g)`. A contract with conditional rate `eta_g` is partially informative when `eta_g < g_g/(1+g_g)`. Thus audit information can restore partial identification at the contract level. However, the fixed-`R`, fixed-`pi` LP analysis shows that group-cap rows may only test whether the observed contract is feasible; they do not automatically shrink the conditional interval. A nontrivial restoration theorem must optimize over the admissible observed-law class, not one fixed `R`.

## 9. Multi-bin survival results

For fixed clean prevalences, exact Huber feasibility and survival endpoints are finite LPs. A0 supports linear joint subgroup functionals; conditional A0 targets are ratios and were not misrepresented as LPs. A1–A3 use `J(K+1)` latent variables, `J` simplex equalities, and observation-cell Huber inequalities. A4-known uses the label-mixed linear operator.

Tiny diagnostics covered two groups, three event states plus a tail, pointwise survival at three horizons, and RMST. All returned optimal statuses with residual tolerance below the declared threshold.

## 10. RMST results

RMST is optimized directly with weights `min(t_j,tau)` and terminal weight `tau`. In the checked scenario, group 0 pointwise widths were `0.23148`, `0.29321`, and `0.29321`; direct RMST width was `0.61343`, versus `0.81790` for their sum. This demonstrates checked joint coupling in one scenario. It does not establish a general RMST theorem.

## 11. Joint-attainability findings

Pointwise extrema cannot be combined into a synthetic survival curve. The valid joint set is the image of one feasible latent-mass polytope and automatically enforces nonnegative event masses and survival monotonicity. Direct RMST optimization handles joint attainability correctly.

## 12. Primal optimization formulation

For A1–A3, minimize/maximize `w^T p_g` subject to `p_g>=0`, group simplex equalities, and `(1-epsilon)Bp <= R`, plus regime constraints. For A0, joint masses are linear for joint survival functionals but conditional survival is linear-fractional. For A4-known, replace `B` by the known label-channel operator.

## 13. Dual/certificate formulation

For the lower endpoint `min c^T x` subject to `Hx<=R`, `Ex=1`, `x>=0`, the dual certificate is:

`max R^T y + 1^T z` subject to `H^T y + E^T z <= c`, `y<=0`.

The upper endpoint uses `-c`. The solver records HiGHS inequality marginals and primal residuals. These are valid finite-instance certificates. A universal audit-prioritization theorem was not obtained: under the fixed-`R` A3 formulation, cap rows can be zero-coefficient feasibility rows rather than informative width constraints.

## 14. Audit-value result

The candidate fixed-data width value `W_A-W_B` is not sufficient by itself. A2/A3 can alter the admissible data-contract domain without changing the conditional LP width for a given feasible `R`. The meaningful unresolved quantity is contract value: worst-case width over all observed laws admissible under each audit regime. This remains open.

## 15. Operator-level theorem attempt

The appropriate object is the operator-specific modulus

`omega_{g,A}(v)=sup |v^T(p_g-p'_g)|`

over pairs of latent worlds with a common contaminated recorded law under regime A. The one-bin `pi_g g_g` term is a special case, not a universal multi-bin replacement. The modulus formulation is promising but remains `PROPOSED/OPEN`.

## 16. Label-error findings

A4-known is coherent when `M` and clean prevalence are fixed; it produces a linear observation operator and LP bounds. A4-bounded requires a frozen clean-membership estimand and a separate optimization over `M`. Existing partial-identification and error-prone survival subgroup literature are direct threats. No label-error novelty claim was made.

## 17. Literature kill test

Targeted sources cover classical censoring bounds, robust inference with censored survival data, partial identification with misclassified data, error-prone subgroup/biomarker survival analysis, robust subgroup analysis, and latent subgroup uncertainty. The strongest novelty threat is that the one-bin audit comparison is standard contamination allocation after a channel, while the finite-grid LP is a direct robust inverse-problem formulation. The literature review therefore leaves Gate N conditional, not passed.

## 18. Counterexamples

- A2 is not simply “more informative A1” on every observed law: it can be infeasible when the observed group marginal is not `pi`.
- A3 group caps need not reduce a fixed-`R` interval when the residual group contamination mass is already determined by `R` and `pi`.
- The pointwise survival optimizers need not be jointly attainable; direct RMST optimization is required.
- A majority group can remain more fragile than a rare group when its censoring support is sufficiently poor.

## 19. Audit Theory Gate A

**CONDITIONAL.** The framework has exact finite-grid LPs, meaningful contract distinctions, and a testable RMST/joint route. A theorem beyond elementary set inclusion and one-bin contamination algebra has not yet been established.

## 20. RMST Gate M

**CONDITIONAL.** Direct RMST optimization reveals checked joint coupling beyond a naive sum of pointwise widths, but a general sharp RMST theorem is unresolved.

## 21. Novelty Gate N

**CONDITIONAL.** No theorem-level novelty claim survives the current literature threats yet.

## 22. Sufficiency Gate S

**CONDITIONAL.** A validated RMST/joint or contract-level audit theorem could matter for abstention and survival reporting, but current diagnostics alone are insufficient.

## 23. M3 direction

**PATH A2 — RMST / JOINT FUNCTIONAL THEORY IS THE PRIMARY PAPER.** The audit comparison remains foundational, while joint multi-horizon functionals are the most defensible surviving route.

## 24. OT policy

`OT_DEFERRED_FROM_PRIMARY_THEORY`. No OT code or theory was added.

## 25. Synthetic-generation policy

`DEFERRED_PENDING_IDENTIFICATION_THEORY`. No synthetic generation was implemented.

## 26. Files modified/created

- `src/survival_ambiguity/identification/audit_models.py`
- `src/survival_ambiguity/identification/finite_grid.py`
- `src/survival_ambiguity/identification/functionals.py`
- `src/survival_ambiguity/identification/lp_bounds.py`
- `src/survival_ambiguity/identification/__init__.py`
- `tests/test_step04_identification.py`
- `scripts/step04_reference_checks.py`
- `results/step04/audit_checks.json`
- `docs/AUDIT_INFORMATION_THEORY.md`
- `docs/M3_THEOREM_CANDIDATES.md`
- `docs/M3_PAPER_CORE_TEST.md`
- `docs/M3_DIRECTION_DECISION.md`
- this report

## 27. Tests and commands

- `git pull --ff-only` — passed before edits.
- `python scripts/step04_reference_checks.py` — passed; 36 one-bin analytic/LP rows and 8 multi-bin/RMST rows generated.
- `python -m pytest -q` — passed, 8 tests.
- `python -m compileall -q src scripts tests` — passed.
- `git diff --check` — passed.
- SciPy: `1.17.1`; LP backend: HiGHS via `scipy.optimize.linprog(method="highs")`.
- Tolerance: `2e-8` for analytic/LP comparisons; solver residuals checked below `1e-8` in tests.
- No random seed, large dataset, model download, credential, or neural experiment was used.

## 28. Deviations

- A4-bounded and A5 were defined but not implemented because their estimands/contracts require additional choices.
- The audit-value computation was not promoted to a theorem after the fixed-`R` cap counterexample.
- Literature review was targeted, not exhaustive.

## 29. Limitations

This is population-level reference infrastructure. It does not provide confidence intervals, estimated-censoring guarantees, dependent-censoring results, unrestricted A0 conditional bounds, label-error partial-identification bounds under unknown `M`, or a novelty guarantee.

## 30. Recommended Step 05 only

Freeze and prove a contract-level joint/RMST theorem, or stop the project if the theorem reduces to standard robust inverse-problem geometry after a complete literature comparison. Do not begin synthetic generation or broad finite-sample inference before that gate is resolved.
