import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

def test_w_shape():
    from submission import w
    assert isinstance(w, np.ndarray), f"w should be np.ndarray, got {type(w).__name__}"
    assert w.shape == (31,), f"w.shape should be (31,), got {w.shape}"

def test_wbits_shape():
    from submission import wbits
    assert isinstance(wbits, np.ndarray), f"wbits should be np.ndarray, got {type(wbits).__name__}"
    assert wbits.shape == (9,), f"wbits.shape should be (9,), got {wbits.shape}"

def test_w_values():
    from submission import w
    assert np.isclose(w[-1] - w[0], 3), f"w[-1] - w[0] should be 3, got {w[-1] - w[0]}"

def test_wbits_values():
    from submission import wbits
    expected = np.array([0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7])
    assert np.allclose(wbits, expected), f"wbits should be {expected}, got {wbits}" 