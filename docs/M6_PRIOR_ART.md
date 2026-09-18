# M6 prior-art update

| Source | Verified relevance | Threat to Step 07 |
|---|---|---|
| Two-Phase Sampling Designs for Data Validation | Optimal/nearly optimal validation sampling for error-prone data; survival setting and measurement-error validation | Threatens allocation novelty under model-based estimation [1] |
| Multi-wave Validation Sampling for Error-prone EHR | Uses influence-function information and validated waves to adapt stratified validation | Threatens adaptive/allocation claims [2] |
| Charikar, Steinhardt, Valiant, *Learning from Untrusted Data* | Semi-verified model formalizes trusted plus untrusted data transfer | Threatens broad transfer-model novelty [3] |
| Finite-population audit sampling | Hypergeometric finite-population audit boundaries and sample-size calculations | Directly subsumes E1-style certification [4] |

The Step 07 model differs in its explicit censored-record oracle and adversarial corrupted values, but the tested one-bin theorem does not use that distinction beyond a scalar known-channel transformation. No novelty claim is made.

## Sources

[1] https://pmc.ncbi.nlm.nih.gov/articles/PMC8715909/
[2] https://pmc.ncbi.nlm.nih.gov/articles/PMC10525037/
[3] https://arxiv.org/abs/1611.02315
[4] https://arxiv.org/html/2604.06116v2
