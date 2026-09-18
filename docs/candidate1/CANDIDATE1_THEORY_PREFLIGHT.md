# Candidate 1 Theory Preflight

## Formal setting

For causes `k=1,...,K`, define `F_k(t|x)=P(T<=t,J=k|X=x)` and `F_all(t|x)=sum_k F_k(t|x)`. When `F_all>0`, the allocation vector is `a_k=F_k/F_all`. This is a descriptive decomposition, not a new estimand by naming alone.

## Elementary cancellation

The tiny discovery script constructs predicted `(0.30,0.20)` and true `(0.05,0.45)`. Both have all-cause risk `0.50`, but the cause-specific vectors differ. Their allocation vectors are `(0.60,0.40)` and `(0.10,0.90)`. Therefore aggregate risk alone does not identify cause allocation.

Status: **ELEMENTARY**.

## Elementary calibration counterexample

A population can be partitioned into groups with errors in opposite cause directions while the all-cause sum remains calibrated. Thus all-cause calibration-in-the-large does not imply cause-specific calibration. This is probability-vector algebra and does not support novelty.

Status: **ELEMENTARY / KNOWN**.

## Decision reversal

Use abstract actions A and B, where action A incurs loss equal to cause-2 risk and action B incurs loss equal to cause-1 risk. Under the predicted vector `(0.30,0.20)`, A is preferred; under the true vector `(0.45,0.05)`, B is preferred, despite equal all-cause risk. More generally, any action utility that weights causes differently can reverse under fixed `F_all` whenever the allocation crosses the action boundary.

Status: **ELEMENTARY decision theory**.

## Temporal crossing

The script uses early CIF `(0.24,0.06)` and late CIF `(0.06,0.24)`: the total is `0.30` at both horizons while the dominant cause changes. This demonstrates that time structure can matter, but it does not establish that existing time-dependent competing-risk validation misses it.

Status: **ELEMENTARY / OPEN as a validation-gap question**.

## Hidden-failure set

A set constrained only by all-cause calibration or all-cause Brier performance permits large cause allocation variation. Adding standard cause-specific calibration and joint proper scores should sharply reduce the feasible set. The useful theorem, if any, would need to state a nontrivial bound from a specified validation contract to decision regret. No such bound was established here.

Status: **OPEN, not computed**.

## Proper-scoring-rule kill test

The full CIF/event-free vector is a categorical probability vector at a fixed horizon. Joint proper scores therefore respond to cause misallocation even when the sum is preserved. This kills any claim that cause allocation is invisible to all standard validation. The remaining issue is practice-level metric omission, which is an evaluation critique rather than a new mathematical result.

Status: **KNOWN / candidate weakened**.

## Theorem gate assessment

`CONDITIONAL` at most. The cancellation, calibration, and decision reversal results are elementary. A non-elementary theorem connecting all-cause/cause-specific validation tolerances to time-dependent action regret remains unproved and must survive the existing literature.

## Discovery script

`discovery/candidate1/elementary_checks.py` is intentionally tiny and non-reusable. It contains only assertions for cancellation, abstract action reversal, and a time-varying allocation crossing.

Sources consulted: [1][2][3]. Additional sources: [4][5][6]. Dataset sources: [7][8]. Comparator sources: [9][10].

## Sources

[1] https://europepmc.org/api/getPdf?pmcid=PMC12519608 — Mozumder et al. 2025 full text
[2] https://www.bmj.com/content/377/bmj-2021-069249 — van Geloven et al. 2022
[3] https://link.springer.com/article/10.1186/s41512-021-00114-6 — Austin et al. 2022 calibration curves
[4] https://pmc.ncbi.nlm.nih.gov/articles/PMC10946485 — Temporal recalibration
[5] https://pmc.ncbi.nlm.nih.gov/articles/PMC11521377 — Competing-risk decision analysis
[6] https://seer.cancer.gov/data — SEER data
[7] https://seer.cancer.gov/data/access.html — SEER access
[8] https://physionet.org/content/mimiciv/3.1 — MIMIC-IV
[9] https://proceedings.mlr.press/v209/jeanselme23a/jeanselme23a.pdf — Neural Fine-Gray
[10] https://proceedings.mlr.press/v193/hu22a.html — Distributionally robust survival
