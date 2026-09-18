# Candidate 3 — Data and Natural-Experiment Gate

## MIMIC-IV and eICU-CRD

Both are credible critical-care sources with access requirements and different schemas. The 2026 preprint already uses them for the central observation-feature/domain-shift comparison. Repeating that pair would not be a distinct experiment. Harmonized physiology, timestamp semantics, site definitions, outcome windows, and leakage controls would still be required.

## Other candidates

MIMIC-IV plus HiRID or AmsterdamUMCdb could provide external comparison, but compatible outcome and measurement definitions, access, and policy labels were not verified in this gate. eICU hospital identifiers may support internal site comparisons, but availability and usable measurement-policy labels were not established from the bounded source check. MIMIC temporal eras do not by themselves identify a policy change; extraction, coding, case-mix, and treatment changes confound interpretation.

## Natural policy change

No documented, accessible laboratory-order or monitoring-policy natural experiment with stable population, known intervention date, and adequate pre/post overlap was verified. A weekday/weekend contrast is already used by DeepJoint and is not a policy-identifying natural experiment.

## Decision

`CONDITIONAL` at most. The final candidate has no verified data configuration that is both distinct from published MIMIC/eICU work and capable of identifying a passive policy effect.
