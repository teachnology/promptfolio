import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import odd_numbers
except ImportError:
    def odd_numbers(n):
        raise NotImplementedError("Function odd_numbers is not defined")

def test_odd_numbers_function_exists():
    assert callable(odd_numbers), "odd_numbers should be a callable function"

def test_odd_numbers_basic():
    assert odd_numbers(10) == [1, 3, 5, 7, 9], "odd_numbers(10) should return [1,3,5,7,9]"
    assert odd_numbers(1) == [], "odd_numbers(1) should return []"
    assert odd_numbers(2) == [1], "odd_numbers(2) should return [1]"
    assert odd_numbers(15) == [1, 3, 5, 7, 9, 11, 13], "odd_numbers(15) should return [1,3,5,7,9,11,13]"

def test_odd_numbers_large():
    res = odd_numbers(100)
    assert res[0] == 1 and res[-1] == 99 and len(res) == 50

def test_odd_numbers_negative():
    try:
        result = odd_numbers(-5)
        assert isinstance(result, list), "odd_numbers(-5) should return a list or raise"
    except Exception:
        pass

def test_odd_numbers_param():
    cases = [
        (0, []), (3, [1]), (5, [1, 3]), (8, [1, 3, 5, 7]), (20, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
    ]
    for n, expected in cases:
        assert odd_numbers(n) == expected, f"odd_numbers({n}) should return {expected}"

def test_odd_numbers_return_type():
    assert isinstance(odd_numbers(10), list), "odd_numbers should return a list"

def test_odd_numbers_function_signature():
    import inspect
    sig = inspect.signature(odd_numbers)
    params = list(sig.parameters.keys())
    assert len(params) == 1, f"odd_numbers should accept 1 parameter, got {len(params)}"
    assert params[0] in ['n', 'num', 'number', 'x'], f"Parameter name should be 'n' or similar, got '{params[0]}'" 