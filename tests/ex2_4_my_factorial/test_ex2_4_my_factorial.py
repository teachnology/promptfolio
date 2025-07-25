import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import my_factorial
except ImportError:
    def my_factorial(n):
        raise NotImplementedError("Function my_factorial is not defined")

def test_my_factorial_0():
    result = my_factorial(0)
    assert result == 1, f"my_factorial(0) should be 1, got {result}"

def test_my_factorial_1():
    result = my_factorial(1)
    assert result == 1, f"my_factorial(1) should be 1, got {result}"

def test_my_factorial_5():
    result = my_factorial(5)
    assert result == 120, f"my_factorial(5) should be 120, got {result}"

def test_my_factorial_10():
    result = my_factorial(10)
    assert result == 3628800, f"my_factorial(10) should be 3628800, got {result}"

def test_my_factorial_function_signature():
    import inspect
    sig = inspect.signature(my_factorial)
    params = list(sig.parameters.keys())
    assert params == ['n'], "my_factorial function should have parameter (n)"

def test_my_factorial_return_type():
    result = my_factorial(5)
    assert isinstance(result, int), f"my_factorial(5) should return int, got {type(result).__name__}" 