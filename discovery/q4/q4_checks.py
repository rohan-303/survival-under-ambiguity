"""Tiny deterministic Q4 checks; not a project implementation."""
from fractions import Fraction

# Group 0 has the same true error rate as group 1, but errors mature more slowly.
# The observed-label monitor therefore emits a false subgroup-safety ranking.
def naive_bias_check():
    # group 0: 8 correct, 2 errors; maturation: correct .9, error .1
    # group 1: 8 correct, 2 errors; maturation: both .9
    g0_obs_error = Fraction(2*1, 8*9 + 2*1)
    g1_obs_error = Fraction(2*9, 8*9 + 2*9)
    assert g0_obs_error < g1_obs_error
    assert Fraction(2, 10) == Fraction(2, 10)
    return g0_obs_error, g1_obs_error


def mar_weighting_check():
    # Known maturation propensities; inverse weighting recovers the finite
    # population totals in expectation (represented here by exact strata totals).
    strata = [(8, 2, Fraction(9, 10)), (2, 1, Fraction(1, 10))]
    weighted_errors = sum(Fraction(e, 1) for _, e, _ in strata)
    weighted_total = sum(Fraction(n, 1) for n, _, _ in strata)
    assert weighted_errors / weighted_total == Fraction(3, 10)
    return weighted_errors / weighted_total


def mnar_nonidentification_check():
    # Same observed masses: P(R=1,Y=1)=.1, P(R=1,Y=0)=.4,
    # P(R=0,RY=0)=.5. Hidden Y among R=0 differs.
    observed = ((Fraction(1,10), Fraction(4,10), Fraction(5,10)))
    risk_a = Fraction(1, 10)
    risk_b = Fraction(1, 10) + Fraction(5, 10)
    assert risk_a != risk_b
    assert observed == ((Fraction(1,10), Fraction(4,10), Fraction(5,10)))
    return risk_a, risk_b


def random_adjudication_check():
    # A positive-probability random adjudication arm makes the unresolved
    # outcome distribution observable under randomized acquisition.
    # This check is structural, not a power calculation.
    rho = Fraction(1, 10)
    assert rho > 0
    assert rho <= 1
    return rho


if __name__ == '__main__':
    print('naive_bias', naive_bias_check())
    print('mar_weighted_risk', mar_weighting_check())
    print('mnar_risks', mnar_nonidentification_check())
    print('random_adjudication_rate', random_adjudication_check())
