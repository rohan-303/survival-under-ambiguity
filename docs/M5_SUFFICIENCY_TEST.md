# M5 sufficiency test

## Strongest currently supported result

In the finite-population model with at most `m>=1` arbitrary corruptions, a gold audit returns only the clean recorded tuple. For any fixed audit policy that leaves at least one record unaudited, an adversary can preserve the same audited outcomes while making that unaudited record either a clean event or a clean non-event. Therefore a universal zero-width guarantee for the clean recorded event fraction requires auditing every record.

The exact realized post-audit interval is useful and transparent, and discovering a corrupted audited record can reduce remaining ambiguity. But this is a negative/impossibility result, not yet an optimal design method.

## Analyst impact

A survival-data analyst would learn an important guardrail: under an unrestricted worst-case corruption model, a small nonadaptive audit cannot certify a clean survival conclusion merely because it checked some records. Any positive audit-allocation rule requires an explicit transfer assumption—random corruption locations, exchangeability, stratum error rates, or a known error channel.

That guardrail is scientifically relevant, but it is not yet enough for a publishable primary paper because the impossibility is largely domain-general and existing validation/robust-learning work is close.

## Gate consequence

The pivot is **CONDITIONAL at best** until a survival-specific positive theorem emerges under the minimal transfer assumption. Step 06 therefore does not claim that audit effort should be allocated by rarity, follow-up, or variance. Those rules would be unsupported.
