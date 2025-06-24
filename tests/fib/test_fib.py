import pytest
import sys
import os
from typing import Any

# Add current directory to Python path to import student code
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Import student submitted function
try:
    from submission import fib
except ImportError:
    # If import fails, create a placeholder function
    def fib(n):
        raise NotImplementedError("Function fib is not defined")

def test_fib_function_exists():
    """Test if function exists"""
    assert callable(fib), "fib should be a callable function"

def test_fib_zero():
    """Test fib(0) = 0"""
    result = fib(0)
    assert result == 0, f"fib(0) should return 0, but got {result}"

def test_fib_one():
    """Test fib(1) = 1"""
    result = fib(1)
    assert result == 1, f"fib(1) should return 1, but got {result}"

def test_fib_two():
    """Test fib(2) = 1"""
    result = fib(2)
    assert result == 1, f"fib(2) should return 1, but got {result}"

def test_fib_five():
    """Test fib(5) = 5"""
    result = fib(5)
    assert result == 5, f"fib(5) should return 5, but got {result}"

def test_fib_ten():
    """Test fib(10) = 55"""
    result = fib(10)
    assert result == 55, f"fib(10) should return 55, but got {result}"

@pytest.mark.parametrize("n,expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55)
])
def test_fib_sequence(n, expected):
    """Parameterized test: verify first 11 Fibonacci numbers"""
    result = fib(n)
    assert result == expected, f"fib({n}) should return {expected}, but got {result}"

def test_fib_negative_input():
    """Test handling of negative input"""
    try:
        result = fib(-1)
        # If function doesn't raise exception, check if return value is reasonable
        assert isinstance(result, int), "fib(-1) should return an integer"
    except (ValueError, TypeError, RecursionError):
        # These exceptions are acceptable
        pass
    except Exception as e:
        pytest.fail(f"fib(-1) raised unexpected exception: {type(e).__name__}: {e}")

def test_fib_large_input():
    """Test handling of large input values"""
    try:
        result = fib(20)
        assert isinstance(result, int), "fib(20) should return an integer"
        assert result > 0, "fib(20) should return a positive number"
    except RecursionError:
        pytest.fail("fib(20) caused recursion depth exceeded, consider using iteration")
    except Exception as e:
        pytest.fail(f"fib(20) raised unexpected exception: {type(e).__name__}: {e}")

def test_fib_function_signature():
    """Test function signature"""
    import inspect
    sig = inspect.signature(fib)
    params = list(sig.parameters.keys())
    
    assert len(params) == 1, f"fib function should accept 1 parameter, but accepts {len(params)}"
    assert params[0] in ['n', 'num', 'number', 'x'], f"Parameter name should be 'n', but got '{params[0]}'"

def test_fib_return_type():
    """Test return value type"""
    result = fib(5)
    assert isinstance(result, int), f"fib(5) should return an integer, but returned {type(result).__name__}" 