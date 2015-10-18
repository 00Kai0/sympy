from sympy import Piecewise, lambdify, Equality, Unequality, symbols, Sum
from sympy.abc import x
from sympy.printing.lambdarepr import NumPyPrinter
import numpy as np


def test_numpy_piecewise_regression():
    """
    NumPyPrinter needs to print Piecewise()'s choicelist as a list to avoid
    breaking compatibility with numpy 1.8. This is not necessary in numpy 1.9+.
    See gh-9747 and gh-9749 for details.
    """
    p = Piecewise((1, x < 0), (0, True))
    assert NumPyPrinter().doprint(p) == 'select([less(x, 0),True], [1,0], default=nan)'


def test_sum():
    k, k0, kN = symbols("k, k0, kN")

    s = Sum(x ** k, (k, k0, kN))
    f = lambdify((k0, kN, x), s, 'numpy')

    k0_, kN_ = 0, 10
    x_ = np.linspace(-1, +1, 100)
    assert np.allclose(f(k0_, kN_, x_), sum(x_ ** k_ for k_ in range(k0_, kN_ + 1)))

    s = Sum(k * x, (k, k0, kN))
    f = lambdify((k0, kN, x), s, 'numpy')

    k0_, kN_ = 0, 10
    x_ = np.linspace(-1, +1, 100)
    assert np.allclose(f(k0_, kN_, x_), sum(k_ * x_ for k_ in range(k0_, kN_ + 1)))


def test_relational():
    e = Equality(x, 1)

    f = lambdify((x,), e)
    x_ = np.array([0, 1, 2])
    assert np.array_equal(f(x_), [False, True, False])

    e = Unequality(x, 1)

    f = lambdify((x,), e)
    x_ = np.array([0, 1, 2])
    assert np.array_equal(f(x_), [True, False, True])

    e = (x < 1)

    f = lambdify((x,), e)
    x_ = np.array([0, 1, 2])
    assert np.array_equal(f(x_), [True, False, False])

    e = (x <= 1)

    f = lambdify((x,), e)
    x_ = np.array([0, 1, 2])
    assert np.array_equal(f(x_), [True, True, False])

    e = (x > 1)

    f = lambdify((x,), e)
    x_ = np.array([0, 1, 2])
    assert np.array_equal(f(x_), [False, False, True])

    e = (x >= 1)

    f = lambdify((x,), e)
    x_ = np.array([0, 1, 2])
    assert np.array_equal(f(x_), [False, True, True])
