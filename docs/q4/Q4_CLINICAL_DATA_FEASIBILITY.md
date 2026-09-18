# Q4 Clinical Data Feasibility

## Outcome processes

| Outcome | Prediction time | Maturation mechanism | Outcome-dependent availability? | Active acquisition? | Feasibility |
|---|---|---|---|---|---|
| 30-day mortality | discharge or index prediction | registry/death record after follow-up | possible loss to follow-up; not directly represented in routine ICU tables | registry linkage/adjudication in principle | protocol benchmark only |
| Readmission | discharge | requires future encounter window | follow-up and health-system capture vary | chart/registry linkage | retrospective reconstruction, not true deployment |
| Pathology confirmation | biopsy/specimen time | laboratory/pathology reporting | urgent/severe cases may return sooner | chart review possible | potentially relevant, access unresolved |
| Adverse drug event | treatment/index encounter | later documentation or adjudication | reporting and follow-up selective | chart review possible | high data-governance risk |
| Specialist diagnosis/recurrence | index/referral | later specialist contact | strongly follow-up dependent | adjudication/registry possible | not supported by MIMIC alone |

## MIMIC-IV and eICU-CRD

Official sources provide retrospective clinical timestamps, outcomes, and treatment-related fields, but not actual model prediction issuance, alert, clinician response, or deployment label-maturation logs. They can support a synthetic/protocol benchmark where a delay and selection mechanism is explicitly declared. They cannot establish a real deployment monitoring effect.

## Best protocol

A theory-led simulation with known eventual `Y`, `D`, `R`, `G`, and `A`, plus a retrospective MIMIC/eICU illustration using reconstructed outcome windows. The illustration must not be called real post-deployment validation.

## Data gate result

`CONDITIONAL`: a protocol benchmark is feasible; a clinically faithful label-maturation dataset with model-mediated selection was not verified.
