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

def test_distance_basic():
    out = distance(0, 10, 5)
    assert len(out) == 5, "distance(0,10,5) should return 5 values"
    assert abs(out[0] - 0) < 1e-6, "First value should be 0"
    assert abs(out[-1] - (-430.5)) < 1e-1, "Last value should be about -430.5"

def test_distance_single():
    out = distance(0, 10, 1)
    assert isinstance(out, list) and len(out) == 1

def test_distance_param():
    cases = [
        (0, 4, 3, 6.0, 9.81, [0.0, 4.0, -31.24]),
        (0, 2, 2, 2.0, 10.0, [0.0, -12.0]),
        (1, 3, 3, 1.0, 9.81, [1.0, -7.905, -26.24])
    ]
    for t_start, t_end, n, v0, g, expected in cases:
        out = distance(t_start, t_end, n, v0, g)
        assert len(out) == n
        for o, e in zip(out, expected):
            assert abs(o - e) < 1e-2

def test_distance_return_type():
    out = distance(0, 1, 2)
    assert isinstance(out, list), "distance should return a list"
    assert all(isinstance(i, float) or isinstance(i, int) for i in out)

def test_distance_function_signature():
    import inspect
    sig = inspect.signature(distance)
    params = list(sig.parameters.keys())
    assert params[:3] == ['t_start', 't_end', 'n'], f"distance should have (t_start, t_end, n, ...) as parameters, got {params}" 