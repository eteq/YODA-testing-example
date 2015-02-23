from __future__ import division

import numpy as np


def test_lorentzian_known_good():
    from do_science import lorentzian

    assert lorentzian(0, 0, 1, 1) == 1/np.pi
    assert lorentzian(1, 1, np.pi, 1) == 1
    assert lorentzian(3, 1, np.pi, 2) == 0.25


def test_lorentz_normalized():
    from scipy.integrate import quad
    from do_science import lorentzian

    for lorentzian_args in [(1, 1, 1.5), (2, 3, 4), (1.2, 83, 12)]:
        print lorentzian_args
        integrand, err = quad(lorentzian, -np.inf, np.inf, args=lorentzian_args)
        assert abs(integrand - lorentzian_args[1]) < 2*err
