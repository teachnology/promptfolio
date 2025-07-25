import sys
import os
import math

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import h
except ImportError:
    def h(x):
        raise NotImplementedError("Function h is not defined")

def test_h_0():
    result = h(0)
    expected = 1 / math.sqrt(2 * math.pi)
    assert abs(result - expected) < 1e-6, f"h(0) should be {expected}, got {result}"

def test_h_1():
    result = h(1)
    expected = 1 / math.sqrt(2 * math.pi) * math.exp(-0.5)
    assert abs(result - expected) < 1e-6, f"h(1) should be {expected}, got {result}"

def test_h_function_signature():
    import inspect
    sig = inspect.signature(h)
    params = list(sig.parameters.keys())
    assert params == ['x'], "h function should have parameter (x)"

def test_h_return_type():
    result = h(0)
    assert isinstance(result, float), f"h(0) should return float, got {type(result).__name__}" 