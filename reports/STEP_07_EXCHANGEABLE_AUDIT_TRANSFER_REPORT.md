# STEP 07 — EXCHANGEABLE AUDIT TRANSFER REPORT

## 1. Final status

**COMPLETE_WITH_WARNINGS — pivot failed the survival-specificity kill test.** The frozen transfer model is mathematically valid, but the tested theorem is standard finite-population audit certification plus a known censoring-channel transform.

## 2. Starting HEAD

`a659fc7c6ef1c2aa250c5266fd0c1d1015cb6285` on `main`; `git pull --ff-only` reported up to date.

## 3. Transfer assumption

Within trusted stratum `h`, corruption count `M_h` is fixed but unknown and corruption locations are uniform conditional on `M_h`. E2 additionally imposes `sum_h M_h <= m`.

## 4. Why this assumption was selected

Step 06 established that unrestricted adversarial locations make limited auditing unable to guarantee zero width. Exchangeable locations were the single frozen minimal transfer model required for this kill test; no assumption shopping was performed.

## 5. What remains adversarial

Corrupted values remain arbitrary. No error channel, error-magnitude model, outcome independence, or unbiasedness is assumed. The audit reveals only the correct recorded tuple `(Y*, Delta*)`, never latent post-censoring `T`.

## 6. Hypergeometric certification

`D_h | M_h,N_h,b_h` is exactly hypergeometric. Equal-tail inversion over `M_h=0,...,N_h` produced conservative confidence sets. `b_h=0` yields all possible counts; `b_h=N_h` identifies `M_h` exactly.

## 7. Simultaneous coverage

Bonferroni gives coverage at least `1-alpha` when `sum alpha_h <= alpha`. Exact exhaustive checks covered `N` values 1–9 and every `M,b` combination; representative minimum coverages included `0.9821428571` at `N=8,b=3,alpha=.05` and `0.9848484848` at `N=12,b=6,alpha=.05`.

## 8. Recorded-event certificate

Conditional on the count upper endpoint, the exact adversarial interval changes unverified observed events to non-events for the lower endpoint and non-events to events for the upper endpoint. Audited clean records are fixed.

## 9. Survival certificate

For the declared one-bin channel `r_h=g_h p_h`, `g_h>0`, map the recorded interval by division by `g_h` and truncate to `[0,1]`. For `g_h=0`, the latent event probability is not identified.

## 10. Sample complexity

The implemented `b*` is conditional on `D_h=0`, worst-case over observed binary composition, and targets a declared interval width. It is not an expected or worst-case-over-discovery count. Example at `N=20,alpha=.05`: for `g=1,delta=.10`, `b*=17`; for `g=.5,delta=.10`, `b*=20`; for `g=.2`, the same target requires full audit in the tested grid.

## 11. Acceptance-sampling kill test

**YES.** The one-bin survival width equals `min(1, recorded-width/g)`. The survival part adds no theorem beyond exact hypergeometric certification plus scalar rescaling.

## 12. Multi-stratum aggregate target

For `p=sum_h pi_h p_h`, independent certificates combine by prevalence-weighted interval arithmetic. Under E2, a tiny exact integer optimization allocates a shared remaining corruption cap across strata.

## 13. Audit-allocation result

Exact enumeration is implemented for H≤3-sized examples. Under the declared clean-audit weighted-width objective, allocations can differ from proportional allocation, but only because the objective includes `pi_h/g_h` and finite-population step effects. No general optimality or greedy theorem was established.

## 14. Censoring-sensitive allocation

Numerically, low `g_h` can make a stratum expensive to certify: in the example `N=(20,20)`, `g=(1,.2)`, `pi=(.6,.4)`, the exact objective favored auditing the well-followed stratum for moderate budgets. This is scalar amplification, not a distinct censoring-survival interaction.

## 15. Rare-vs-censored example

A rare, well-followed group can receive more audit effort than a common, heavily censored group under the weighted objective; reversing prevalences or follow-up can reverse the ranking. The result is an objective-dependent rescaling, not a universal rare-group theorem.

## 16. Global-cap coupling

The E2 cap can tighten aggregate intervals relative to independent stratum caps. The implementation optimizes the coupled integer corruption allocation exactly for tiny cases. This is potentially useful computationally but did not pass the novelty/survival-specificity standard.

## 17. Marginal audit value

Discrete marginal values are computable by enumeration. Diminishing returns, submodularity, and greedy optimality were not claimed.

## 18. Adaptive-wave note

Observed first-wave discrepancies can change a second-wave allocation, as in ordinary multiwave validation. No distinctive adaptive theorem was established.

## 19. Two-bin findings

**NOT COMPUTED.** The one-bin kill test failed, so a two-horizon extension was not used to rescue the direction.

## 20. Prior-art comparison

Hypergeometric audit certification is directly threatened by finite-population audit literature.[4]

Two-phase survival validation and multiwave EHR validation threaten model-based and adaptive allocation claims.[1][2]

Semi-verified learning threatens broad trusted/untrusted transfer novelty.[3]

## 21. Transfer Theory Gate T

**FAIL.** The frozen transfer model yields correct certification, but no nontrivial theorem beyond standard audit sampling and elementary downstream composition survived.

## 22. Survival-Specificity Gate C

**FAIL.** Censoring enters only through the known scalar `g_h` in the evaluated one-bin model.

## 23. Novelty Gate N

**FAIL.** No exact surviving contribution was distinguished from hypergeometric certification, survival validation, influence-function allocation, multiwave validation, or semi-verified transfer.

## 24. Sufficiency Gate S

**FAIL.** Although the certificate can change an audit plan, the result does not provide a sufficiently distinctive survival-specific decision rule.

## 25. Selected T1–T6 path

**PATH T6 — AUDIT PIVOT FAILS; END THIS RESEARCH LINE.**

## 26. OT policy

`OT_DEFERRED_FROM_PRIMARY_THEORY` remains unchanged.

## 27. Synthetic policy

`SYNTHETIC_GENERATION_SUSPENDED` remains unchanged.

## 28. Files changed

- `src/survival_ambiguity/audit/hypergeom_bounds.py`
- `src/survival_ambiguity/audit/survival_certificate.py`
- `src/survival_ambiguity/audit/allocation.py`
- `src/survival_ambiguity/audit/__init__.py`
- `tests/test_step07_exchangeable.py`
- `scripts/step07_reference_checks.py`
- `results/step07/exchangeable_checks.json`
- `docs/EXCHANGEABLE_AUDIT_THEORY.md`
- `docs/M6_PRIOR_ART.md`
- `docs/M6_THEOREM_CANDIDATES.md`
- `docs/M6_SUFFICIENCY_TEST.md`
- `docs/M6_DIRECTION_DECISION.md`
- this report

## 29. Tests

`python -m pytest -q` passed: **27 tests**.

## 30. Exact coverage verification

The dedicated script exhaustively checked hypergeometric normalization and confidence-set coverage over all `N=1,...,9`, every `M`, and every audit size `b`, plus representative larger cases.

## 31. Brute-force end-to-end verification

For `N=6,M=2,b=3`, all corruption-location subsets and all audit subsets were enumerated. Corrupted values were fixed adversarial flips; the resulting certificate covered the clean recorded event fraction at probability at least `1-alpha`.

## 32. Deviations

The two-bin pilot and full adaptive-wave development were intentionally not run after the mandatory one-bin kill test failed. No parametric corruption channel, Bernoulli rate, real dataset, neural model, synthetic generator, or OT method was introduced.

## 33. Limitations

The survival channel is one-bin and assumes known `g_h`. Confidence sets are conservative. Allocation results are exact small-population reference calculations, not asymptotic or general optimality theorems. Literature review identifies threats but does not establish exhaustive novelty.

## 34. Recommended Step 08 only

Do not continue this exchangeable-audit line as a primary survival theory. If the broader project continues, begin a separately specified research question only after an independent novelty search; do not silently revive the closed RMST branch or promote these certification compositions as a survival contribution.

## Sources

[1] https://pmc.ncbi.nlm.nih.gov/articles/PMC8715909/
[2] https://pmc.ncbi.nlm.nih.gov/articles/PMC10525037/
[3] https://arxiv.org/abs/1611.02315
[4] https://arxiv.org/html/2604.06116v2
