# Candidate 2 Data Access

## EBMT / `calibmsm` example

The `calibmsm` example data are distributed with the package and via a public figshare record.[2][10] The example includes a transplant multistate structure with recovery, adverse events, relapse, and death in the worked example.[2] It is suitable for reproducing calibration tooling, not for proving external site validation: the example is one package-level cohort and no independent site pair was verified.

Status: **COMPATIBLE for method reproduction; INSUFFICIENT for external-validation gate**.

## MIMIC-IV

MIMIC-IV is credentialed and comes from Beth Israel Deaconess Medical Center.[6] It can support longitudinal state definitions only after a clinically justified state graph and ascertainment contract are frozen. It is a single health system, so it cannot alone provide external site validation.

Status: **POTENTIALLY_COMPATIBLE for internal multistate development; INSUFFICIENT for external pair**.

## eICU-CRD

eICU-CRD is a credentialed, multi-center ICU database with over 200,000 admissions, 335 units, and 208 hospitals.[7] However, hospital and unit identifiers were removed, and the database documentation warns that interfaces differ across units. This supports multi-center data but complicates a defensible site label, state ascertainment, and harmonized external split.

Status: **POTENTIALLY_COMPATIBLE for multi-center development; UNKNOWN for a clean external validation pair**.

## Dataset pair assessment

| Pair | State graph compatibility | External site | Access | Verdict |
|---|---|---|---|---|
| `calibmsm` example + MIMIC-IV | Different population/state contract | yes in principle, not harmonized | package public + credentialed | `INCOMPATIBLE` |
| MIMIC-IV + eICU-CRD ICU states | Not yet harmonized; timestamp/interface differences | nominally different sources | both credentialed | `UNKNOWN` |
| eICU internal units/hospitals | Hospital/unit IDs removed | not defensibly identified from official page | credentialed | `UNKNOWN` |
| EBMT-style transplant cohort pair | Not found and not audited | unknown | unknown | `UNKNOWN` |

## Data Gate assessment

`CONDITIONAL` at best, but no PASS-level pair was verified. The most plausible future pair is MIMIC-IV plus eICU-CRD for a carefully specified ICU state graph, yet endpoint/state compatibility, site labeling, and transition observability remain unresolved. No data were downloaded.

Sources consulted: [1][2][3]. Additional sources: [4][5][6]. Dataset sources: [7][8]. Comparator sources: [9][10].

## Sources

[1] https://doi.org/10.1002/sim.10094 — Pate et al. 2024 calibration plots
[2] https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0320504 — Pate et al. 2025 calibmsm
[3] https://cran.r-project.org/package=calibmsm — CRAN calibmsm
[4] https://doi.org/10.1002/bimj.201600191 — Spitoni et al. prediction errors
[5] https://cran.r-project.org/package=mstate — CRAN mstate
[6] https://physionet.org/content/mimiciv/3.1 — MIMIC-IV
[7] https://physionet.org/content/eicu-crd/2.0 — eICU-CRD
[8] https://doi.org/10.1002/sim.2712 — Putter et al. 2007 multistate
[9] https://pmc.ncbi.nlm.nih.gov/articles/PMC11521377 — Competing-risk decision analysis
[10] https://figshare.com/articles/dataset/Data_required_for_running_vignettes_with_calibmsm_R_package/27635844 — calibmsm example data
