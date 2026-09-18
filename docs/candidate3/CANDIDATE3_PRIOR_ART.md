# Candidate 3 — Prior-Art Matrix

## Matrix

| Citation | Year | Prediction/inference | Visit process | Measurement process | Counts/masks | Event outcome | External shift | Intervention | Joint model | Model-agnostic diagnostic | Exact overlap / remaining gap |
|---|---:|---|---|---|---|---|---|---|---|---|---|
| Sisk et al., DOI 10.1093/jamia/ocaa242 | 2021 | Prediction review | Yes | Yes | Yes | Mixed | Discussed | No | Reviews methods | No | Establishes informative presence/observation and recommends using process information; no policy intervention certificate. |
| Jeanselme et al., DeepJoint, arXiv:2205.13481 | 2022 | Prediction | Yes | Yes | Longitudinal, inter-observation, missingness | Survival | Weekday/weekend | No | Yes | No | Directly establishes clinical-presence shift and more robust joint modeling; no arbitrary-pretrained-model diagnostic or physiology-policy identification. |
| Zamanian et al., DOI 10.3390/jpm14050514 | 2024 | Methodological/prediction analysis | Indirect | Yes | Ten missingness scenarios | Observational health data | Deployment scenarios | Policy causes discussed | No single joint model | No | Establishes physician, patient, facility, and recording mechanisms as distinct missingness sources and calls for domain-informed sensitivity analysis. |
| Pate et al./Jeanselme clinical-presence line | 2022–2026 | Prediction | Yes | Yes | Yes | Survival | Yes | Not a passive intervention | Joint approaches | No | Occupies the core claim that care-process features improve internal prediction and can shift transportability. |
| Yamamoto et al., medRxiv DOI 10.64898/2026.04.05.26350209 | 2026 | Prediction | Partly | Yes | Counts and summaries | Sepsis mortality | MIMIC-IV to eICU-CRD | No | Logistic/boosted models | No | Directly tests the proposed count-feature domain-shift failure: >60,000 patients, internal AUROC improvement and larger external degradation for complex observation summaries. |
| Missing-data / MNAR and joint-observation literature cited by Sisk | Before 2021 | Inference and prediction | Yes | Yes | Yes | Mixed | Sometimes | Sometimes | Yes | No | Policy-dependent observation and support/positivity limits are established statistical problems. |
| Generic invariance, shortcut, and stress-test literature | Ongoing | Prediction | Domain-dependent | Domain-dependent | Perturbations | Mixed | Yes | Often synthetic | Sometimes | Yes | A paired perturbation score alone is not a new healthcare contribution. |

## Top five novelty threats

1. DeepJoint’s explicit clinical-presence shift and weekday/weekend transfer experiment.
2. Sisk et al.’s review of informative presence and informative observation as prediction signal.
3. Yamamoto et al.’s 2026 MIMIC-IV/eICU study, which directly reports observation-feature transport degradation.
4. Domain-informed missingness and MNAR analyses, including Zamanian et al.
5. Generic invariant prediction, missingness perturbation, and shortcut-learning diagnostics.

## Broad-hypothesis verdict

`YES — SUBSTANTIALLY ESTABLISHED.` The claim that visit or laboratory-order patterns improve internal prediction and can fail after care-process change is not a new research question.

The only authorized refinement—controlled observation-policy intervention for a pretrained model—remains unoccupied only in a narrow, conditional sense. Its identification and information-loss problems were not solved here.

## Source limits

The exact title “Prediction of Survival Outcomes under Clinical Presence Shift: A Joint Neural Network Architecture” was not independently matched in the bounded bibliographic sources. The directly verifiable DeepJoint preprint already covers the asserted overlap. No claim is made about an unmatched version.
