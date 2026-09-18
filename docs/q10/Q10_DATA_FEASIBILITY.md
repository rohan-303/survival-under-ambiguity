# Q10 Data Feasibility

## Best candidate

MIMIC-IV-Note is the strongest accessible substrate for a temporal clinical-text protocol. It contains deidentified discharge summaries and radiology reports linkable to MIMIC-IV.[4][5] The published resource reports 331,794 discharge summaries from 145,915 patients and 2,321,355 radiology reports from 237,427 patients.[5]

## Recommended task

A fixed discharge-summary phenotype/document classification task is preferable to NER or coding for Step 00 because longitudinal evaluation can preserve a document-level metric and avoid token-level annotation scarcity. The task label would need to be frozen from structured fields or an existing validated annotation protocol before any experiment.

## Blockers

- Files require credentialed PhysioNet access and a data-use agreement.[5]
- Deidentification placeholders and changing note templates can look like semantic drift without representing clinical concept change.
- A single hospital does not separate temporal from site shift.
- The task label may change with documentation practice, creating concept/label drift rather than pure semantic drift.
- No data were downloaded and no task labels were inspected in this gate.

**Data Gate:** `CONDITIONAL`, not `PASS`.
