# Candidate 3 — Clinical-Presence Kill Test

## Result

The original hypothesis is **YES — SUBSTANTIALLY ESTABLISHED**. It fails as a fresh candidate.

DeepJoint defines clinical presence through longitudinal timing, inter-observation time, test-order/missingness patterns, and observed values, and models these jointly with survival. Its weekday/weekend experiment is already an observation-process shift test. The paper also reports that simple count features can be especially vulnerable to covariate shift.

Sisk et al. review the same phenomenon under informative presence and observation, including missing indicators, summary measures, observation times, inter-observation time, frequency, joint models, and latent structures.

The 2026 MIMIC-IV/eICU-CRD preprint is an even closer empirical overlap. Its abstract reports more than 60,000 records, count and physiologic-summary feature sets, internal AUROC gains from richer summaries, larger external AUROC degradation, and progressively worse external calibration. That directly establishes the proposed broad failure mode, not merely a related workflow observation.

## What remains distinct?

A passive-policy intervention diagnostic for an already-trained arbitrary model could be distinct from ordinary external validation if it were identifiable, information-matched, and actionable. No such result was established. The proposed paired record manipulation either removes information or changes legitimate temporal meaning; a prediction change is therefore not a certificate of shortcut reliance.

## External calibration comparison

External calibration can reveal that transport failed. A policy perturbation could, in principle, attribute failure to a visit or measurement mechanism before target labels arrive. But unlabeled process drift alone does not identify outcome degradation, and a source-only perturbation does not reproduce the target policy without overlap and mechanism assumptions.

## Verdict

Do not revive Candidate 3’s broad question. The remaining refinement is too conditional for a project-selection pass.
