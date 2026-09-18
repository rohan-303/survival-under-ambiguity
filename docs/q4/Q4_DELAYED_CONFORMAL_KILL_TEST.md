# Q4 Delayed-Conformal Kill Test

## El Halabi & Brandt 2026

The paper studies delayed adaptive conformal inference for forecasts with a fixed horizon. It assumes the outcome needed to evaluate a forecast arrives after the horizon, decomposes the delayed recursion into interleaved ACI-like sequences, derives finite-sample long-run coverage bounds depending on delay, and introduces a delay-to-memory ratio. Its feedback is delayed but ultimately observed in the core setup. The paper studies temporal dependence and adaptation, not clinical subgroup selective risk, policy-dependent permanent label loss, or outcome-dependent feedback selection.

Therefore delayed ACI does not literally subsume M2/M3. It does subsume Q4's M0 and much of M1 when maturation is a known fixed/structured delay. Q4 cannot claim “delayed conformal prediction” as its contribution.

## Conditional and subgroup conformal threats

Finite prespecified subgroup validity, Mondrian conformal prediction, weighted conformal methods, and risk-coverage control already establish that subgroup targets require explicit conditioning or weighting. Running a monitor separately by subgroup is not a new theory. Unequal subgroup sample sizes create power and precision problems, not a new identification result.

## Selective feedback test

The only remaining candidate is a feedback indicator `R` whose arrival probability depends on score, action, subgroup, or outcome. Under outcome-dependent feedback, the ACI update sees a selected error stream. Nominal delayed-feedback coverage cannot be assumed from delay-only results. A valid repair would need known/estimable feedback propensities, a randomized validation stream, or a sharp sensitivity bound.

That distinction is potentially meaningful but currently generic: it resembles online learning with missing/selective feedback and missing-not-at-random conformal calibration. No clinical-specific theorem or data contract was found that would carry a project alone.

## Verdict

**Delayed-Feedback Gate D: `CONDITIONAL`.** Delayed ACI does not cover all selective maturation, but it occupies fixed guaranteed delay and leaves Q4 with only an unresolved generic partial-feedback problem. Q4 does not pass this gate.
