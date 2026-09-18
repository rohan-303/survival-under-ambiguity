# Q4 Step 00 — Delayed-Label Monitoring Gate Report

## 1. Status

`COMPLETE_WITH_WARNINGS — Q4 FAILED`

This was a pre-project kill gate. No model was trained, no large dataset was downloaded, and no conformal method was implemented.

## 2. Starting HEAD

`4a4a291e7e47c41be8a0fb3485cba5d8c1b43307`

Preflight passed on `main`, origin/upstream were correct, `git pull --ff-only` succeeded, and the worktree was clean.

## 3. Q4 question

At a fixed monitoring time, when labels have matured for a selected and subgroup-dependent subset of prior predictions, under what assumptions is subgroup-conditional selective risk identifiable, and what minimum randomized or holdout design is required when it is not?

## 4. Selective-risk target

Fix `A=1` as accepted/acted-on predictions and `G=g` as a prespecified subgroup. The target is `R_g=E[l(f(X),Y)|G=g,A=1]`; optional secondary target is subgroup coverage conditional on `G=g,A=1`. The deployment cohort is frozen before inspecting label maturity.

## 5. Label-maturation model

`D` is time to label observability and `R(u)=1{D<=u-s}`. M0 is fixed delay; M1 is conditionally noninformative maturation; M2 is outcome-dependent maturation; M3 permits permanent missingness. Delayed-but-eventually-observed labels must not be conflated with selectively observed labels.

## 6. M0 result

M0 is stale feedback, not a fundamental identification problem if all labels eventually arrive. It is occupied by delayed-feedback methods and insufficient as novelty.

## 7. M1 result

Under `R independent of Y | X,G,A`, inverse-probability-of-maturation weighting identifies `R_g` under positivity and correct/consistent maturation propensities. Unequal subgroup maturity reduces effective sample size. This is standard MAR machinery.

## 8. M2 result

If `R` depends on `Y` after conditioning on `X,G,A`, the naïve monitor can be arbitrarily misleading and risk is not point identified without restrictions. A two-population construction shares observed `(R,RY)` masses but has true risks 0.1 versus 0.6. This is standard MNAR nonidentification.

## 9. M3 result

Permanent missing labels are at least as difficult. Bounds, sensitivity parameters, validation samples, or randomized acquisition are needed. No Q4-specific result survived.

## 10. Naïve-monitor bias and false-safe example

Two groups can have equal true selective risk 0.2. If group-0 errors mature at probability 0.1 while correct labels mature at 0.9, its observed error rate is `2/(72+2)=0.027`; group 1 with equal 0.9 maturity has observed rate 0.2. The monitor falsely declares group 0 safer. Reversing the maturation mechanism reverses the apparent ranking. This is elementary label-selection bias.

## 11. Delayed ACI 2026 comparison

El Halabi and Brandt study delayed adaptive conformal inference for fixed-horizon forecasts. Their recursion decomposes into interleaved ACI-like sequences and yields finite-sample long-run coverage bounds depending on delay; they also introduce a delay-to-memory ratio. The core feedback is delayed but ultimately observed. Their result covers M0 and much of M1, not outcome-dependent or permanently missing clinical labels.[1]

## 12. Conditional-conformal comparison

Conditional, Mondrian, weighted, and risk-coverage conformal methods already address prespecified subgroup validity, approximate conditional guarantees, and selective prediction. Running them separately by group does not make Q4 novel. Their usual assumptions do not automatically resolve selected maturation.

## 13. Clinical selective-prediction comparison

Clinical conformal/selective prediction work addresses risk-coverage, subgroup or shift-aware weighting, deferral, and calibration when evaluation labels are available. Q4's proposed distinction is label maturation at the monitoring cutoff. No verified clinical theorem was found that converts this distinction into a novel guarantee.

## 14. Corbin label-selection comparison

Corbin, Baiocchi, and Chen study biased clinical model performance estimates when only a subset of labels is observed. They describe three label-selection classes, simulate distinct mechanisms, show naïve discrimination/calibration failure, use weighting when selection probabilities are specified, and discuss injected randomization for deployment monitoring.[2] This substantially covers Q4's M1/M3 label-selection core and random-adjudication remedy.

## 15. Selective-label comparison

Selective labels are outcomes observed only for policy-selected cases; delayed labels are eventually observed later. Q4's M2/M3 regimes combine these familiar issues. The combination is not itself a contribution.

## 16. Random-adjudication result

Randomly adjudicating unresolved cases with positive probability within each subgroup restores identification under consistency, positivity, and a valid reference standard. This is a known randomized-validation design and is adjacent to Corbin et al. Positive probability establishes asymptotic identification, not a new finite-sample minimum-rate theorem.

## 17. Holdout result

A shadow-mode or randomized holdout arm can supply labels under a reference policy. This is ordinary randomized exploration/withholding. It may be the correct deployment design, but no Q4-specific novelty was established.

## 18. Delayed-conformal selective-feedback result

If feedback arrival depends on score, action, subgroup, or outcome, adaptive conformal updates observe a selected error stream. Delay-only ACI bounds cannot be transferred automatically. A correction would require known/estimated feedback propensities, randomized validation, or sensitivity bounds. This is the strongest open direction, but it remains threatened by generic online learning with partial feedback and MNAR conformal theory.

## 19. Subgroup-specific result

Subgroups create unequal maturity, selection, and effective sample sizes. Simultaneous subgroup monitoring requires ordinary stratification, multiplicity control, or concentration methods. No nontrivial subgroup theorem beyond those tools was established.

## 20. Data feasibility

MIMIC-IV and eICU-CRD can support a declared protocol benchmark using retrospective timestamps and reconstructed outcome windows. They do not contain complete model prediction, alert, clinician response, or deployment label-maturation logs. Pathology, readmission, adverse-event, and specialist-diagnosis labels are plausible delayed outcomes, but a faithful public deployment dataset was not verified.

## 21. Strongest theorem candidate

T3—selectively observed delayed conformal feedback—is the only potentially load-bearing direction. T1 (M0–M3 identification), T2 (random acquisition), and T4 (simultaneous subgroup safety) are known or compositional. T3 was not proved novel or clinically identifiable.

## 22. Strongest prior-art threat

Corbin et al. for label selection and randomized validation; El Halabi & Brandt for delayed adaptive conformal inference; generic MNAR, selective-label, and partial-feedback online-learning theory for the remaining interaction.

## 23. Gates

- **Delayed-Feedback Gate D:** `CONDITIONAL`
- **Label-Selection Gate L:** `FAIL`
- **Subgroup Gate G:** `CONDITIONAL`
- **Identifiability Gate I:** `CONDITIONAL`
- **Data Gate:** `CONDITIONAL`
- **Novelty Gate N-Q4:** `FAIL`
- **Sufficiency Gate S-Q4:** `CONDITIONAL`

## 24. Exact surviving contribution

None established.

Existing work establishes delayed adaptive coverage under ultimately observed feedback and biased clinical evaluation under selected labels, whereas Q4 would need to establish a sharp identification or randomized-design boundary for subgroup selective risk under outcome-selective delayed feedback. That boundary was not derived and remains generic in the bounded search.

## 25. Master decision

**`Q4-G — FAIL FOR MULTIPLE REASONS`**

`NO_AUTOMATIC_NEXT_CANDIDATE`

## 26. Files created

- `docs/q4/Q4_PRIOR_ART.md`
- `docs/q4/Q4_THEORY_PREFLIGHT.md`
- `docs/q4/Q4_DELAYED_CONFORMAL_KILL_TEST.md`
- `docs/q4/Q4_LABEL_SELECTION_KILL_TEST.md`
- `docs/q4/Q4_CLINICAL_DATA_FEASIBILITY.md`
- `docs/q4/Q4_THEOREM_CANDIDATES.md`
- `docs/q4/Q4_SUFFICIENCY_TEST.md`
- `docs/q4/STEP00_Q4_DECISION.md`
- `reports/Q4_STEP00_DELAYED_LABEL_MONITORING_GATE_REPORT.md`
- `discovery/q4/q4_checks.py`

## 27. Commands/checks

The tiny checks cover naïve subgroup bias, an MAR-weighting structural check, an MNAR observational-equivalence construction, and positive-probability random adjudication. Archived repository tests, compilation, and diff checks are run before commit.

## 28. Deviations

The supplied instruction names a 2026 clinical selective-prediction source without a stable title/identifier. A bounded bibliographic search did not produce a unique primary record, so no unsupported details were assigned to it. The directly verified delayed-ACI preprint and Corbin et al. were used as the principal threats.

## 29. Limitations

The MNAR construction is an elementary identifiability example. No clinical deployment log, randomized withholding trial, or actual delayed-label monitoring stream was available. The data feasibility result is therefore a protocol-level assessment, not a deployment validation.

## 30. Recommended next step only

Do not implement Q4 and do not start Q9 or Q10 automatically. Decide separately whether either finalist merits a new kill gate.

## Sources

[1] https://arxiv.org/abs/2609.07251
[2] https://pubmed.ncbi.nlm.nih.gov/37350883
