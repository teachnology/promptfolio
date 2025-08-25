import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import heaviside
except ImportError:
    def heaviside(x):
        raise NotImplementedError("Function heaviside is not defined")

def test_heaviside_negative():
    result = heaviside(-5)
    assert result == 0, f"heaviside(-5) should be 0, got {result}"

def test_heaviside_zero():
    result = heaviside(0)
    assert result == 1, f"heaviside(0) should be 1, got {result}"

def test_heaviside_positive():
    result = heaviside(3.14)
    assert result == 1, f"heaviside(3.14) should be 1, got {result}"

def test_heaviside_function_signature():
    import inspect
    sig = inspect.signature(heaviside)
    params = list(sig.parameters.keys())
    assert params == ['x'], "heaviside function should have parameter (x)"

def test_heaviside_return_type():
    result = heaviside(0)
    assert isinstance(result, int), f"heaviside(0) should return int, got {type(result).__name__}" 