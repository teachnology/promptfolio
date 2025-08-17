import sys
import os
import numbers
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import Simple
except ImportError:
    class Simple:
        def __init__(self, *args, **kwargs):
            raise NotImplementedError("Class Simple is not defined")


def test_simple_double_and_types():
    s = Simple(2)
    for _ in range(10):
        s.double()
    assert np.isclose(s.i, 2**11), f"After 11 values (init + 10 doubles), i should be 2**11, got {s.i}"

    assert isinstance(s, Simple)
    assert isinstance(s.i, numbers.Real)
    assert s.double() is None
    assert callable(s.double)


