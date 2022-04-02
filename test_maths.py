import pytest
import math
import maths
def test_recA():
    x = 10
    y = 30
    r = maths.recA(x, y)
    assert x * y == r


def test_recP():
    x = 10
    y = 30
    r = maths.recP(x, y)
    assert 2 * (x + y) == r
def test_circle():
    x = 10
    r = maths.circle(x)
    assert maths.pi * x * x == r


def test_square():
    x = 15
    r = maths.square(x)
    assert x * x == r


def test_tri():
    x = 10
    y = 15
    r = maths.tri(x, y)
    assert (x * y) / 2 == r
