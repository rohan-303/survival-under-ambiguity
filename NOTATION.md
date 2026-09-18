# Notation

- `X`: baseline covariates.
- `T`: latent event time.
- `C`: censoring time.
- `Y = min(T,C)`: observed time.
- `Delta = 1{T <= C}`: event indicator.
- `H`: censoring law or censoring mechanism, with assumptions stated per result.
- `A_H`: observation operator induced by censoring law `H`.
- `epsilon`: contamination budget, with `0 <= epsilon <= 1`.
- `Q`: contamination law; its admissible class must be specified.
- `P_0`: latent clean event-time/population law.
- `P_obs`: observed-data law.
- `G`: subgroup variable or subgroup label; use `G=g` for subgroup membership.
- `pi_g = P(G=g)`: prevalence of subgroup `g`.
- `G_C(t) = P(C >= t | G=g)` when subgroup conditioning is needed: subgroup-specific censoring survival. This is distinct from the subgroup label `G`.
- `tau`: prespecified time horizon, often used for RMST.
- `S(t) = P(T > t)`: survival function; subgroup versions use `S_g(t)`.
- `RMST(tau) = E[min(T,tau)] = integral_0^tau S(u)du`, when defined; subgroup versions use `RMST_g(tau)`.
- `Theta`: latent survival model class/assumption set.
- `psi`: target functional, such as `S(t)`, RMST, a median when defined, or a subgroup functional.
- `identified set`: all values of `psi(P)` over latent laws compatible with the observed evidence, contamination model, censoring assumptions, and `Theta`.
- `ambiguity set`: the compatible collection of latent/observed laws under the specified uncertainty model.
- `omega_{psi,Theta,A}(r)`: candidate recoverability modulus, e.g. the supremum of `|psi(P)-psi(P')|` over `P,P' in Theta` satisfying an observation-indistinguishability constraint `d(A_H P,A_H P') <= r`. The exact definition remains [OPEN] and may depend on contamination.

Symbols and conditioning conventions must be frozen more precisely before proofs or computation.
