import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import multiply
except ImportError:
    def multiply(A, b):
        raise NotImplementedError("Function multiply is not defined")

def test_multiply_basic():
    A = np.array([[0, 12, -1], [-1, -1, -1], [11, 5, 5]])
    b = np.array([-2, 1, 7])
    result = multiply(A, b)
    expected = np.array([5, -6, 18])
    assert np.allclose(result, expected), f"multiply(A, b) should be {expected}, got {result}"

def test_multiply_identity():
    A = np.identity(3)
    b = np.array([5, 9, -11.1])
    result = multiply(A, b)
    expected = b
    assert np.allclose(result, expected), f"multiply(identity, b) should be {expected}, got {result}"

def test_multiply_function_signature():
    import inspect
    sig = inspect.signature(multiply)
    params = list(sig.parameters.keys())
    assert params == ['A', 'b'], "multiply function should have parameters (A, b)"

def test_multiply_return_type():
    A = np.identity(3)
    b = np.array([1, 2, 3])
    result = multiply(A, b)
    assert isinstance(result, np.ndarray), f"multiply(A, b) should return np.ndarray, got {type(result).__name__}" 