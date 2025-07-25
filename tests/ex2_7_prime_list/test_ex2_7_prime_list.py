import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import prime_list
except ImportError:
    def prime_list(n):
        raise NotImplementedError("Function prime_list is not defined")

def test_prime_list_10():
    result = prime_list(10)
    assert result == [2, 3, 5, 7], f"prime_list(10) should be [2, 3, 5, 7], got {result}"

def test_prime_list_0():
    result = prime_list(0)
    assert result == [], f"prime_list(0) should be [], got {result}"

def test_prime_list_20():
    result = prime_list(20)
    assert result == [2, 3, 5, 7, 11, 13, 17, 19], f"prime_list(20) should be [2, 3, 5, 7, 11, 13, 17, 19], got {result}"

def test_prime_list_function_signature():
    import inspect
    sig = inspect.signature(prime_list)
    params = list(sig.parameters.keys())
    assert params == ['n'], "prime_list function should have parameter (n)"

def test_prime_list_return_type():
    result = prime_list(10)
    assert isinstance(result, list), f"prime_list(10) should return list, got {type(result).__name__}" 