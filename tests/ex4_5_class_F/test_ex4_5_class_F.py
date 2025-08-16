import sys
import os
import numbers
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import F
except ImportError:
    class F:  # sentinel to raise clearer error when used
        def __init__(self, *args, **kwargs):
            raise NotImplementedError("Class F is not defined")


def test_F_init_and_value():
    f = F(5, 4.1)
    assert np.isclose(f.a, 5), f"f.a should be 5, got {f.a}"
    assert np.isclose(f.w, 4.1), f"f.w should be 4.1, got {f.w}"
    assert np.isclose(f.value(3), -8.052321580865151e-08), f"f.value(3) should be -8.0523e-08, got {f.value(3)}"


def test_F_types_and_methods():
    f = F(0.73, 1.14185)
    assert isinstance(f, F), "Instance should be of class F"
    assert isinstance(f.a, numbers.Real) and isinstance(f.w, numbers.Real), "Attributes should be numeric"
    assert isinstance(f.value(0.1), numbers.Real), "value(x) should return a number"
    assert callable(f.value), "value should be callable"


