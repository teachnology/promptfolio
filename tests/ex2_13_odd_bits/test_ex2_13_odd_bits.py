import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

def test_odd_shape():
    from submission import odd
    assert isinstance(odd, np.ndarray), f"odd should be np.ndarray, got {type(odd).__name__}"
    assert odd.shape == (28,), f"odd.shape should be (28,), got {odd.shape}"

def test_odd_sq_shape():
    from submission import odd_sq
    assert isinstance(odd_sq, np.ndarray), f"odd_sq should be np.ndarray, got {type(odd_sq).__name__}"
    assert odd_sq.shape == (4, 7), f"odd_sq.shape should be (4, 7), got {odd_sq.shape}"

def test_odd_bits_shape():
    from submission import odd_bits
    assert isinstance(odd_bits, np.ndarray), f"odd_bits should be np.ndarray, got {type(odd_bits).__name__}"
    assert odd_bits.shape == (2, 3), f"odd_bits.shape should be (2, 3), got {odd_bits.shape}"

def test_odd_values():
    from submission import odd
    expected = np.arange(1, 56, 2)
    assert np.allclose(odd, expected), f"odd should be {expected}, got {odd}"

def test_odd_bits_values():
    from submission import odd_sq, odd_bits
    expected = np.arange(1, 56, 2).reshape(4, 7)[1:3, 1::2]
    assert np.allclose(odd_bits, expected), f"odd_bits should be {expected}, got {odd_bits}" 