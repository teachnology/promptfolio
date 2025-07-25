import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import f_cubic
except ImportError:
    def f_cubic(A):
        raise NotImplementedError("Function f_cubic is not defined")

def test_f_cubic_basic():
    A = np.array([[1, 2, -6], [2, 2, -5]])
    result = f_cubic(A)
    expected = np.power(A, 3) + np.multiply(A, np.exp(A)) + 1
    assert np.allclose(result, expected), f"f_cubic(A) should be {expected}, got {result}"

def test_f_cubic_shape():
    A = np.array([[0, 1], [2, 3]])
    result = f_cubic(A)
    assert result.shape == A.shape, f"f_cubic(A) should have shape {A.shape}, got {result.shape}"

def test_f_cubic_function_signature():
    import inspect
    sig = inspect.signature(f_cubic)
    params = list(sig.parameters.keys())
    assert params == ['A'], "f_cubic function should have parameter (A)"

def test_f_cubic_return_type():
    A = np.array([[1]])
    result = f_cubic(A)
    assert isinstance(result, np.ndarray), f"f_cubic(A) should return np.ndarray, got {type(result).__name__}" 