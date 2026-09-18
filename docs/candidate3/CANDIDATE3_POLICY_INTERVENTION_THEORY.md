# Candidate 3 — Policy-Intervention Theory Gate

## Proposed intervention

Let `O_pi = A_pi(L)` and `O_pi' = A_pi'(L)`. Under a *passive* intervention, the latent trajectory and outcome mechanism are fixed. An ideal predictor based on a sufficient latent state is invariant:

`f*(O_pi) = f*(O_pi') = P(Y | L)`.

This is a consequence of sufficiency and the intervention definition, not a new theorem.

## Why the converse fails

If a fitted model changes under `pi` and `pi'`, this can mean:

- it uses observation-process information;
- the intervention removed predictive information;
- the representation is insufficient;
- timestamps changed meaningful disease dynamics;
- the intervention changed treatment or physiology.

Therefore instability is evidence of sensitivity, not proof of an illicit shortcut.

## Matched-information proposal

Holding total counts, measured variables, and window summaries fixed while changing selection or timing is attractive, but not automatically coherent. Selection conditional on severity changes the information distribution; changing timestamps changes valid temporal features; synthetic replacement values can create records that no care process could produce. Without a defined policy class and overlap, the comparison is not identified.

## Identification requirements

A causal policy claim would require consistency, well-defined policies, policy exchangeability conditional on sufficient history, positivity/overlap, and a defensible measurement mechanism. EHR site differences do not supply these assumptions. Monitoring can change care, so O2 is not a pure nuisance intervention. Masking/releasing measurements (O1) is experimentally controllable but is an information-loss intervention.

## Gate result

`CONDITIONAL` in isolation, but insufficient for Candidate 3. The proposed diagnostic reduces to generic perturbation/invariance testing unless a healthcare-specific identification theorem or policy natural experiment is supplied. No such theorem or experiment was verified.
