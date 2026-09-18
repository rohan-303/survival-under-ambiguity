# Adversarial survival audit model (Step 06)

## 1. Motivation

The provisional problem is verification of censored survival records that may contain arbitrary row corruption. The audit question is distinct from recovering latent event times: a gold-standard audit corrects the recorded data quality, but cannot undo right censoring.

## 2. Audit oracle

For subject `i`, latent event time `T_i` and censoring time `C_i` induce the clean recorded tuple

`Z_i*=(G_i,Y_i,Delta_i)`, `Y_i=min(T_i,C_i)`, `Delta_i=1{T_i<=C_i}`.

The observed tuple `Z_i` may be corrupted. An audit returns `Z_i*` exactly. It never returns `T_i` when `Delta_i=0`, and it never converts a censored record into an observed future event.

The finite reference code stores only `(group, y_bin, delta)` and has no latent-`T` audit field.

## 3. V-P: population/stratified validation

A large error-prone population is accompanied by validated records from selected strata. This connects directly to two-phase and validation-subset literature. A probability or exchangeability model is needed to translate validation outcomes to population error rates. No V-P estimator or asymptotic theory is implemented in Step 06.

## 4. V-F: finite-population adversarial audit

There are `n` observed tuples and unknown clean tuples with Hamming corruption budget `m`:

`# {i: Z_i != Z_i*} <= m`.

An audit set `A`, with `|A|<=B`, returns the clean recorded tuples on `A`. The primary target is the clean recorded event fraction. A one-bin survival probability can be reported only through an explicitly declared known follow-up channel; the audit itself does not reveal censored `T`.

## 5. Selected primary model

**V-F** is primary for the Step 06 preflight. It cleanly separates deterministic adversarial identification from probability-based validation design and supports exact enumeration for tiny populations. V-P remains secondary and is retained only as a prior-art comparison.

## 6. Corruption and censoring

The corruption model is arbitrary row replacement with at most `m` changed recorded tuples. Censoring is encoded in `delta=0`; the audit preserves that censoring state. The primary finite-population theorem is about recorded-event fractions because finite deterministic records do not by themselves identify a population event probability under random censoring.

## 7. Target and width

For clean recorded event fraction `theta*=n^{-1} sum_i Delta_i*`, the post-audit identified interval is the range of `theta*` over all clean tuples compatible with the observed tuples, audit outcomes, and corruption budget. Width is `W(I)=upper-lower`. If a known one-bin channel asserts recorded event probability `r=g p`, the corresponding channel-translated interval is `[lower/g, upper/g]`; this is not additional information from the audit.

## 8. Exact post-audit interval

Let `d_A` be audited discrepancies and `m'=m-d_A`. Among unverified records, let `u_1` be observed events and `u_0` observed non-events. Then:

`lower_count = audited_clean_events + u_1 - min(u_1,m')`,

`upper_count = audited_clean_events + u_1 + min(u_0,m')`.

Divide by `n` for the recorded-event interval. Brute-force enumeration agrees for all tested tiny cases.

## 9. Unrestricted-adversarial impossibility

For any fixed audit policy with `B<n` and `m>=1`, an adversary can choose an observed population and compatible audit outcomes leaving at least one unaudited record whose clean event status is ambiguous. Thus a universal zero-width guarantee requires auditing every record. This is a finite-population impossibility result, checked by enumeration and witnessed by all observed/audited records being censored while one unaudited record may be clean event or non-event.

Auditing can still reduce width for realized outcomes—for example, discovering a corrupted record consumes the corruption budget—but the worst-case guarantee remains positive unless the audit covers the population.

## 10. Structured auditability assumptions

A positive nontrivial design requires a transfer assumption linking audited and unaudited records. Candidate assumptions are random corruption locations, stratum contamination caps with a justified update rule, exchangeability within strata, a bounded error channel, or an explicit probabilistic validation model. None is promoted as the primary theorem here. A cap stated only as “at most `m_h` in stratum h” does not by itself make an audited correct record evidence that unaudited records are correct.

## 11. Rare groups and adaptation

Rare-group allocation is not developed as a theorem. In the unrestricted V-F model, group labels do not create transfer information, so “audit the rare group” is not minimax-justified. Under a future transfer model, remaining uncertainty would combine group record count, error budget, and censoring channel; auditing cannot recover censored future events.

Adaptive and randomized policies do not defeat the basic impossibility against an adversary that can preserve the same audited outcomes while leaving one unaudited ambiguity. Any advantage requires an oblivious/random-location or exchangeability assumption.

## 12. Claim status

| Claim | Status |
|---|---|
| Audit reveals the clean recorded tuple only | `ELEMENTARY_DEFINITION` / `CHECKED` |
| Exact post-audit binary recorded-event interval | `DERIVED` / `CHECKED` |
| Brute-force agreement for tiny cases | `CHECKED` |
| Full-audit zero width | `ELEMENTARY_DERIVATION` |
| Non-full-audit universal zero-width impossibility | `POTENTIALLY_NOVEL`, finite-model theorem candidate; novelty unverified |
| Positive rare-group minimax allocation | `OPEN` |
| Censoring-dependent positive audit theorem | `OPEN` |
| Adaptive advantage | `OPEN`; no advantage under the unrestricted worst-case witness |
| Population V-P identification | `OPEN` and prior-art sensitive |

## 13. Limitations

This is not a finite-sample confidence procedure, not a population validation estimator, and not a latent-event-time recovery method. It does not claim that chart review reveals unobserved survival after censoring. No synthetic generation, OT, neural model, or real dataset is used.
