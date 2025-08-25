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

def test_odd_numbers_ten():
    result = odd_numbers(10)
    assert result == [1, 3, 5, 7, 9], f"odd_numbers(10) should be [1, 3, 5, 7, 9], got {result}"

def test_odd_numbers_one():
    result = odd_numbers(1)
    assert result == [], f"odd_numbers(1) should be [], got {result}"

def test_odd_numbers_two():
    result = odd_numbers(2)
    assert result == [1], f"odd_numbers(2) should be [1], got {result}"

def test_odd_numbers_fifteen():
    result = odd_numbers(15)
    assert result == [1, 3, 5, 7, 9, 11, 13], f"odd_numbers(15) should be [1, 3, 5, 7, 9, 11, 13], got {result}"

def test_odd_numbers_negative():
    try:
        result = odd_numbers(-5)
        assert isinstance(result, list), f"odd_numbers(-5) should be list, got {type(result).__name__}"
    except Exception:
        pass

def test_odd_numbers_0():
    result = odd_numbers(0)
    assert result == [], f"odd_numbers(0) should be [], got {result}"

def test_odd_numbers_3():
    result = odd_numbers(3)
    assert result == [1], f"odd_numbers(3) should be [1], got {result}"

def test_odd_numbers_5():
    result = odd_numbers(5)
    assert result == [1, 3], f"odd_numbers(5) should be [1, 3], got {result}"

def test_odd_numbers_8():
    result = odd_numbers(8)
    assert result == [1, 3, 5, 7], f"odd_numbers(8) should be [1, 3, 5, 7], got {result}"

def test_odd_numbers_20():
    result = odd_numbers(20)
    assert result == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], f"odd_numbers(20) should be [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], got {result}"

def test_odd_numbers_return_type():
    result = odd_numbers(10)
    assert isinstance(result, list), f"odd_numbers(10) should be list, got {type(result).__name__}"