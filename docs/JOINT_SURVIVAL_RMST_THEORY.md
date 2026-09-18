# Joint Survival and RMST Theory (Step 05)

**Status:** `COMPLETE_WITH_WARNINGS`; the apparent Step 04 RMST gap was corrected and not promoted. No result is labeled `NOVEL`.

## 1. Exact contamination-compatible latent polytope

For event times `t_1<...<t_K` and a terminal tail state, let `p in R^{K+1}_+` with `1^T p=1`. For a validated censoring operator `A_q`, exact Huber compatibility is

`R=(1-epsilon) A_q p + epsilon Q`, `Q>=0`, `1^TQ=1`.

Eliminating `Q` gives exactly

`(1-epsilon)A_q p <= R`, `p>=0`, `1^T p=1`.

The mass equality for `Q` follows because both `R` and `A_qp` have mass one. Thus `P_epsilon(R,q)` is a compact convex polytope whenever nonempty. It has `K+1` nonnegative variables, one equality, and one inequality for each recorded cell. This is an `ELEMENTARY_DERIVATION`.

## 2. Survival-vector linear map

The project uses the strict convention `S(t_j)=P(T>t_j)`. Define

`B_{jk}=1{t_k>t_j}` for event states and `B_{j,infty}=1` for the tail. Then `s=Bp` is a nonincreasing survival vector. The map is linear, and the joint set

`S_epsilon(R,q)={Bp:p in P_epsilon(R,q)}`

is compact and convex. These are `ELEMENTARY_DERIVATION`s.

## 3. Pointwise intervals and rectangular envelope

`L_j=min_{s in S}s_j` and `U_j=max_{s in S}s_j` are sharp LP endpoints. The rectangle `R_pw=prod_j[L_j,U_j]` contains `S`. It can be strictly larger for a general convex set of monotone vectors; the rectangle is never treated as the identified set.

## 4. RMST and support function

For the finite convention used by the code,

`RMST_tau(p)=sum_k min(t_k,tau)p_k + tau p_infty`.

Equivalently, for `tau>=t_1`,

`RMST_tau = t_1 + sum_j w_j(tau) S(t_j)`,

where `w_j=max(0,min(t_{j+1},tau)-t_j)` for nonterminal `j`, and `w_K=max(0,tau-t_K)`. All weights are nonnegative. Direct bounds are support-function evaluations:

`U_RMST=h_S(w)` and `L_RMST=-h_S(-w)`.

Support-function language and the weighted-sum optimization identity are `ELEMENTARY_DERIVATION` / `KNOWN_OR_CLOSE_TO_KNOWN`, not contributions.

## 5. Pointwise-integration inequality and gaps

The valid naive interval is

`L_pw=t_1+sum_j w_j L_j`, `U_pw=t_1+sum_j w_j U_j`.

For nonnegative weights,

`L_RMST >= L_pw` and `U_RMST <= U_pw`.

Define `Gamma_minus=L_RMST-L_pw`, `Gamma_plus=U_pw-U_RMST`, and `Gamma_W=Gamma_minus+Gamma_plus`. Nonnegativity is elementary. Equality for a positive-weight side is equivalent to a common feasible optimizer attaining every active pointwise endpoint: if a single `p` attains the endpoints, equality follows; conversely, equality in a finite sum of nonnegative coordinate gaps forces every active coordinate gap to vanish at an optimizer of the weighted objective. This criterion is generic convex optimization.

## 6. Critical correction to the Step 04 interpretation

Step 04 compared an **unweighted sum** of pointwise survival widths (`0.81790`) with an RMST width (`0.61343`). That is not the pointwise-integrated RMST interval because RMST uses horizon weights. With the correct weights for the same scenario, the pointwise RMST width equals `0.61343`, matching direct RMST optimization to numerical tolerance. The earlier apparent strict coupling gap was therefore a dimensional comparison error, not a validated phenomenon.

This negative result is `CHECKED` and is a required correction to the Step 04 record.

## 7. Joint attainability

The implementation checks common endpoint feasibility by adding `Bp=U_active` or `Bp=L_active` as equality constraints. In the corrected Step 04 scenario both sides are feasible. Across the deterministic structured-censoring phase study, all tested active pointwise endpoints were jointly attainable and `Gamma_W` was at most `1.33e-15`.

This does not prove universal attainability. It does show that the original finite diagnostic does not support a strict-gap theorem.

## 8. K=2 symbolic result

A complete closed form was obtained for the no-censoring K=2 edge case. With `A=I`, define `u_i=min(1,R_i/(1-epsilon))`. The compatible set is the capped simplex `0<=p_i<=u_i`, `sum p_i=1`. Therefore:

`S(t_1) in [1-u_1, 1-max(0,1-u_2-u_infty)]`,

`S(t_2) in [max(0,1-u_1-u_2), u_infty]`.

Any linear functional, including RMST, is solved by filling the capped simplex in coefficient order; the resulting closed form agrees with LP over 24 deterministic cases. In this edge case the active survival extrema are jointly attainable, so the RMST coupling gaps are zero.

For general censored K=2, a global piecewise closed form was not obtained. The structured deterministic checks found no positive gap, but this is `OPEN`, not a theorem.

## 9. K=3 findings

The exact LP was written and checked for three event bins plus a tail. The direct RMST interval and correctly weighted pointwise interval agreed in the corrected Step 04 configuration. The phase study covered 48 deterministic cases for K=2,3,5; the maximum observed `Gamma_W` was `1.33e-15` at tolerance `2e-8`. No active-set phase structure or positive gap was found.

## 10. Source-of-coupling ablation

For an arbitrary convex set, event-mass conservation, monotonicity, and observation inequalities can jointly create tradeoffs. A generic monotone-set example can have vectors `(1,0.2)` and `(0.5,0.5)`: coordinatewise maxima are not a common point. However, that generic fact does not establish such a tradeoff for the validated right-censoring/Hüber polytope.

The current ablation result is negative: removing or retaining the simplex/monotonicity constraints in the tested structured censoring cases did not produce a survival-specific strict RMST gap. The remaining possible source is the exact operator-specific inequality pattern, but no theorem was found.

## 11. Triangular-operator and specialized-algorithm attempt

The implemented censoring matrix is nonnegative and column-stochastic, with rows determined by censoring support and the tie rule. It is not a universally triangular invertible matrix: censor rows aggregate latent states, and later event states can remain unobserved under early censoring. The exact feasible problem remains a small LP.

No correct backward greedy, water-filling, flow, or dynamic-programming algorithm beyond generic LP was established. The no-censoring capped-simplex solution is a special edge case only.

## 12. Worst-case, censoring, contamination, and grid analyses

A worst-case positive gap theorem was not found. In the modest deterministic study, the observed gap was numerical zero across K=2,3,5, several censoring patterns, and epsilon values `0,.05,.10,.20`. This cannot support monotonicity claims in censoring, contamination, or grid resolution. No claim is made that overall identified-set width is monotone in the coupling gap.

RMST-curve matrices for multiple restriction times are supported by the same `Cp` map, but no new joint-curve theorem was established. Two-group RMST contrasts and shared-contamination allocation were not implemented in this step.

## 13. Literature overlap

The support-function representation and coordinate-envelope inequality are standard convex/partial-identification machinery. Lee, Park & Lee (2024) directly study sensitivity analysis for RMST differences under unmeasured confounding, so any broad direct-RMST sensitivity claim is threatened. Zhao et al. (2015) and Zhong & Schaubel (2022) establish RMST-curve statistical theory, not this exact population Huber polytope, but they constrain broad RMST-curve novelty. Baitairian et al. (2026) is a major unresolved threat: the title and authors were found in an arXiv recent-statistics listing, but the exact paper record/appendix could not be reliably retrieved, so no theorem contents are inferred.

## 14. Claim status table

| Statement | Classification |
|---|---|
| Exact Huber feasible polytope | `ELEMENTARY_DERIVATION` |
| Convex survival-vector identified set | `ELEMENTARY_DERIVATION` |
| RMST support-function representation | `KNOWN_OR_CLOSE_TO_KNOWN` |
| Pointwise interval contains joint set | `ELEMENTARY_DERIVATION` |
| Correctly weighted pointwise RMST interval contains direct interval | `ELEMENTARY_DERIVATION` |
| Equality/common-optimizer criterion | `ELEMENTARY_DERIVATION` |
| Step 04 apparent strict gap | `FALSE_OR_REFUTED` as previously measured |
| K=2 no-censoring capped-simplex formula | `DERIVED` and `CHECKED` |
| General censored K=2 strict-gap theorem | `OPEN` |
| K=3 positive coupling gap | `NOT OBSERVED`, not disproved universally |
| Specialized censored-RMST algorithm | `OPEN` |
| Broad joint-RMST novelty | `OPEN` with strong generic prior-art threats |
