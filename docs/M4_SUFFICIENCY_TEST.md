# M4 sufficiency test

## Scientific question

Would a fully proved theorem change how an analyst reports RMST uncertainty from contaminated censored data?

## Result

The answer is currently **no** for the claimed Step 04 phenomenon. The earlier numerical comparison used an unweighted sum of pointwise widths, which is not the RMST pointwise-integration interval. After using the correct RMST survival weights, the direct and pointwise intervals coincided in the corrected scenario and throughout the modest deterministic phase study.

A general direct-RMST LP remains a valid implementation, but “optimize a weighted sum over one feasible set rather than sum coordinatewise optima” is generic. Without a positive gap, a censoring-dependent phase transition, or a specialized exact algorithm, it does not yet provide a survival-specific reporting rule beyond correct optimization practice.

## What would pass later

A sufficient result would need at least one of:

1. a verified censored K=2/K=3 theorem showing a strict, interpretable coupling gap;
2. a sharp worst-case-over-`R` bound showing pointwise integration can materially overstate RMST ambiguity;
3. a survival-specific algorithm exploiting the censoring operator;
4. a theorem showing when direct RMST bounds equal pointwise integration, with nontrivial conditions and a clear diagnostic.

The current evidence establishes none of these. No neural model or synthetic generator is needed for such a result, but neither is justified yet.
