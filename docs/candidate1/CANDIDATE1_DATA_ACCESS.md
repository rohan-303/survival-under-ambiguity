# Candidate 1 Data Access and Compatibility

## SEER

The official SEER page states that SEER collects cancer incidence data through population-based registries covering approximately 45.9% of the U.S. population, with demographics, primary tumor site, morphology, stage, first-course treatment, and vital-status follow-up.[6] The official access page states that Research Data require registration and a SEER*Stat account, while Research Plus/NCCR data require additional authentication and agreements.[7]

### Site-shift verdict

SEER provides registry/geographic structure in principle, but this gate did not verify that the standard accessible Research Data expose a defensible, harmonized site variable suitable for external validation, nor that cause definitions and treatment/endpoints are identical across registry partitions. Registry partitions could reflect population and ascertainment differences rather than a clean site intervention.

Status: **POTENTIALLY_COMPATIBLE for competing-risk data; UNKNOWN for defensible site-shift construction**.

## MIMIC-IV

The official PhysioNet page describes MIMIC-IV as a deidentified dataset from Beth Israel Deaconess Medical Center, covering ICU and emergency-department admissions, and states that access is credentialed with a data-use agreement and required training.[8] It is one hospital system, even though it contains hospital-wide and ICU data sources.

### Site-shift verdict

MIMIC-IV is not a genuine multi-site external-validation pair by itself. A temporal split would be temporal shift, not site shift. Cause-specific endpoints may be derivable for selected tasks, but this gate did not verify a harmonized multi-cause prognostic cohort with an external site.

Status: **INCOMPATIBLE with the primary site-shift claim as a standalone source**.

## Second external dataset search

A broad search considered oncology registries, transplant cohorts, cardiovascular cohorts, kidney-failure/death cohorts, and ICU outcomes. No second dataset pair with verified compatible cause definitions, comparable index date/horizon, accessible individual-level data, and genuine site separation was established in this gate.

Potential future sources such as restricted registry products or credentialed cohorts remain **UNKNOWN**, not PASS. No data were downloaded.

## Endpoint compatibility table

| Pair | Index date | Cause definitions | Horizon/censoring | Site separation | Status |
|---|---|---|---|---|---|
| SEER registry partitions | potentially available | not audited for exact paired task | not frozen | registry/geography may be available | UNKNOWN |
| MIMIC-IV internal temporal split | available in principle | task-dependent | not frozen | no site separation | INCOMPATIBLE for site claim |
| SEER + MIMIC-IV | not comparable | cancer registry vs acute-care EHR | incompatible populations | nominally different sources | INCOMPATIBLE |
| Restricted oncology/transplant pairs | not inspected at row level | unknown | unknown | possible | UNKNOWN |

## Data Gate assessment

`FAIL` for a PASS-level site-shift project. SEER is plausible but not yet an audited external-site benchmark; MIMIC-IV cannot supply the required multi-site validation alone; and no second compatible pair was verified.

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
