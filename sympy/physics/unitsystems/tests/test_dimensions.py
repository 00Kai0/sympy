# -*- coding: utf-8 -*-

from sympy import Tuple
from sympy.physics.unitsystems.dimensions import Dimension
from sympy.utilities.pytest import raises


def test_definition():

    length = Dimension(name="length", symbol="L", length=1)

    assert length.get('length') == 1
    assert length.get('time') is None
    assert length.name == "length"
    assert length.symbol == "L"


def test_dict_properties():
    dic = {"length": 1, "time": -2}
    d = Dimension(dic)

    assert d["length"] == 1

    assert d.args == (Tuple("length", 1), Tuple("time", -2))

    assert d.items() == dic.items()
    assert d.keys() == dic.keys()
    assert d.values() == dic.values()

    assert len(d) == 2

    assert d.get("length") == 1
    assert d.get("mass") is None

    assert ("length" in d) is True
    assert ("mass" in d) is False


def test_error_definition():
    # tuple with more or less than two entries
    raises(ValueError, lambda: Dimension(("length", 1, 2)))
    raises(ValueError, lambda: Dimension(["length"]))

    # non-number power
    raises(TypeError, lambda: Dimension(length="a"))

    # non-dict/list/tuple as positional arg
    raises(TypeError, lambda: Dimension("length"))

    # non-number with named argument
    raises(TypeError, lambda: Dimension(length=(1, 2)))

def test_str():
    assert str(Dimension(length=1)) == "{'length': 1}"
    assert str(Dimension(length=1, symbol="L")) == "L"
    assert str(Dimension(length=1, name="length")) == "length"
    assert str(Dimension(length=1, symbol="L", name="length")) == 'L'


def test_properties():
    assert Dimension(length=1).is_dimensionless is False
    assert Dimension().is_dimensionless is True
    assert Dimension(length=0).is_dimensionless is True


def test_add_sub():
    length = Dimension(length=1)

    assert length + length == length
    assert length - length == length
    assert -length == length

    raises(TypeError, lambda: length + 1)
    raises(TypeError, lambda: length - 1)
    raises(ValueError, lambda: length + Dimension(time=1))
    raises(ValueError, lambda: length - Dimension(time=1))


def test_mul_div_exp():
    length = Dimension(length=1)
    time = Dimension(time=1)
    velocity = length / time

    assert length**2 == Dimension(length=2)
    assert length*length == length**2
    assert length * time == Dimension(length=1, time=1)
    assert velocity == Dimension(length=1, time=-1)
    assert velocity**2 == Dimension(length=2, time=-2)

    raises(TypeError, lambda: length**"a")
