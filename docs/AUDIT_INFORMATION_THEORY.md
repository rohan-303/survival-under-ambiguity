# Audit-Information Theory (Step 04)

**Status:** population-level finite-grid reference framework, with explicit negative findings. No statement below is labeled `NOVEL`.

## 1. Finite-grid grouped survival model

There are groups `g=1,...,J`, clean prevalences `pi_g>0`, and conditional event-mass vectors `p_g` on `K` event states plus a terminal tail state. For known subgroup censoring laws, `A_g=A_{q_g}` maps `p_g` to recorded cells (event cells and censoring cells). The clean recorded joint law is the block vector

`B p = (pi_1 A_1 p_1, ..., pi_J A_J p_J)`.

Columns of each `A_g` sum to one. Event rows use `T <= C` as the tie convention; the terminal state receives mass not assigned to an event before censoring. The implementation checks nonnegativity, column conservation, and the no-censoring limit on small grids.

The population contamination law is exactly `R=(1-epsilon)B p + epsilon Q`; no TV ball is substituted for this constraint.

## 2. Audit regimes

- **A0, global only:** `Q` is arbitrary and clean group prevalence is not externally fixed. A conditional subgroup functional is a ratio and is not represented as an LP without additional prevalence restrictions. Joint subgroup masses are linear.
- **A1, trusted marginal:** clean `pi` is externally known; `Q` remains arbitrary. This is a model-contract restriction on `p`, not a claim that the contaminated group marginal equals `pi`.
- **A2, marginal-preserving:** clean and contaminant group marginals are both `pi`, hence the observed group marginal must equal `pi`. Conditional contamination is then the same mixture fraction in every group.
- **A3, group caps:** `Q(G=g)/pi_g <= bar_epsilon_g` is a conditional cap on contaminating mass in group `g`; equivalently total contaminating mass in that group is at most `pi_g bar_epsilon_g`. It is not the same as a cap on the fraction of contamination globally assigned to a group.
- **A4-known:** labels pass through known row-stochastic `M`, `M_ab=P(G_obs=b|G_clean=a)`, before the recorded law is contaminated. The resulting known linear operator is LP-compatible.
- **A4-bounded:** only bounds on entries of `M` are known. This was not implemented because the feasible set and target contract need a separate explicit specification.
- **A5:** optional intersection of A1/A3/A4 constraints; retained as a future composition, not used to manufacture a narrow result.

## 3. Feasible sets and information partial order

For fixed recorded law `R`, `F_A(R)` consists of nonnegative latent masses satisfying simplex constraints and coordinatewise exact-Huber residual constraints `R-(1-epsilon)Bp >= 0`, plus the regime-specific audit constraints.

On a common domain, A2 is contained in A1, and A3 adds a contract check to A1. However, the domains differ: A2 is infeasible whenever the observed group marginal is not `pi`, while A1 can remain feasible. Thus these are not a useful universal total order. A4 changes the observation operator and is not ordered with A1 unless the label channel and data contract are fixed jointly.

A direct counterexample to treating audit regimes as a total order is an observed law with group marginal different from `pi`: it is feasible under A1 with a contaminant carrying group-marginal mass, but infeasible under A2. Conversely, a label channel can make an A4-known contract informative about clean membership while an A3 outcome-contamination cap says nothing about label corruption. These are incomparable information types.

## 4. One-bin closed forms

For a trusted group with prevalence `pi`, follow-up `g`, and arbitrary global Huber contamination, the worst-case population diameter over compatible observed laws is the Step 03 elementary result

`min(1, epsilon / ((1-epsilon) pi g))`.

Its complete-nonidentification threshold is `epsilon >= pi*g/(1+pi*g)`.

If the contamination preserves group marginal mass (A2), the conditional within-group contamination fraction is `epsilon`, giving the corresponding worst-case conditional diameter

`min(1, epsilon / ((1-epsilon) g))`.

The `1/pi` amplification disappears because the adversary cannot concentrate mixture mass into the target group. This is an `ELEMENTARY_DERIVATION`, not a novelty claim.

For A3, define the conditional contaminating rate `eta_g=Q(G=g)epsilon/pi_g` under the exact mixture decomposition. The one-group worst-case rate is bounded by

`eta_g^max = min(bar_epsilon_g, epsilon/pi_g)`

and the local one-bin diameter is

`min(1, eta_g^max / ((1-eta_g^max) g))`.

This is a comparison of contamination contracts. It is not automatically the width of a fixed-observed-law LP: once `R` and `pi` are fixed, the residual group mass is already fixed. The reference solver therefore treats A3 caps as explicit feasibility constraints and records the important negative result that they need not shrink a fixed-data interval unless the audit contract changes the admissible observed-law class.

For A0 with unknown clean prevalence, the conditional target is generally linear-fractional. No universal formula is asserted because the clean prevalence and the latent group/outcome relation are not identified by the global contamination contract alone.

For A4-known, known `M` produces a linear operator. Bounds are LPs when the clean prevalence is fixed; the label channel may improve or destroy information depending on its invertibility and the available outcome cells. A4-bounded was left `OPEN`.

## 5. Sharp survival-probability bounds

For a fixed prevalence and A1/A2/A3, define `w_j(t)=1{t_j>t}` plus a tail weight of one. The endpoint is the minimum or maximum of `w(t)^T p_g` over the feasible LP. Endpoints are sharp because finite-dimensional feasible polytopes attain linear extrema whenever nonempty.

The implementation does not replace the full operator by `G_C,g(t)` at every horizon. The operator determines which event mass reaches which recorded cell. A scalar follow-up reduction is valid only in the one-event reduction.

## 6. RMST bounds

For event states `t_j` and terminal tail, the discrete RMST weights are `min(t_j,tau)` and `tau`. The same LP gives sharp RMST endpoints. RMST is not obtained by combining unrelated pointwise extrema.

In the tiny diagnostic scenario, group 0 had pointwise widths `0.23148`, `0.29321`, and `0.29321`, while the direct RMST LP width was `0.61343`; the sum of pointwise widths is `0.81790`. This demonstrates the expected coupling: the direct functional interval can be strictly narrower than a naive sum of independent pointwise widths. It does not establish a general theorem.

## 7. Audit value

For a fixed observed law and a genuinely nested contract, define `V_g(A->B;psi)=W_g^A-W_g^B`. The Step 04 analysis found a qualification: A2 and A3 can change feasibility of the observed-data contract without changing the conditional LP width for a fixed `R` and fixed `pi`. Therefore a positive value-of-audit theorem requires comparing admissible observed-law classes, not simply adding a constant group-marginal row to one fixed LP.

The useful future value definition should distinguish:

1. **conditional value:** width reduction at fixed `R`, when the added constraint actually restricts latent outcome allocations;
2. **contract value:** reduction in worst-case width over all `R` admissible under the audit contract.

The latter is the natural target for a nontrivial audit-restoration result. It remains `OPEN` beyond the one-bin closed forms.

## 8. Exact width-restoration implication

The one-bin formulas give a threshold comparison: global-only complete nonidentification occurs when `epsilon >= pi*g/(1+pi*g)`, while marginal-preserving contamination uses the larger effective denominator `g`, and a group cap replaces the global rate by `eta_g^max`. Thus a contract can move a group from width one to width below one exactly when its permitted conditional rate satisfies

`eta_g^max < g/(1+g)`.

This is a sharp contract-level threshold in the one-bin model, but it is still an elementary contamination-budget comparison. It is not promoted as the Step 04 theorem.

## 9. Multi-bin primal LP

For A1-A3, variables are conditional masses `p_g>=0`, with `sum_k p_gk=1`. Let `B` be the block observation operator. The exact-Huber inequalities are

`(1-epsilon) B p <= R`.

The objective is `w^T p_g` for `S_g(t)` or RMST. For A4-known, replace `B` by the label-mixed operator `B_M`, with entries `pi_a M_ab A_a` in observed-label block `b`. All constraints and objectives remain linear when clean prevalences are fixed. A0 uses joint masses `x_g=pi_g p_g`, `sum_gk x_gk=1`; joint survival mass is linear, while conditional survival is a ratio.

Dimensions: with `J` groups and `K+1` latent states, the fixed-prevalence LP has `J(K+1)` variables, `J` simplex equalities, and `J m` Huber inequalities when each group has `m` recorded cells.

## 10. Dual/certificate formulation

For the minimization LP `min c^T x` subject to `Hx<=R`, `Ex=1`, `x>=0`, one exact dual is

`max R^T y + 1^T z` subject to `H^T y + E^T z <= c`, `y<=0`.

The upper endpoint uses `-c` and negates the optimum. At a feasible optimum, primal and dual objectives agree; the dual variables provide a certificate. A constraint whose right-hand side is an audit cap has a standard LP shadow-price interpretation only within the local active-set/sensitivity regime. In the present A3 fixed-R formulation, the cap rows are data-contract rows with zero latent coefficients, so their multipliers diagnose feasibility rather than a universal width reduction.

The reference solver exposes HiGHS inequality marginals and primal residuals. They are numerical certificates for the checked instance, not a symbolic dual theorem.

## 11. Operator-level generalization

The correct finite-grid modulus is

`omega_{g,A}(v)=sup{|v^T(p_g-p'_g)|: p,p' have a common R under regime A}`.

The one-bin `pi*g` factor is the special case where changing one event probability changes the clean recorded law in one observable direction. In the multi-bin problem, the relevant quantity is the support function of the feasible operator image, not a scalar horizon follow-up. This formulation is `POTENTIALLY_NOVEL` only as a research direction; no theorem-level novelty is claimed.

## 12. Joint attainability

A pointwise optimizer at each horizon need not be the same latent survival vector. The joint set

`I_g={ (w(t_1)^T p_g,...,w(t_K)^T p_g): p in F_A(R) }`

is the image of one feasible polytope and automatically respects nonnegative event masses and survival monotonicity. Direct RMST optimization over that polytope is the valid way to handle joint attainability. Combining independently optimized pointwise endpoints is prohibited.

## 13. Label-error extension

A4-known is a linear-channel baseline. A4-bounded requires optimizing over `M` as well as `p`; if the target clean subgroup is not defined separately from the observed label, the problem is ill-posed. Existing work on partial identification with misclassified data provides a direct prior-art threat, and recent survival work using error-prone subgroup/biomarker information is an additional threat. The project does not claim a label-error theorem.

## 14. Literature overlap

The literature kill test remains negative for any novelty claim. Classical censoring identification/bounds, general Huber contamination geometry, partial identification with misclassified data, robust inference with censored survival data, robust subgroup analysis, and latent-subgroup uncertainty all threaten broad framing. Targeted records include:

- Peterson et al., classical competing-risk/censoring bounds: https://www.pnas.org/doi/10.1073/pnas.73.1.11
- Robust inference with censored survival data (Scandinavian Journal of Statistics, 2022): https://onlinelibrary.wiley.com/doi/full/10.1111/sjos.12570
- Partial identification of probability distributions with misclassified data: https://www.sciencedirect.com/science/article/abs/pii/S0304407607002564
- Error-prone subgroup/biomarker survival analysis with subgroup-specific sensitivity/specificity: https://pmc.ncbi.nlm.nih.gov/articles/PMC12869679/
- Robust subgroup analysis for heterogeneous censored data: https://arxiv.org/html/2607.11389
- Latent subgroup classification uncertainty: https://pmc.ncbi.nlm.nih.gov/articles/PMC9508766/

These sources do not prove exact theorem overlap, but they prevent a novelty claim. The strongest threat is that the one-bin audit comparison is a relabeling of standard contamination allocation and the multi-bin LP is a direct robust inverse-problem formulation.

## 15. Open problems

1. Prove a contract-level audit-restoration frontier over all admissible `R`.
2. Decide whether a nontrivial RMST/operator theorem survives exact literature comparison.
3. Derive sharp A4-bounded bounds with a frozen estimand.
4. Establish whether dual audit sensitivity identifies a meaningful audit-prioritization rule.
5. Keep finite-sample and estimated-censoring uncertainty out of the theory until these population questions are resolved.

## 16. Claim classification

| Result | Classification |
|---|---|
| A1/A2 one-bin formulas | `ELEMENTARY_DERIVATION` |
| A3 contract threshold | `ELEMENTARY_DERIVATION` |
| Fixed-R A3 cap may only test feasibility | `CHECKED` and `POTENTIALLY_NOVEL` as a negative design warning, not a novelty claim |
| Multi-bin LP | `KNOWN_OR_CLOSE_TO_KNOWN` threat; `CHECKED` implementation |
| Direct RMST LP and joint attainability handling | `CHECKED`; theorem status `OPEN` |
| Operator modulus | `PROPOSED` / `OPEN` |
| A4-known channel LP | `CHECKED` implementation; theorem status `OPEN` |
| Broad novelty | `OPEN`, with strong `KNOWN_OR_CLOSE_TO_KNOWN` threats |
