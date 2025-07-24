import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import compute_heights
except ImportError:
    def compute_heights(h_0=1.0, h_1=0.3, n=10):
        raise NotImplementedError("Function compute_heights is not defined")

def test_compute_heights_function_exists():
    assert callable(compute_heights), "compute_heights should be a callable function"

def test_compute_heights_basic():
    out = compute_heights(1.0, 0.3, 10)
    expected = [1.0, 0.9, 0.81, 0.729, 0.6561, 0.59049, 0.531441, 0.4782969, 0.43046721, 0.387420489, 0.3486784401]
    for o, e in zip(out, expected):
        assert abs(o - e) < 1e-8, f"compute_heights(1.0, 0.3, 10) should be {expected}, but got {o}"
    assert len(out) == 11, "compute_heights(1.0, 0.3, 10) should be 11 elements"

def test_compute_heights_stop_by_h1():
    out = compute_heights(1.0, 0.5, 10)
    assert out[-1] < 0.5 and out[-2] > 0.5, "compute_heights(1.0, 0.5, 10) should stop when height < 0.5"

def test_compute_heights_2_0_1_5():
    out = compute_heights(2.0, 0.1, 5)
    expected = [2.0, 1.8, 1.62, 1.458, 1.3122, 1.181]
    for o, e in zip(out, expected):
        assert abs(o - e) < 1e-8, f"compute_heights(2.0, 0.1, 5) should be {expected}, but got {o}"

def test_compute_heights_1_0_0_01_3():
    out = compute_heights(1.0, 0.01, 3)
    expected = [1.0, 0.9, 0.81, 0.729]
    for o, e in zip(out, expected):
        assert abs(o - e) < 1e-8, f"compute_heights(1.0, 0.01, 3) should be {expected}, but got {o}"

def test_compute_heights_0_5_0_05_2():
    out = compute_heights(0.5, 0.05, 2)
    expected = [0.5, 0.45, 0.405]
    for o, e in zip(out, expected):
        assert abs(o - e) < 1e-8, f"compute_heights(0.5, 0.05, 2) should be {expected}, but got {o}"