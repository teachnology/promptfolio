import sys
import os
import numbers
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import Line
except ImportError:
    class Line:
        def __init__(self, *args, **kwargs):
            raise NotImplementedError("Class Line is not defined")


def test_line_vertical_and_defined():
    line = Line(p0=(0, 0), p1=(0, 0))
    assert line.p0 == (0, 0)
    assert line.p1 == (0, 0)
    assert line.value(10) is None

    line = Line(p0=(0, 0), p1=(10, 10))
    assert line.p0 == (0, 0)
    assert line.p1 == (10, 10)
    for x in np.linspace(-10, 10, 20):
        assert np.isclose(line.value(x), x), f"For y=x line, value({x}) should be {x}, got {line.value(x)}"


def test_line_types():
    line = Line(p0=(0, 0), p1=(10, 10))
    assert isinstance(line, Line)
    assert isinstance(line.p0, tuple)
    assert isinstance(line.p1, tuple)
    assert all(isinstance(i, numbers.Real) for i in line.p0)
    assert all(isinstance(i, numbers.Real) for i in line.p1)
    assert isinstance(line.value(100), numbers.Real)
    assert callable(line.value)


