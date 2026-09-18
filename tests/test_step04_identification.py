import numpy as np

from survival_ambiguity.identification import (
    AuditRegime, AuditSpec, bound_conditional_functional, censoring_operator,
    bound_joint_functional, rmst_weights, survival_weights,
)


def _case():
    times = np.array([0.25, 1.0])
    ops = [censoring_operator(np.array([1.0]), times)] * 2
    pi = (0.2, 0.8)
    clean = np.array([0.35, 0.25, 0.40, 0.10, 0.45, 0.45])
    q = np.array([0.04, 0.06, 0.16, 0.04, 0.20, 0.50])
    r = (0.9 * np.array([pi[0] * ops[0] @ clean[:3], pi[1] * ops[1] @ clean[3:]])).reshape(-1)
    r = r + 0.1 * q
    return times, ops, pi, r


def test_operator_conserves_probability_and_functionals():
    times, ops, _, _ = _case()
    assert all(np.allclose(a.sum(0), 1) for a in ops)
    assert np.allclose(survival_weights(times, 0.25), [0, 1, 1])
    assert np.allclose(rmst_weights(times, 1.5), [0.25, 1.0, 1.5])


def test_a1_lp_bounds_are_valid_and_rmst_is_linear():
    times, ops, pi, r = _case()
    spec = AuditSpec(AuditRegime.A1_TRUSTED_MARGINAL, 0.1, pi)
    s = bound_conditional_functional(ops, r, spec, 0, survival_weights(times, 0.25))
    m = bound_conditional_functional(ops, r, spec, 0, rmst_weights(times, 1.5))
    assert s.status == m.status == "OPTIMAL"
    assert 0 <= s.lower <= s.upper <= 1
    assert m.lower <= m.upper
    assert s.primal_residual is not None and s.primal_residual < 1e-8


def test_a2_requires_the_observed_marginal_contract():
    times, ops, pi, r = _case()
    # The constructed R has a contaminated group marginal, so A2 is infeasible.
    spec = AuditSpec(AuditRegime.A2_MARGINAL_PRESERVING, 0.1, pi)
    out = bound_conditional_functional(ops, r, spec, 0, survival_weights(times, 0.25))
    assert out.status == "INFEASIBLE"


def test_a3_cap_is_a_contract_check_under_fixed_observed_r():
    times, ops, pi, r = _case()
    spec = AuditSpec(AuditRegime.A3_GROUP_CAPS, 0.1, pi, (0.60, 0.30))
    out = bound_conditional_functional(ops, r, spec, 0, survival_weights(times, 0.25))
    assert out.status == "OPTIMAL"
    too_tight = AuditSpec(AuditRegime.A3_GROUP_CAPS, 0.1, pi, (0.01, 0.30))
    assert bound_conditional_functional(ops, r, too_tight, 0, survival_weights(times, 0.25)).status == "INFEASIBLE"


def test_a0_joint_functional_and_a4_identity_channel():
    times, ops, pi, r = _case()
    joint = bound_joint_functional(ops, r, 0.1, 0, survival_weights(times, 0.25))
    assert joint.status == "OPTIMAL" and 0 <= joint.lower <= joint.upper <= 1
    a1 = AuditSpec(AuditRegime.A1_TRUSTED_MARGINAL, 0.1, pi)
    a4 = AuditSpec(AuditRegime.A4_KNOWN_LABEL_CHANNEL, 0.1, pi,
                   label_matrix=((1.0, 0.0), (0.0, 1.0)))
    w = survival_weights(times, 0.25)
    one = bound_conditional_functional(ops, r, a1, 0, w)
    four = bound_conditional_functional(ops, r, a4, 0, w)
    assert np.isclose(one.lower, four.lower) and np.isclose(one.upper, four.upper)
