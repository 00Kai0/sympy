from sympy import Symbol, exp, log
from sympy.calculus.singularities import (singularities, is_increasing,
                                          is_strictly_increasing, is_decreasing,
                                          is_strictly_decreasing)
from sympy.sets import Interval
from sympy import oo, S

from sympy.utilities.pytest import XFAIL

x = Symbol('x')


def test_singularities():
    x = Symbol('x', real=True)

    assert singularities(x**2, x) == ()
    assert singularities(x/(x**2 + 3*x + 2), x) == (-2, -1)


@XFAIL
def test_singularities_non_rational():
    x = Symbol('x', real=True)

    assert singularities(exp(1/x), x) == (0)
    assert singularities(log((x - 2)**2), x) == (2)


def test_is_increasing():
    assert is_increasing(x**3 - 3*x**2 + 4*x, S.Reals)
    assert is_increasing(-x**2, Interval(-oo, 0))
    assert not is_increasing(-x**2, Interval(0, oo))
    assert not is_increasing(4*x**3 - 6*x**2 - 72*x + 30, Interval(-2, 3))


def test_is_strictly_increasing():
    assert is_strictly_increasing(4*x**3 - 6*x**2 - 72*x + 30, Interval.Ropen(-oo, -2))
    assert is_strictly_increasing(4*x**3 - 6*x**2 - 72*x + 30, Interval.Lopen(3, oo))
    assert not is_strictly_increasing(4*x**3 - 6*x**2 - 72*x + 30, Interval.open(-2, 3))
    assert not is_strictly_increasing(-x**2, Interval(0, oo))


def test_is_decreasing():
    assert is_decreasing(1/(x**2 - 3*x), Interval.open(1.5, 3))
    assert is_decreasing(1/(x**2 - 3*x), Interval.Lopen(3, oo))
    assert not is_decreasing(1/(x**2 - 3*x), Interval.Ropen(-oo, S(3)/2))
    assert not is_decreasing(-x**2, Interval(-oo, 0))


def test_is_strictly_decreasing():
    assert is_decreasing(1/(x**2 - 3*x), Interval.open(1.5, 3))
    assert is_decreasing(1/(x**2 - 3*x), Interval.Lopen(3, oo))
    assert not is_decreasing(1/(x**2 - 3*x), Interval.Ropen(-oo, S(3)/2))
    assert not is_decreasing(-x**2, Interval(-oo, 0))
