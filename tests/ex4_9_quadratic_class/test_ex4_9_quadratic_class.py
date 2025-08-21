import sys
import os
import numbers
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import Quadratic
except ImportError:
    class Quadratic:
        def __init__(self, *args, **kwargs):
            raise NotImplementedError("Class Quadratic is not defined")


def test_quadratic_value_and_roots_and_table():
    f = Quadratic(a=5, b=6, c=1)
    assert f.a == 5 and f.b == 6 and f.c == 1
    assert f.value(0) == 1
    assert np.allclose(f.roots(), (-0.2, -1)), f"roots should be (-0.2, -1), got {f.roots()}"
    assert f.table(0, 10, 11) is None


def test_quadratic_types_and_methods():
    f = Quadratic(a=10.2, b=5.6, c=-30.11)
    assert isinstance(f, Quadratic)
    assert isinstance(f.a, numbers.Real)
    assert isinstance(f.b, numbers.Real)
    assert isinstance(f.c, numbers.Real)
    assert isinstance(f.value(100), numbers.Real)
    r = f.roots()
    assert all(isinstance(i, numbers.Real) for i in r)
    assert callable(f.value)
    assert callable(f.table)
    assert callable(f.roots)


