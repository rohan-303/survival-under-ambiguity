"""Tiny Step 00 checks; not a reusable project implementation."""
from __future__ import annotations

from math import isclose


def main() -> None:
    # Fixed-horizon two-cause cancellation.
    predicted = (0.30, 0.20)
    truth = (0.05, 0.45)
    assert isclose(sum(predicted), sum(truth))
    assert predicted != truth

    # Abstract action loss: action A protects cause 1, action B protects cause 2.
    # Unit loss for choosing the action aimed at the other cause.
    def loss(action: str, risks: tuple[float, float]) -> float:
        return risks[1] if action == "A" else risks[0]

    assert loss("A", truth) > loss("B", truth)
    assert loss("A", predicted) < loss("B", predicted)

    # Time-varying allocation crossing with a fixed total event risk.
    early = (0.24, 0.06)
    late = (0.06, 0.24)
    assert isclose(sum(early), sum(late))
    assert early[0] > early[1] and late[0] < late[1]

    print({
        "cancellation": "ELEMENTARY",
        "decision_reversal": "ELEMENTARY",
        "allocation_crossing": "ELEMENTARY",
        "all_cause_total": sum(predicted),
        "predicted_allocation": [v / sum(predicted) for v in predicted],
        "true_allocation": [v / sum(truth) for v in truth],
    })


if __name__ == "__main__":
    main()
