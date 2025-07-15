import sys
import os
import math

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import calculate_pi
except ImportError:
    def calculate_pi(n):
        raise NotImplementedError("Function calculate_pi is not defined")

def test_calculate_pi_function_exists():
    assert callable(calculate_pi), "calculate_pi should be a callable function"

def test_calculate_pi_basic():
    assert abs(calculate_pi(1) - 4) < 1e-6, "calculate_pi(1) should return 4"
    assert abs(calculate_pi(10) - 3.0418396189) < 1e-6
    assert abs(calculate_pi(1000) - math.pi) < 1e-2

def test_calculate_pi_param():
    cases = [
        (0, 0), (2, 2.6666666667), (5, 3.3396825397), (100, 3.1315929036)
    ]
    for n, expected in cases:
        assert abs(calculate_pi(n) - expected) < 1e-6

def test_calculate_pi_large():
    val = calculate_pi(10000)
    assert abs(val - math.pi) < 1e-3

def test_calculate_pi_return_type():
    assert isinstance(calculate_pi(10), float), "calculate_pi should return a float"

def test_calculate_pi_function_signature():
    import inspect
    sig = inspect.signature(calculate_pi)
    params = list(sig.parameters.keys())
    assert len(params) == 1, f"calculate_pi should accept 1 parameter, got {len(params)}"
    assert params[0] in ['n', 'num', 'number', 'x'], f"Parameter name should be 'n' or similar, got '{params[0]}'" 