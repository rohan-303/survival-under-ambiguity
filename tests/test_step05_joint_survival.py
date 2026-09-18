import numpy as np

from survival_ambiguity.identification import (
    compatible_joint_set, coupling_gaps, censoring_operator,
    pointwise_bounds, rmst_event_weights, rmst_survival_representation,
    survival_map,
)


def _polytope(k=3, epsilon=0.1):
    times = np.arange(1, k + 1, dtype=float)
    q = np.ones(k + 1) / (k + 1)
    a = censoring_operator(q, times)
    p = np.linspace(1, k + 1, k + 1, dtype=float)
    p /= p.sum()
    contam = np.ones(a.shape[0]) / a.shape[0]
    r = (1 - epsilon) * (a @ p) + epsilon * contam
    return times, a, compatible_joint_set(a, r, epsilon)


def test_exact_polytope_and_survival_map():
    times, a, poly = _polytope(3)
    assert poly.dimension == 4
    assert poly.constraint_count == (1, a.shape[0])
    poly.validate()
    b = survival_map(times)
    assert b.shape == (3, 4)
    assert np.allclose(b @ np.array([0.1, 0.2, 0.3, 0.4]), [0.9, 0.7, 0.4])


def test_rmst_representation_matches_event_weights():
    times = np.array([1.0, 2.0, 4.0])
    p = np.array([0.1, 0.2, 0.3, 0.4])
    constant, weights = rmst_survival_representation(times, 5.0)
    lhs = rmst_event_weights(times, 5.0) @ p
    s = survival_map(times) @ p
    assert np.isclose(lhs, constant + weights @ s)


def test_pointwise_envelope_contains_direct_rmst_interval_and_gaps_nonnegative():
    times, _, poly = _polytope(3)
    out = coupling_gaps(poly, times, 3.5)
    assert out["gamma_plus"] >= -1e-9
    assert out["gamma_minus"] >= -1e-9
    assert out["rmst_lower"] >= out["pointwise_lower"] - 1e-9
    assert out["rmst_upper"] <= out["pointwise_upper"] + 1e-9


def test_no_censoring_two_bin_has_zero_coupling_gap():
    times = np.array([1.0, 2.0])
    a = censoring_operator(np.array([1.0]), np.array([0.25, 0.75]))
    p = np.array([0.2, 0.3, 0.5])
    r = 0.9 * (a @ p) + 0.1 * np.array([0.2, 0.3, 0.5])
    poly = compatible_joint_set(a, r, 0.1)
    out = coupling_gaps(poly, times, 3.0)
    assert out["gamma_plus"] < 1e-8 and out["gamma_minus"] < 1e-8


def test_corrected_step04_scenario_has_no_rmst_gap_after_weighting():
    times = np.array([0.25, 1.0, 2.0])
    a = censoring_operator(np.array([0.25, 0.25, 0.50]), times)
    p = np.array([0.30, 0.20, 0.20, 0.30])
    r = 0.9 * (a @ p) + 0.1 * np.full(a.shape[0], 1 / a.shape[0])
    poly = compatible_joint_set(a, r, 0.1)
    out = coupling_gaps(poly, times, 2.5)
    assert out["gamma_plus"] >= -1e-8 and out["gamma_minus"] >= -1e-8
    assert out["gamma_plus"] < 1e-8 and out["gamma_minus"] < 1e-8
    assert out["upper_common_attainable"] and out["lower_common_attainable"]


def test_infeasible_recorded_law_is_rejected():
    times = np.array([1.0])
    a = censoring_operator(np.array([1.0]), times)
    poly = compatible_joint_set(a, np.array([1.0, 0.0]), 0.0)
    try:
        pointwise_bounds(poly, times)
    except ValueError as exc:
        assert "infeasible" in str(exc)
    else:
        raise AssertionError("infeasible exact-Huber polytope was accepted")
