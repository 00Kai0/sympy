from sympy import symbols, Mul
from sympy.stats import Normal, Poisson, variance
from sympy.stats.rv import probability, expectation
from sympy.stats.symbolic_probability import Covariance, Variance, Probability, Expectation


def test_literal_probability():
    X = Normal('X', 2, 3)
    Y = Normal('Y', 3, 4)
    Z = Poisson('Z', 4)
    W = Poisson('W', 3)
    x, y, w, z = symbols('x, y, w, z')

    assert Probability(X > 0).doit() == probability(X > 0)
    assert Probability(X > x).doit() == probability(X > x)

    assert Expectation(X).doit() == expectation(X)
    assert Expectation(X**2).doit() == expectation(X**2)

    assert Variance(w) == 0
    assert Variance(X).doit() == variance(X)
    assert Variance(X + z) == Variance(X)
    assert Variance(X*Y).args == (Mul(X, Y),)
    assert type(Variance(X*Y)) == Variance
    assert Variance(z*X) == z**2*Variance(X)
    assert Variance(X + Y) == Variance(X) + Variance(Y) + 2*Covariance(X, Y)
    assert Variance(X + Y + Z + W) == (Variance(X) + Variance(Y) + Variance(Z) + Variance(W) +
                                       2 * Covariance(X, Y) + 2 * Covariance(X, Z) + 2 * Covariance(X, W) +
                                       2 * Covariance(Y, Z) + 2 * Covariance(Y, W) + 2 * Covariance(W, Z))

    assert Covariance(w, z) == 0
    assert Covariance(X, w) == 0
    assert Covariance(w, X) == 0
    assert Covariance(X, Y).args == (X, Y)
    assert type(Covariance(X, Y)) == Covariance
    assert Covariance(z*X + 3, Y) == z*Covariance(X, Y)
    assert Covariance(X, X) == Variance(X)
    assert Covariance(z*X + 3, w*Y + 4) == w*z*Covariance(X,Y)
    assert Covariance(X, Y) == Covariance(Y, X)
    assert Covariance(X + Y, Z + W) == Covariance(W, X) + Covariance(W, Y) + Covariance(X, Z) + Covariance(Y, Z)
    assert Covariance(x*X + y*Y, z*Z + w*W) == (x*w*Covariance(W, X) + w*y*Covariance(W, Y) +
                                                x*z*Covariance(X, Z) + y*z*Covariance(Y, Z))
