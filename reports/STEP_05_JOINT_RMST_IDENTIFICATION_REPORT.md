# STEP 05 — JOINT RMST IDENTIFICATION REPORT

## 1. Final status

**COMPLETE_WITH_WARNINGS**

The exact finite-grid latent polytope, survival-vector projection, support-function formulation, common-attainability check, K=2 no-censoring closed form, corrected RMST comparison, deterministic phase study, targeted prior-art review, and negative direction decision were completed. The central Step 04 apparent strict gap was refuted as an invalid unweighted-width comparison. No novelty or positive coupling theorem was established.

## 2. Starting HEAD

- Repository: `C:/Users/rohan/survival-under-ambiguity`
- Starting HEAD: `5ceaa3f5f1f17c8215986df2c52175957f607e26`
- Branch: `main`
- Remote: `https://github.com/rohan-303/survival-under-ambiguity.git`
- Starting worktree: clean and aligned with `origin/main`
- `git pull --ff-only`: passed; already up to date.

## 3. Frozen model and assumptions

One coherent finite-grid latent event distribution with event states `t_1<...<t_K` plus a terminal tail; known right-censoring operator; strict survival convention `S(t)=P(T>t)`; fixed contaminated population law `R`; exact population Huber contamination; unrestricted latent event masses. No neural models, synthetic generation, OT, real data, finite-sample inference, estimated censoring, or dependent censoring.

## 4. Exact latent feasible polytope

Exact compatibility is equivalent to

`p>=0`, `1^T p=1`, `(1-epsilon)A_q p <= R`.

The residual defines `Q=[R-(1-epsilon)A_qp]/epsilon`; its mass is one because both `R` and `A_qp` are probability vectors. The feasible set is therefore a compact convex polytope when nonempty, with `K+1` variables, one equality, and one inequality per recorded cell.

## 5. Joint survival identified set

The survival map is `s=Bp`, where `B_jk=1{t_k>t_j}` and the terminal column is one. The joint set `S={Bp:p in P_epsilon(R,q)}` is compact, convex, and has nonincreasing coordinates.

## 6. Pointwise interval results

Each `L_j` and `U_j` is a sharp LP endpoint. The rectangle `prod_j[L_j,U_j]` contains the joint set but is not treated as the identified set.

## 7. Joint attainability

A common optimizer is checked by adding all active equalities `Bp=U_active` or `Bp=L_active` to the LP. This is an elementary convex-feasibility criterion. In the corrected Step 04 scenario, both upper and lower active endpoint collections were jointly attainable.

## 8. RMST support-function formulation

The direct finite-grid functional is

`RMST_tau(p)=sum_k min(t_k,tau)p_k + tau p_infty`.

For `tau>=t_1`, it equals a constant plus a nonnegative weighted sum of strict survival coordinates. Direct endpoints are support-function evaluations `h_S(w)` and `-h_S(-w)`. The support-function representation is generic partial-identification machinery, not a novelty claim.

## 9. Pointwise integration bound

With the correct RMST weights,

`L_RMST >= L_pw` and `U_RMST <= U_pw`.

The coupling gaps are `Gamma_minus=L_RMST-L_pw`, `Gamma_plus=U_pw-U_RMST`, and `Gamma_W=Gamma_minus+Gamma_plus`.

## 10. Coupling-gap definitions and correction

Step 04 compared an unweighted sum of pointwise widths (`0.81790`) to an RMST width (`0.61343`). That was not the RMST pointwise-integrated interval. After applying the correct RMST weights, the pointwise and direct RMST widths both equal `0.61343` in the same scenario. The earlier apparent strict gap is therefore classified `FALSE_OR_REFUTED` as measured.

## 11. Equality conditions

For positive active weights, equality on one side holds exactly when one feasible latent distribution attains all corresponding active pointwise endpoints. This is a generic weighted-sum equality result. It was implemented as a feasibility check, not promoted as a theorem of novelty.

## 12. K=2 closed form

A closed form was obtained and verified for the no-censoring K=2 edge case. With `A=I` and `u_i=min(1,R_i/(1-epsilon))`, the feasible set is a capped simplex:

`S(t_1) in [1-u_1, 1-max(0,1-u_2-u_infty)]`,

`S(t_2) in [max(0,1-u_1-u_2),u_infty]`.

Any linear functional is solved by coefficient-ordered capped-simplex filling. It matched LP results over 24 deterministic cases. No complete closed form was obtained for general censored K=2.

## 13. K=3 findings

The exact K=3 LP was implemented. In the corrected Step 04 configuration and the deterministic study, correctly weighted direct and pointwise RMST intervals agreed. No positive coupling phase was found.

## 14. Source of coupling

Generic monotone convex sets can have incompatible coordinatewise maxima, so a generic rectangle gap is possible. However, the validated right-censoring/Hüber polytope did not produce such a gap in the tested cases. No survival-specific source of a positive gap was isolated.

## 15. Triangular-operator findings

The censoring operator is nonnegative and column-stochastic but is not universally triangular/invertible because censoring rows aggregate latent states. No valid greedy, water-filling, flow, dynamic-programming, or other specialized exact algorithm beyond generic LP was established.

## 16. Specialized algorithm result

Only the no-censoring capped-simplex allocation has a direct coefficient-order algorithm. The general censored problem remains a transparent small LP. No algorithmic contribution was claimed.

## 17. Worst-case gap

No positive worst-case gap theorem was obtained. The 48-case structured phase study had maximum observed `Gamma_W=1.33e-15`, below the `2e-8` comparison tolerance. This is not a proof that all possible operators have zero gap.

## 18. Censoring dependence

No monotonicity claim was made. The study did not establish that heavier censoring increases or decreases the coupling gap.

## 19. Contamination dependence

No monotonicity or intermediate-contamination phase transition was established. Tested values were `0,.05,.10,.20`.

## 20. Grid dependence

K=2, 3, and 5 were checked. No positive normalized gap was observed. A grid-resolution theorem was not obtained.

## 21. RMST-curve findings

Multiple restriction times can be represented by a matrix map `m=Cp`, but no additional joint RMST-curve theorem was established. Sampling RMST-curve literature remains a prior-art constraint, not an exact overlap finding.

## 22. Two-group contrast findings

Two-group RMST differences under shared contamination were not implemented in Step 05. No claim is made about their identified intervals.

## 23. Literature kill test

The support-function and weighted-envelope steps are generic. Lee, Park & Lee (2024) directly study RMST sensitivity under unmeasured confounding. Zhao et al. (2015) and Zhong & Schaubel (2022) cover RMST curves under censored-data inference. Baitairian et al. (2026) is a major unresolved threat: the title/authors were found in an arXiv recent-statistics listing, but the exact paper record and appendix could not be reliably retrieved, so no theorem contents were inferred.

## 24. Baitairian 2026 comparison

Status: **UNRESOLVED PRIOR-ART THREAT**. It may contain direct sharp survival/RMST sensitivity results, but exact overlap was not verified. The project makes no claim that its result is distinct.

## 25. Lee 2024 comparison

Status: **CLOSE BUT DIFFERENT MODEL**. The paper targets RMST differences under unmeasured confounding, not the exact fixed-`R` Huber contamination-after-censoring polytope. It nevertheless blocks broad claims that direct sharp RMST sensitivity analysis is new.

## 26. Generic partial-identification comparison

The polytope projection, support function, and dual weighted optimization are standard convex identified-set machinery. Any surviving contribution would need a nontrivial censoring-specific theorem, not merely an LP implementation.

## 27. Counterexamples

- The Step 04 apparent strict gap disappears after correct RMST weighting.
- A generic monotone convex set can have incompatible pointwise maxima, but no such strict gap was found in the tested structured censoring models.
- No tested case showed a positive gap increasing with censoring, contamination, or grid resolution.

## 28. Theorem candidates

J1/J2 are elementary or generic. J3 is a checked no-censoring K=2 edge case. J4–J7 remain open and unsupported after the correction. J8 was not implemented. Details are in `docs/M4_THEOREM_CANDIDATES.md`.

## 29. Joint Theory Gate J

**FAIL.** The central positive coupling phenomenon was not validated; the remaining machinery is generic support-function/LP theory without a survival-specific theorem.

## 30. RMST Gate M

**FAIL.** RMST is correctly handled by direct LP optimization, but no distinct RMST theory beyond generic linear-functional identification was established.

## 31. Novelty Gate N

**FAIL.** No exact theorem or algorithm remained clearly distinct after the corrected calculation and targeted prior-art review.

## 32. Sufficiency Gate S

**FAIL.** The measured effect was an invalid comparison; the corrected study does not show that direct RMST identification changes scientific reporting in this model.

## 33. M4 path

**PATH J6 — JOINT THEORY IS TOO GENERIC; PIVOT AGAIN.** Step 05 does not authorize Step 06 implementation. A future redesign would require a different estimand, a genuinely meaningful structural restriction, or a new contract-level theorem.

## 34. OT policy

`OT_DEFERRED_FROM_PRIMARY_THEORY`.

## 35. Synthetic-generation policy

`DEFERRED_PENDING_IDENTIFICATION_THEORY`.

## 36. Files created/modified

- `src/survival_ambiguity/identification/joint_survival.py`
- `src/survival_ambiguity/identification/__init__.py`
- `tests/test_step05_joint_survival.py`
- `scripts/step05_reference_checks.py`
- `results/step05/joint_rmst_checks.json`
- `results/step05/counterexamples.json`
- `docs/RMST_JOINT_PRIOR_ART.md`
- `docs/JOINT_SURVIVAL_RMST_THEORY.md`
- `docs/M4_THEOREM_CANDIDATES.md`
- `docs/M4_SUFFICIENCY_TEST.md`
- `docs/M4_DIRECTION_DECISION.md`
- this report

## 37. Tests and commands

- `git pull --ff-only` — passed before edits.
- `python scripts/step05_reference_checks.py` — passed; 24 K=2 closed-form rows and 48 phase-study rows generated.
- `python -m pytest -q` — passed after final correction.
- `python -m compileall -q src scripts tests` — passed.
- `git diff --check` — passed.

## 38. Solver/version/tolerance

- Python: `3.11.15`
- SciPy: `1.17.1`
- LP backend: `scipy.optimize.linprog(method="highs")`
- Analytic/LP tolerance: `2e-8`
- Maximum observed phase-study gap: `1.33e-15`
- No large simulation, real dataset, neural model, synthetic generator, credential, or copyrighted paper was staged.

## 39. Deviations

- General censored K=2 symbolic formulas were not forced after no positive gap was found.
- Baitairian 2026 was recorded as an unresolved access/metadata threat rather than summarized from an unverified source.
- Two-group RMST contrasts and bounded label-error channels were not expanded.
- The previous Step 04 report was not rewritten; the correction is documented here and in the M4 theory/direction documents. History was not rewritten.

## 40. Known limitations

The result is population-level and finite-grid. It does not prove universal zero coupling gap, establish a specialized censored-RMST algorithm, resolve Baitairian 2026, provide finite-sample inference, or establish novelty.

## 41. Recommended Step 06 only

Do not start Step 06 automatically. First decide whether to redesign the research question around a genuinely structural survival restriction or stop this theory line. Synthetic generation and finite-sample inference remain deferred.
