import sys
import os
import math

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import approx_pi
except ImportError:
    def approx_pi(n):
        raise NotImplementedError("Function approx_pi is not defined")

def test_approx_pi_10():
    result = approx_pi(10)
    assert abs(result - math.pi) < 0.1, f"approx_pi(10) should be close to {math.pi}, got {result}"

def test_approx_pi_100():
    result = approx_pi(100)
    assert abs(result - math.pi) < 0.01, f"approx_pi(100) should be close to {math.pi}, got {result}"

def test_approx_pi_function_signature():
    import inspect
    sig = inspect.signature(approx_pi)
    params = list(sig.parameters.keys())
    assert params == ['n'], "approx_pi function should have parameter (n)"

def test_approx_pi_return_type():
    result = approx_pi(10)
    assert isinstance(result, float), f"approx_pi(10) should return float, got {type(result).__name__}" 