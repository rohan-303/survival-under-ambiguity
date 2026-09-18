# M5 theorem candidates

| Candidate | Assumptions | Proof status | Novelty threat | Scientific meaning | Survival specificity | Practical plausibility |
|---|---|---|---|---|---|---|
| V1 — unrestricted-adversary audit impossibility | V-F; at most `m>=1` arbitrary row corruptions; audit returns clean recorded tuples; `B<n` | Exact binary finite-model derivation and brute-force checked | Horowitz–Manski and generic trusted/untrusted robustness | A finite audit cannot guarantee exact recovery when corruption can hide outside audited records | Censoring is preserved, but core impossibility is generic | High as a negative theorem |
| V2 — minimal transfer assumption | Need a link from audited to unaudited records | Open | Two-phase validation and semi-verified learning | Identifies what must be assumed before audits can inform unaudited records | Could be survival-specific only through censoring channel | High conceptual value, theorem incomplete |
| V3 — sharp one-bin post-audit width | Binary recorded event/censor indicator; known `m`; fixed audit outcome | Derived and brute-force checked | Generic finite-population corruption accounting | Exact realized audit gain | Follow-up translates recorded width but auditing does not reveal latent `T` | High but elementary |
| V4 — audit sample complexity | Width target `delta`; V-F worst-case | In unrestricted model, exact zero-width requires `B=n`; nonzero target formula remains elementary | Generic active verification | How much review is required for certification | Survival-specific only after a declared channel | Moderate |
| V5 — censoring-dependent audit value | A transfer/error model beyond V-F | Open | Existing survival validation designs | Could distinguish correctable corruption from irrecoverable censoring | Strong if a nonmonotone or threshold result appears | Unknown |
| V6 — rare-group allocation | Group-stratum transfer model | Open | Optimal two-phase stratified validation | Allocation under rarity, corruption, and follow-up | Potentially strong | Not justified under unrestricted V-F |
| V7 — adaptive/nonadaptive gap | Adversary and transfer model explicitly fixed | No positive gap found under unrestricted worst case | Adaptive multiwave validation | Could distinguish minimax from efficiency design | Open | Unknown |
| V8 — decision-stability threshold | Threshold `S_g(t)>c` plus a transfer model | Open | Robust decision certification and validation sampling | Direct audit budget for a stable conclusion | Potentially strong | Future only |

The current evidence supports V1 as a valid negative theorem candidate and V3 as an exact reference calculation. It does not yet support a positive audit-design theorem.
