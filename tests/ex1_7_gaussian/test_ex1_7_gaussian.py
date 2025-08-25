import sys
import os
import math

# Add current directory to Python path to import student code
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import gaussian
except ImportError:
    def gaussian(x, m=0, s=1):
        raise NotImplementedError("Function gaussian is not defined")

def test_gaussian_function_exists():
    assert callable(gaussian), "gaussian should be a callable function"

def test_gaussian_0():
    expected = 1 / math.sqrt(2 * math.pi)
    result = gaussian(0)
    assert abs(result - expected) < 1e-6, f"gaussian(0) should be {expected}, but got {result}"

def test_gaussian_2():
    expected = 0.0539909665
    result = gaussian(2, 0, 1)
    assert abs(result - expected) < 1e-6, f"gaussian(2,0,1) should be {expected}, but got {result}"

def test_gaussian_shifted_mean():
    expected = 1 / math.sqrt(2 * math.pi)
    result = gaussian(2, 2, 1)
    assert abs(result - expected) < 1e-6, f"gaussian(2,2,1) should be {expected}, but got {result}"

def test_gaussian_small_sigma():
    expected = 1 / (0.1 * math.sqrt(2 * math.pi))
    result = gaussian(0, 0, 0.1)
    assert abs(result - expected) < 1e-5, f"gaussian(0,0,0.1) should be {expected}, but got {result}"

def test_gaussian_1():
    expected = math.exp(-0.5) / math.sqrt(2 * math.pi)
    result = gaussian(1, 0, 1)
    assert abs(result - expected) < 1e-6, f"gaussian(1,0,1) should be {expected}, but got {result}"

def test_gaussian_0_1_1():
    expected = math.exp(-0.5) / math.sqrt(2 * math.pi)
    result = gaussian(0, 1, 1)
    assert abs(result - expected) < 1e-6, f"gaussian(0,1,1) should be {expected}, but got {result}"

def test_gaussian_half_sigma():
    expected = 1 / (0.5 * math.sqrt(2 * math.pi))
    result = gaussian(0, 0, 0.5)
    assert abs(result - expected) < 1e-6, f"gaussian(0,0,0.5) should be {expected}, but got {result}"

def test_gaussian_negative_sigma():
    try:
        result = gaussian(0, 0, -1)
        assert isinstance(result, float), f"gaussian(0,0,-1) should be float, but got {type(result).__name__}"
    except (ValueError, ZeroDivisionError):
        pass
    except Exception as e:
        assert False, f"gaussian(0,0,-1) raised unexpected exception: {type(e).__name__}: {e}"

def test_gaussian_function_signature():
    import inspect
    sig = inspect.signature(gaussian)
    params = list(sig.parameters.keys())
    assert params == ['x', 'm', 's'], "gaussian function should have parameters (x, m, s)"

def test_gaussian_return_type():
    result = gaussian(0)
    assert isinstance(result, float), f"gaussian(0) should be float, but got {type(result).__name__}" 