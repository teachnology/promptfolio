import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import mult
except ImportError:
    def mult(vector, n):
        raise NotImplementedError("Function mult is not defined")

def test_mult_basic():
    result = mult([1, 2, 3], 2)
    assert result == [2, 4, 6], f"mult([1, 2, 3], 2) should be [2, 4, 6], got {result}"

def test_mult_empty():
    result = mult([], 5)
    assert result == [], f"mult([], 5) should be [], got {result}"

def test_mult_negative():
    result = mult([1, -1, 0], -3)
    assert result == [-3, 3, 0], f"mult([1, -1, 0], -3) should be [-3, 3, 0], got {result}"

def test_mult_float():
    result = mult([1.1, 2.2], 2)
    assert result == [2.2, 4.4], f"mult([1.1, 2.2], 2) should be [2.2, 4.4], got {result}"

def test_mult_function_signature():
    import inspect
    sig = inspect.signature(mult)
    params = list(sig.parameters.keys())
    assert params == ['vector', 'n'], "mult function should have parameters (vector, n)"

def test_mult_return_type():
    result = mult([1, 2, 3], 2)
    assert isinstance(result, list), f"mult([1, 2, 3], 2) should return list, got {type(result).__name__}" 