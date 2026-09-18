# Step 02 Sharpness Preflight

Date: 2026-09-18. Evidence labels are used literally: **[DERIVED]** means an elementary local derivation, **[CHECKED]** means executed finite verification, **[CONJECTURED]** means a proposed extension, and **[OPEN]** means unresolved. No result below is claimed novel.

## 1. Assumptions

Unless otherwise stated, `0 <= epsilon < 1`, all distributions are on a finite alphabet, TV is `||P-R||_TV = (1/2)||P-R||_1`, and contamination is population-level Huber contamination. The censoring law is known in the finite pilots, event is observed under `T <= C`, and the terminal state means `T` exceeds the last grid time.

## 2. Exact Huber compatibility geometry

For observed recorded-data law `R` and candidate clean law `P`,

`R = (1-epsilon)P + epsilon Q`.

For `epsilon > 0`, the implied contaminant is

`Q_i = [R_i - (1-epsilon)P_i] / epsilon`.

Therefore the necessary and sufficient conditions are:

1. `P_i >= 0`, `R_i >= 0`;
2. `(1-epsilon)P_i <= R_i` for every alphabet cell `i`;
3. `sum_i P_i = 1`.

The mass condition for `Q` then follows automatically:
`sum_i Q_i = [1-(1-epsilon)]/epsilon = 1`.
For `epsilon=0`, compatibility reduces to `P=R`.

Thus the exact feasible set is a coordinatewise-cap set, not a generic symmetric TV ball. Exact compatibility implies

`TV(P,R) = epsilon TV(P,Q) <= epsilon`,

but the converse fails in general. For example, with `R=(0.5,0.5)` and `epsilon=0.2`, `P=(0.7,0.3)` has `TV(P,R)=0.2` but violates `P_1 <= 0.5/0.8=0.625` and is not Huber-compatible.

## 3. Pairwise Huber-neighborhood overlap

For two clean laws `P0,P1`, equal-epsilon Huber neighborhoods intersect iff there is an `R` satisfying `R_i >= (1-epsilon) max(P0_i,P1_i)` for all `i`. Such an `R` exists iff

`(1-epsilon) sum_i max(P0_i,P1_i) <= 1`.

Since `sum_i max(P0_i,P1_i) = 1 + TV(P0,P1)`, the exact condition is

`TV(P0,P1) <= epsilon/(1-epsilon)`.

This is both necessary and sufficient for `0 <= epsilon < 1`; it is a pairwise-neighborhood statement, not the claim that every candidate in a TV ball of that radius is compatible with a fixed `R`. **[DERIVED]**

## 4. One-bin censoring derivation

Let an event occur at fixed time `t` with latent probability `p`; otherwise the event time exceeds the horizon. Follow-up reaches `t` with probability `g`, independently of the event state. Use recorded categories `(early censoring, observed event, observed event-free)`. Then

`A_g(p) = (1-g, gp, g(1-p))`.

For `p,p'`,

`TV(A_g(p), A_g(p')) = g |p-p'|`.

This is exact because the first coordinate is unchanged and the two remaining coordinate differences are `g(p-p')` and `-g(p-p')`. **[DERIVED; CHECKED]**

For a fixed observed law `R=(R_0,R_1,R_2)`, the exact identified interval is

`p_low = max(0, 1 - R_2/[(1-epsilon)g])`,

`p_high = min(1, R_1/[(1-epsilon)g])`,

provided `R_0 >= (1-epsilon)(1-g)`; otherwise the fixed `R` is infeasible under the model. This follows directly from the two coordinate caps involving `gp` and `g(1-p)`. **[DERIVED]**

## 5. Sharp one-bin contaminated population diameter

Two latent values can generate one common contaminated recorded law iff their clean recorded laws have overlapping Huber neighborhoods. Combining the pairwise condition with the exact one-bin TV identity gives

`g |p-p'| <= epsilon/(1-epsilon)`.

Therefore the sharp population diameter is

`diam(p) = min{1, epsilon/[(1-epsilon)g]}`.

The lower bound is attained by choosing `|p-p'|` equal to the right-hand side when it is below 1, and by `p=0,p'=1` when the right-hand side is at least 1. The overlap theorem supplies common `R` and hence valid `Q,Q'`, so this is not merely a numerical upper bound. Edge cases: `epsilon=0` gives diameter 0; `g=0` gives diameter 1 for every `epsilon` because no event information reaches the record; and `epsilon >= 1/2` is not required for saturation—the threshold is `epsilon >= g/(1+g)` when `g>0`. **[DERIVED]**

This is a population identification diameter. It is not a confidence interval, finite-sample bound, estimator error bound, or censoring-model misspecification analysis.

## 6. Multi-bin operator and exact optimization

For event times `t_1 < ... < t_K`, a terminal tail state, censoring support `c_1,...,c_L`, and censoring probabilities `q_l`, define `A_q` with rows for observed events and censoring cells and columns for latent event states plus tail:

`A_q[row(event j), col(event j)] = sum_{l:t_j <= c_l} q_l`,

`A_q[row(censor l), col(event j)] = q_l 1{t_j > c_l}`,

`A_q[row(censor l), col(tail)] = q_l`.

The tie convention is explicit: `t_j <= c_l` is an observed event. Each column is nonnegative and sums to one. The exact fixed-`R` Huber identified set is the polytope

`p >= 0`, `1^T p=1`, `(1-epsilon) A_q p <= R`.

Any linear functional `w^T p` (including a grid survival probability or discrete RMST) has sharp extrema by two linear programs. This is a finite-dimensional reduction, not an implemented theorem about general survival laws.

The executed pilot used `K=3`, `q=(0.15,0.25,0.35,0.25)`, terminal tail, and exact LP constraints. At the chosen `R=A_q p_true`, widths for survival after the last event were 0, 0.05263, and 0.25 at epsilon 0, 0.05, and 0.2; RMST widths were 0, 0.10526, and 0.5. These are **[CHECKED]** values for one finite configuration, not general claims.

## 7. Rare-subgroup derivation

Let the rare group have clean prevalence `pi`, subgroup event probability `p_g`, and subgroup follow-up `g_1`. Under **Model G-A**, the observed subgroup label is trusted, the clean prevalence is fixed at `pi`, but arbitrary contamination may allocate its mass to the rare observed subgroup. Keep the majority law fixed and vary only the rare conditional law. The joint clean recorded-law TV distance is

`TV(P_0^rec,P_1^rec) = pi * g_1 * |p_g-p'_g|`.

The exact pairwise Huber overlap condition therefore gives the sharp conditional-world diameter

`diam(p_g) = min{1, epsilon/[(1-epsilon) pi g_1]}`.

This derives the charter intuition with the required `(1-epsilon)` correction and a saturation threshold; it is not a finite-sample result and its scope depends on the trusted-label/fixed-prevalence model. **[DERIVED]**

A distinct constrained variant—contamination is also required to preserve the subgroup marginal exactly—does not permit global contamination to be reallocated into the rare group; the `pi` amplification disappears in this conditional perturbation construction. This is why “trusted label” must be specified together with the allowed contaminant law.

Under **Model G-B**, subgroup labels may themselves be contaminated or misassigned. The target `S_g` must then define whether `g` refers to latent clean membership or observed membership. Without a misclassification/contamination restriction, the observed subgroup-conditioned target is not the same estimand as the clean subgroup target, and no single sharp formula is asserted here. **[OPEN]**

For Model G-A, saturation occurs when `epsilon >= pi*g_1/(1+pi*g_1)`, and `g_1=0` gives complete subgroup nonidentification. The exact result is a phase transition in a deliberately simple model, but whether it supports a sufficiently distinctive paper contribution remains open.

## 8. Restricted-class pilot

`Theta_0` is the unrestricted simplex over three event masses plus terminal tail. `Theta_1` is the monotone discrete-hazard class, checked on a deterministic grid with step 0.05. The pilot enumerated 643 candidate laws. It found zero width at epsilon 0 as expected and a maximum fixed-`R` width of approximately 0.25 at epsilon 0.2 for the selected survival functional. This is a grid calculation, not an exact optimization over `Theta_1`; it only shows that the restriction did not eliminate ambiguity in this example. **[CHECKED]**

No theorem or sufficiency claim is supported by this pilot. The restriction is scientifically interpretable, but the current evidence does not show a nontrivial threshold change or a result beyond a constrained LP/grid exercise. **[OPEN]**

## 9. TV versus OT

Exact Huber compatibility is coordinatewise and TV-compatible but not equal to a TV ball. A geometry-aware OT ambiguity set adds a transport-cost assumption. Robust OT literature provides principled outlier-robust Wasserstein discrepancies under Huber contamination, including partial-mass removal and statistical guarantees.[2][3] It does not automatically establish sharp survival identification for the present observation operator.

Tiny counterexamples clarify the distinction. On support `{0,1}` with unit cost, `W_1` equals TV, so OT adds no geometry. On `{0,1,10}`, a TV radius 0.2 can move 0.2 mass to 10, while a `W_1` radius 0.2 permits at most 0.02 mass moved directly from 0 to 10. The latter is tighter only because it assumes a transport budget; it is not a free improvement over arbitrary Huber contamination. For survival functionals, whether that assumption is scientifically appropriate depends on the meaning of nearby event times and contamination.

Preliminary verdict: **OT_NOT_JUSTIFIED_YET**. It should remain an ablation/alternative assumption, not the primary theory, until a survival-specific validity and usefulness result is proved.

## 10. Status ledger

### PROVED IN THIS STEP

- Exact finite-alphabet Huber compatibility characterization.
- Exact equal-epsilon Huber-neighborhood overlap condition.
- One-bin observed-law TV identity.
- Sharp one-bin population diameter under the stated model.
- Exact finite-grid fixed-`R` LP formulation.

These are local derivations; publication novelty is not established.

### NUMERICALLY CHECKED

- Six one-bin TV identities.
- Finite censoring matrix normalization.
- Six fixed-`R` multi-bin LP rows.
- Three pairwise finite-grid LP rows.
- Monotone-hazard step-0.05 pilot.

### CONJECTURED

- A useful survival-specific theorem may remain in the interaction between subgroup allocation constraints, censoring support, and restricted classes.

### OPEN

- Model G-B sharp formula.
- Exact restricted-class identification frontier.
- Finite-sample inference with estimated censoring.
- Whether any result survives a complete literature novelty audit.
- Whether compatible synthetic worlds add sufficient scientific value.
