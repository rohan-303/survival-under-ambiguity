# Q10 Clinical-Shift Kill Test

Clinical-ShiftEval is directly framed around simulating and evaluating model adaptation in dynamic clinical NLP tasks.[2] It therefore threatens any contribution whose main artifact is simply a temporal clinical-NLP shift benchmark.

Semantic-drift work establishes that clinical terms can change meaning across time, including pediatric anxiety terminology.[3] That supports the existence of the phenomenon but does not, on the evidence retrieved here, establish label-free prediction of downstream model failure.

The SIReNs / Interpreting Dataset Shift in Clinical Notes line is an additional direct threat for explaining which clinical-note features changed. The exact full paper was not independently retrievable in this gate, so its scope is recorded as an unresolved threat rather than overstated as a verified subsumption.

**Kill conclusion:** Q10 must not repackage shift measurement or shift explanation. Only a validated warning-before-labels result would remain distinct, and that result is not yet demonstrated.
