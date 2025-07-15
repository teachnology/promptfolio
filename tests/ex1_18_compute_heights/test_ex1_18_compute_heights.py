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
        assert abs(o - e) < 1e-8
    assert len(out) == 11

def test_compute_heights_stop_by_h1():
    out = compute_heights(1.0, 0.5, 10)
    # 1.0, 0.9, 0.81, 0.729, 0.6561, 0.59049, 0.531441, 0.4782969 (should stop here)
    assert out[-1] < 0.5 and out[-2] > 0.5

def test_compute_heights_param():
    cases = [
        (2.0, 0.1, 5, [2.0, 1.8, 1.62, 1.458, 1.3122, 1.181]),
        (1.0, 0.01, 3, [1.0, 0.9, 0.81, 0.729]),
        (0.5, 0.05, 2, [0.5, 0.45, 0.405])
    ]
    for h0, h1, n, expected in cases:
        out = compute_heights(h0, h1, n)
        for o, e in zip(out, expected):
            assert abs(o - e) < 1e-8

def test_compute_heights_return_type():
    out = compute_heights(1.0, 0.3, 10)
    assert isinstance(out, list), "compute_heights should return a list"
    assert all(isinstance(i, float) or isinstance(i, int) for i in out)

def test_compute_heights_function_signature():
    import inspect
    sig = inspect.signature(compute_heights)
    params = list(sig.parameters.keys())
    assert params[:3] == ['h_0', 'h_1', 'n'], f"compute_heights should have (h_0, h_1, n, ...) as parameters, got {params}" 