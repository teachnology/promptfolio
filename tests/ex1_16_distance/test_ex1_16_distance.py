import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import distance
except ImportError:
    def distance(t_start, t_end, n, v0=6.0, g=9.81):
        raise NotImplementedError("Function distance is not defined")

def test_distance_function_exists():
    assert callable(distance), "distance should be a callable function"

def test_distance_0_10_5():
    out = distance(0, 10, 5)
    assert len(out) == 5, "distance(0, 10, 5) should be 5 values"
    assert abs(out[0] - 0) < 1e-6, "distance(0, 10, 5)[0] should be 0"
    assert abs(out[-1] - (-430.5)) < 1e-1, "distance(0, 10, 5)[-1] should be -430.5"

def test_distance_0_10_1():
    out = distance(0, 10, 1)
    assert isinstance(out, list) and len(out) == 1, "distance(0, 10, 1) should be a list of length 1"

def test_distance_0_4_3():
    out = distance(0, 4, 3, 6.0, 9.81)
    expected = [0.0, 4.0, -31.24]
    for o, e in zip(out, expected):
        assert abs(o - e) < 1e-2, f"distance(0, 4, 3, 6.0, 9.81) should be {expected}, but got {o}"

def test_distance_0_2_2():
    out = distance(0, 2, 2, 2.0, 10.0)
    expected = [0.0, -12.0]
    for o, e in zip(out, expected):
        assert abs(o - e) < 1e-2, f"distance(0, 2, 2, 2.0, 10.0) should be {expected}, but got {o}"

def test_distance_1_3_3():
    out = distance(1, 3, 3, 1.0, 9.81)
    expected = [1.0, -7.905, -26.24]
    for o, e in zip(out, expected):
        assert abs(o - e) < 1e-2, f"distance(1, 3, 3, 1.0, 9.81) should be {expected}, but got {o}"