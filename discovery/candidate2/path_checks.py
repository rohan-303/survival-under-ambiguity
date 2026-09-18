"""Tiny Candidate 2 checks; not a reusable multistate implementation."""
from __future__ import annotations

from collections import Counter


def main() -> None:
    # Two path distributions end in state 4 with probability one.
    path_a = [(1, 2, 4)]
    path_b = [(1, 3, 4)]
    assert path_a[-1][-1] == path_b[-1][-1] == 4
    assert path_a != path_b

    # Same endpoint state, different dwell burden in adverse state 2.
    # The sequences encode unit time steps: 1->2->2->4 versus 1->2->4.
    trajectory_a = (1, 2, 2, 4)
    trajectory_b = (1, 2, 4, 4)
    dwell_a = trajectory_a.count(2)
    dwell_b = trajectory_b.count(2)
    assert trajectory_a[-1] == trajectory_b[-1] == 4
    assert dwell_a != dwell_b

    # A sparse landmark at the endpoint sees the same occupancy vector.
    endpoint_a = Counter({4: 1.0})
    endpoint_b = Counter({4: 1.0})
    assert endpoint_a == endpoint_b

    print({
        "path_nonidentification": "ELEMENTARY",
        "dwell_time_nonidentification": "ELEMENTARY",
        "endpoint_occupancy_equal": True,
        "dwell_state_2": [dwell_a, dwell_b],
        "multiple_landmark_status": "NOT_IDENTIFIED_BY_THIS_FIXTURE",
    })


if __name__ == "__main__":
    main()
