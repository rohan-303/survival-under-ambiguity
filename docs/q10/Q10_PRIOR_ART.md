# Q10 Prior-Art Matrix

| Citation | Clinical text? | Temporal shift? | Semantic shift? | Unlabeled target? | Downstream task/performance | Label-free estimate | Early warning | Exact overlap / remaining gap |
|---|---:|---:|---:|---:|---|---:|---:|---|
| SUDO (Kiyasseh et al.)[1] | Yes | Not primary | No semantic mechanism required | Yes | Clinical-note example; unreliable predictions, model selection, bias assessment | Yes | Operationally possible, but not a temporal lead-time study | Directly threatens label-free performance monitoring; Q10 must add a validated semantic-specific advantage. |
| Clinical-ShiftEval[2] | Yes | Yes | Simulated/dynamic task shifts | Yes/partly | Adaptation benchmark with measured downstream metrics | Not its central claim | No verified pre-label warning claim in the accessible record | Threatens benchmark novelty; label-free early warning remains the only possible gap. |
| Pediatric anxiety semantic drift[3] | Yes | Yes | Yes | Not necessarily | Semantic meaning changes in EHR terminology | No | No | Establishes semantic drift, not task-failure warning; Q10 would need downstream prediction. |
| SIReNs / Interpreting Dataset Shift in Clinical Notes | Yes | Reported target | Shift explanation | Yes | Shift characterization and explanation | Not established here | Not established here | Exact paper was not independently retrievable in this gate; treat title-level overlap as a threat, not as verified scope. |
| MIMIC-IV-Note[4][5] | Yes | Multi-era notes | Potentially | Labels depend on task construction | Public clinical text resource | No | No | Feasible substrate, but credentialed access, deidentification artifacts, and task-label consistency constrain the design. |
| Unsupervised domain adaptation theory[6] | Generic | Generic | Representation-agnostic | Yes | Shows target risk is not generally identified from unlabeled target covariates | No | No | Establishes the impossibility boundary; semantic scores require extra assumptions. |
| Generic clinical semantic-drift study[7] | Yes/clinical context uncertain | Yes | Yes | Variable | Drift measurement rather than performance warning | No | No | Further reduces novelty of a standalone semantic-drift statistic. |

## Gate interpretation

The matrix does not establish that Q10 is impossible. It establishes that semantic drift measurement and label-free clinical-AI evaluation are separately occupied. The load-bearing claim would have to be a task-specific, prospective warning result that beats SUDO and uncertainty baselines, not another drift metric.

## Search boundary

Retrieved primary/official pages and DOI landing pages on 2026-09-18. Search results for SIReNs and the exact Vaez-Ghaemi title were incomplete; the report therefore does not claim comprehensive absence or verified details for that work.
