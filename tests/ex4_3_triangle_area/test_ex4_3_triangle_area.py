import sys
import os
import numbers
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import triangle_area
except ImportError:
    def triangle_area(vertices):
        raise NotImplementedError("Function triangle_area is not defined")


def test_triangle_area_examples():
    res = triangle_area({1: (0, 0), 2: (3, 0), 3: (0, 7)})
    assert isinstance(res, numbers.Real), f"triangle_area should return a real number, got {type(res).__name__}"
    assert np.isclose(res, 10.5), f"Area should be 10.5, got {res}"


def test_triangle_area_zero():
    res = triangle_area({1: (0, 0), 2: (0, 0), 3: (0, 0)})
    assert res == 0, f"Area should be 0 for degenerate triangle, got {res}"


