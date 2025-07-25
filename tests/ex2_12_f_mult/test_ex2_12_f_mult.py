import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import f_mult
except ImportError:
    def f_mult(A, B):
        raise NotImplementedError("Function f_mult is not defined")

def test_f_mult_basic():
    A = np.array([[0, 12, -1], [-1, -1, -1], [11, 5, 5]])
    B = np.array([[-2, 1, 7], [3, 0, 6], [2, 3, 5]])
    result = f_mult(A, B)
    expected = np.array([[34, -3, 67], [-3, -4, -18], [3, 26, 132]])
    assert np.allclose(result, expected), f"f_mult(A, B) should be {expected}, got {result}"

def test_f_mult_identity():
    A = np.identity(3)
    B = np.identity(3)
    result = f_mult(A, B)
    expected = np.identity(3)
    assert np.allclose(result, expected), f"f_mult(identity, identity) should be {expected}, got {result}"

def test_f_mult_function_signature():
    import inspect
    sig = inspect.signature(f_mult)
    params = list(sig.parameters.keys())
    assert params == ['A', 'B'], "f_mult function should have parameters (A, B)"

def test_f_mult_return_type():
    A = np.identity(3)
    B = np.identity(3)
    result = f_mult(A, B)
    assert isinstance(result, np.ndarray), f"f_mult(A, B) should return np.ndarray, got {type(result).__name__}" 