import numpy as np

from scripts.step02_sharpness_preflight import censor_matrix, one_bin, tv


def test_one_bin_tv_identity():
    g, p, p_prime = 0.37, 0.2, 0.81
    assert np.isclose(tv(one_bin(g, p), one_bin(g, p_prime)), g * abs(p - p_prime))


def test_censor_matrix_is_stochastic():
    matrix = censor_matrix(np.array([0.2, 0.3, 0.1, 0.4]), np.array([1.0, 2.0, 3.0]))
    assert np.all(matrix >= 0)
    assert np.allclose(matrix.sum(axis=0), 1.0)
