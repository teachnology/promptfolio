import sys
import os
import numbers

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import my_factorial
except ImportError:
    def my_factorial(x):
        raise NotImplementedError("Function my_factorial is not defined")


def test_my_factorial_exists():
    assert callable(my_factorial), "my_factorial should be a callable function"


def test_my_factorial_0():
    assert my_factorial(0) == 1, f"my_factorial(0) should be 1, got {my_factorial(0)}"

def test_my_factorial_1():
    assert my_factorial(1) == 1, f"my_factorial(1) should be 1, got {my_factorial(1)}"

def test_my_factorial_2():
    assert my_factorial(2) == 2, f"my_factorial(2) should be 2, got {my_factorial(2)}"

def test_my_factorial_5():
    assert my_factorial(5) == 120, f"my_factorial(5) should be 120, got {my_factorial(5)}"


def test_my_factorial_negative_raises():
    import pytest
    with pytest.raises(ValueError):
        my_factorial(-5)


def test_my_factorial_return_type():
    result = my_factorial(5)
    assert isinstance(result, numbers.Real), f"my_factorial(5) should return a real number, got {type(result).__name__}"


