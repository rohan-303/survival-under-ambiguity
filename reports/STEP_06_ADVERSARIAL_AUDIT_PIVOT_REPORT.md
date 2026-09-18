# STEP 06 — ADVERSARIAL AUDIT PIVOT REPORT

## 1. Final status

**COMPLETE_WITH_WARNINGS**

The hard pivot was evaluated without modifying the closed RMST theory branch. The audit oracle, V-P/V-F distinction, targeted validation-design literature review, exact finite-population post-audit interval, unrestricted-adversary impossibility witness, brute-force verifier, and pivot gate decision were completed. A positive survival-specific audit-allocation theorem was not established.

## 2. Starting HEAD

- Repository: `C:/Users/rohan/survival-under-ambiguity`
- Starting HEAD: `99994156090de0019d616a1c1e945ab08f20f727`
- Branch: `main`
- Remote: `https://github.com/rohan-303/survival-under-ambiguity.git`
- Starting worktree: clean and aligned with `origin/main`
- `git pull --ff-only`: passed; already up to date.

## 3. Why Step 05 forced a pivot

The apparent RMST coupling gap was caused by comparing an unweighted sum of pointwise widths with an RMST width. Correct RMST weighting removed the gap in the corrected case and in the deterministic phase study. The joint-RMST branch was therefore closed rather than rescued.

## 4. Prior-art kill test

Classical contaminated/corrupted-data identification, survival validation subsets, right-censored outcome misclassification validation, two-phase survival designs, multiwave EHR validation, and semi-verified learning all overlap with broad versions of the new idea. The remaining possible distinction is narrow: an exact minimax finite-population theorem for auditing clean recorded tuples under arbitrary row corruption while explicitly preserving censoring loss.

Key sources are recorded in `docs/M5_PIVOT_PRIOR_ART.md`, including Horowitz–Manski, Magaret/Xie 2008, Giganti et al. 2018, Han et al. 2021, multiwave validation work, and semi-verified learning.

## 5. Audit oracle definition

An audit returns `Z_i*=(G_i,Y_i,Delta_i)` where `Y_i=min(T_i,C_i)` and `Delta_i=1{T_i<=C_i}`. It does not reveal latent `T_i` beyond censoring. The implementation stores only `(group,y_bin,delta)` and has no post-censoring event-time field.

## 6. V-P model

V-P is a population/stratified validation model connected to classical two-phase validation. It requires a probability, exchangeability, or error-channel assumption to transfer validation results to unvalidated records. It was not developed as the primary model.

## 7. V-F model

V-F has `n` observed recorded tuples, unknown clean tuples, at most `m` arbitrary row corruptions, and an audit set of size at most `B` returning clean recorded tuples. The primary target is the clean recorded event fraction; a one-bin survival-channel translation is separate and does not undo censoring.

## 8. Selected primary model

**V-F — finite-population adversarial audit model.** It provides deterministic sharp intervals and exact enumeration without importing estimator-efficiency assumptions. V-P remains secondary prior art.

## 9. No-audit baseline

For binary recorded event indicators, with no audits the clean event count can differ from the observed count by up to the corruption budget, subject to the `[0,n]` bounds. This is a finite-population analogue of the prior contamination baseline and is not claimed as new.

## 10. Does auditing help under unrestricted corruption?

It can reduce the realized interval, especially when an audited discrepancy consumes corruption budget. But under the worst-case criterion, any policy with `B<n` and `m>=1` leaves a positive ambiguity witness: all observed/audited records can be censored while one unaudited record may be either clean event or clean non-event. A universal zero-width guarantee requires full audit.

## 11. Minimal transfer assumption

A positive nontrivial audit-design theorem requires a link from audited to unaudited records: random corruption locations, exchangeability, stratum-level error rates with a valid update rule, or a known/bounded error channel. An upper corruption cap alone does not make an audited clean record evidence that unaudited records are clean.

## 12. One-record audit result

For an observed population, let `d_A` be audited discrepancies, `m'=m-d_A`, and let `u_1,u_0` be unverified observed event/non-event counts. The exact post-audit clean-event interval is:

`[audited_clean_events + u_1 - min(u_1,m'), audited_clean_events + u_1 + min(u_0,m')] / n`.

The result is sharp by direct construction and agrees with brute-force enumeration for all tested cases.

## 13. One-bin post-audit identification

If a separately declared known follow-up channel gives recorded event probability `r=g p`, the recorded interval maps to `[lower/g, upper/g]`. This is a channel transformation only. Auditing never reveals the unobserved event time of a censored record.

## 14. Audit sample complexity

For unrestricted V-F and target width zero, `B*=n` in the worst case whenever `m>=1`. For nonzero width targets, the exact realized formula gives the required budget conditional on the audit outcome, but no universal survival-specific sample-complexity theorem was established.

## 15. Decision stability

No separate threshold theorem was promoted. A threshold such as `S_g(t)>c` can be evaluated from the post-audit interval once a valid transfer/channel model is specified. Under unrestricted V-F, a small audit cannot universally certify a latent survival decision because recorded corruption and censoring remain unresolved.

## 16. Rare-group result

No minimax rare-group allocation rule was established. Without a transfer assumption, subgroup rarity does not justify auditing that subgroup: the adversary can leave ambiguity in any unaudited group. Any future rule must combine stratum size, corruption uncertainty, and follow-up while respecting residual censoring.

## 17. Censoring-versus-audit interaction

The oracle distinction establishes a one-sided fact: audit corrects recorded corruption but not censoring. A positive monotone or nonmonotone audit-value theorem under heavier censoring remains open. No unsupported claim that rare/heavily censored records should receive more audits was made.

## 18. Adaptive-vs-nonadaptive result

Under the unrestricted worst-case model, adaptivity does not defeat the basic witness: an adversary can preserve audited outcomes while leaving an unaudited ambiguity. A positive adaptive advantage requires a random-location, exchangeability, or error-channel assumption. No adaptive theorem was claimed.

## 19. K=2 findings

K=2 latent survival was not expanded into a separate censoring LP because the unrestricted V-F impossibility already appears at the binary recorded-event level. The implementation remains compatible with adding two event bins once a transfer assumption is frozen.

## 20. Classical validation-design comparison

Classical validation work optimizes estimator variance, likelihood efficiency, bias, or MSE under stochastic measurement-error models. The V-F candidate optimizes worst-case identified width under arbitrary corruption. This objective difference is real, but existing validation and robust-data literatures make broad novelty claims unsafe.

## 21. Strongest theorem candidates

V1, unrestricted-adversary audit impossibility, is the strongest currently supported candidate. V3, the exact realized post-audit interval, is checked but elementary. V2/V5/V6/V7/V8 require a minimal transfer model and remain open.

## 22. Pivot Theory Gate V

**CONDITIONAL.** The finite-population impossibility boundary is exact, falsifiable, and practically relevant as a guardrail. Its core logic is not yet demonstrably survival-specific, and positive audit design remains unresolved.

## 23. Novelty Gate N

**CONDITIONAL.** Existing partial-identification, survival-validation, multiwave-design, and semi-verified-learning work creates substantial threats. The narrow recorded-tuple minimax theorem remains unverified against all exact overlaps.

## 24. Sufficiency Gate S

**CONDITIONAL.** The result would prevent overclaiming from small audits, but it does not yet give a positive audit-allocation rule that would change practice.

## 25. Selected direction

**PATH V2 — AUDIT IMPOSSIBILITY / MINIMAL-ASSUMPTION THEORY BECOMES PRIMARY.** The next valid question is which weakest transfer assumption makes audited censored records informative about unaudited records.

## 26. OT policy

`OT_DEFERRED_FROM_PRIMARY_THEORY`.

## 27. Synthetic-generation policy

`SUSPENDED_UNTIL_NEW_CORE_PASSES`.

## 28. Files changed

- `docs/PIVOT_HISTORY.md`
- `docs/ADVERSARIAL_AUDIT_MODEL.md`
- `docs/M5_PIVOT_PRIOR_ART.md`
- `docs/M5_THEOREM_CANDIDATES.md`
- `docs/M5_SUFFICIENCY_TEST.md`
- `docs/M5_DIRECTION_DECISION.md`
- `src/survival_ambiguity/audit/models.py`
- `src/survival_ambiguity/audit/__init__.py`
- `tests/test_step06_audit.py`
- `scripts/step06_reference_checks.py`
- `results/step06/audit_checks.json`
- this report

## 29. Tests

- `git pull --ff-only` — passed.
- `python scripts/step06_reference_checks.py` — passed; 20 exact policy/budget rows generated.
- `python -m pytest -q` — passed, 20 tests.
- `python -m compileall -q src scripts tests` — passed.
- `git diff --check` — passed.

## 30. Brute-force verification

The closed-form post-audit interval matched exhaustive clean-record enumeration for every tested tiny population. Cases covered `n=3,4,5`, `m=1,2`, `B=0,...,n`, corruption discovery, verified-clean records, rare-group records, and full-audit zero width. The reference output is `results/step06/audit_checks.json`.

## 31. Deviations

- V-P was not implemented beyond definition and literature comparison because V-F provides the cleaner impossibility preflight.
- No positive transfer assumption was selected prematurely.
- No adaptive, randomized, or K=2 positive-design theorem was forced after the unrestricted impossibility result.

## 32. Limitations

The finite-population result targets clean recorded-event fractions, not a finite-sample estimator of latent survival. Translating to `S(t)` requires a declared censoring channel and does not recover censored future event times. The project has not established a positive minimax audit-allocation theorem, rare-group rule, censoring-value theorem, or novelty guarantee.

## 33. Recommended Step 07 only

Freeze one minimal transfer assumption—preferably an explicitly specified stratum-level stochastic corruption model—and test whether it yields a genuinely survival-specific minimax audit theorem. If it reduces to standard two-phase validation efficiency, stop this pivot. Do not begin Step 07 automatically.
