import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import even_numbers
except ImportError:
    def even_numbers(n):
        raise NotImplementedError("Function even_numbers is not defined")

def test_even_numbers_function_exists():
    assert callable(even_numbers), "even_numbers should be a callable function"

def test_even_numbers_basic():
    assert even_numbers(10) == [0, 2, 4, 6, 8], "even_numbers(10) should return [0,2,4,6,8]"
    assert even_numbers(1) == [0], "even_numbers(1) should return [0]"
    assert even_numbers(2) == [0], "even_numbers(2) should return [0]"
    assert even_numbers(11) == [0, 2, 4, 6, 8, 10], "even_numbers(11) should return [0,2,4,6,8,10]"

def test_even_numbers_large():
    res = even_numbers(100)
    assert res[0] == 0 and res[-1] == 98 and len(res) == 50

def test_even_numbers_negative():
    try:
        result = even_numbers(-5)
        assert isinstance(result, list), "even_numbers(-5) should return a list or raise"
    except Exception:
        pass

def test_even_numbers_param():
    cases = [
        (0, []), (3, [0, 2]), (6, [0, 2, 4]), (8, [0, 2, 4, 6]), (20, [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
    ]
    for n, expected in cases:
        assert even_numbers(n) == expected, f"even_numbers({n}) should return {expected}"

def test_even_numbers_return_type():
    assert isinstance(even_numbers(10), list), "even_numbers should return a list"

def test_even_numbers_function_signature():
    import inspect
    sig = inspect.signature(even_numbers)
    params = list(sig.parameters.keys())
    assert len(params) == 1, f"even_numbers should accept 1 parameter, got {len(params)}"
    assert params[0] in ['n', 'num', 'number', 'x'], f"Parameter name should be 'n' or similar, got '{params[0]}'" 