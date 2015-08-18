from sympy import symbols, oo, Sum, harmonic, Add, S, binomial, factorial, dd
from sympy.series.limitseq import limitseq
from sympy.utilities.pytest import raises, XFAIL

n, m, k = symbols('n m k', integer=True)


def test_difference_delta():
    e = n*(n + 1)
    e2 = e * k

    assert dd(e) == 2*n + 2
    assert dd(e2, n, 2) == k*(4*n + 6)

    raises(ValueError, lambda: dd(e2))
    raises(ValueError, lambda: dd(e2, n, oo))


def test_difference_delta__Sum():
    e = Sum(1/k, (k, 1, n))
    assert dd(e, n) == 1/(n + 1)
    assert dd(e, n, 5) == Add(*[1/(i + n + 1) for i in range(5)])

    e = Sum(1/k, (k, 1, 3*n))
    assert dd(e, n) == Add(*[1/(i + 3*n + 1) for i in range(3)])

    e = n * Sum(1/k, (k, 1, n))
    assert dd(e, n) == 1 + Sum(1/k, (k, 1, n))

    e = Sum(1/k, (k, 1, n), (m, 1, n))
    assert dd(e, n) == harmonic(n)


def test_difference_delta__Add():
    e = n + n*(n + 1)
    assert dd(e, n) == 2*n + 3
    assert dd(e, n, 2) == 4*n + 8

    e = n + Sum(1/k, (k, 1, n))
    assert dd(e, n) == 1 + 1/(n + 1)
    assert dd(e, n, 5) == 5 + Add(*[1/(i + n + 1) for i in range(5)])


def test_limitseq():
    e = binomial(2*n, n) / Sum(binomial(2*k, k), (k, 1, n))
    assert limitseq(e, n) == S(3) / 4

    e = (5*n**3 + 3*n**2 + 4) / (3*n**3 + 4*n - 5)
    assert limitseq(e, n) == S(5) / 3

    e = (harmonic(n) * Sum(harmonic(k), (k, 1, n))) / (n*harmonic(2*n)**2)
    assert limitseq(e, n) == 1

    e = Sum(k**2 * Sum(2**m/m, (m, 1, k)), (k, 1, n)) / (2**n*n)
    assert limitseq(e, n) == 4

    e = (Sum(binomial(3*k, k) * binomial(5*k, k), (k, 1, n)) /
         (binomial(3*n, n) * binomial(5*n, n)))
    assert limitseq(e, n) == S(84375) / 83351

    e = (harmonic(n)**3 * Sum(1/harmonic(k), (k, 1, n)) /
         (n * Sum(harmonic(k)/k, (k, 1, n))))
    assert limitseq(e, n) == 2

    e = Sum(harmonic(k)**2/k, (k, 1, 2*n)) / harmonic(n)**3
    assert limitseq(e, n) == S(1) / 3


@XFAIL
def test_limitseq_fail():
    e = (Sum(2**k * binomial(2*k, k) / k**2, (k, 1, n)) /
         (Sum(2**k/k*2, (k, 1, n)) * Sum(binomial(2*k, k), (k, 1, n))))
    assert limitseq(e, n) == S(3) / 7

    e = n**3*Sum(2**k/k**2, (k, 1, n))**2 / (2**n * Sum(2**k/k, (k, 1, n)))
    assert limitseq(e, n) == 2

    e = (harmonic(n) * Sum(2**k/k, (k, 1, n)) /
         (n * Sum(2**k*harmonic(k)/k**2, (k,1, n))))
    assert limitseq(e, n) == 1

    e = (Sum(2**k*factorial(k) / k**2, (k, 1, 2*n)) /
         (Sum(4**k/k**2, (k, 1, n)) * Sum(factorial(k), (k, 1, 2*n))))
    assert limitseq(e, n) == S(3) / 16
