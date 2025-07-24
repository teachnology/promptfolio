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
    assert odd_numbers(10) == [1, 3, 5, 7, 9], "odd_numbers(10) should return [1, 3, 5, 7, 9]"

def test_odd_numbers_one():
    assert odd_numbers(1) == [], "odd_numbers(1) should return []"

def test_odd_numbers_two():
    assert odd_numbers(2) == [1], "odd_numbers(2) should return [1]"

def test_odd_numbers_fifteen():
    assert odd_numbers(15) == [1, 3, 5, 7, 9, 11, 13], "odd_numbers(15) should return [1, 3, 5, 7, 9, 11, 13]"

def test_odd_numbers_negative():
    try:
        result = odd_numbers(-5)
        assert isinstance(result, list), "odd_numbers(-5) should return a list or raise"
    except Exception:
        pass

def test_odd_numbers_0():
    assert odd_numbers(0) == [], "odd_numbers(0) should return []"

def test_odd_numbers_3():
    assert odd_numbers(3) == [1], "odd_numbers(3) should return [1]"

def test_odd_numbers_5():
    assert odd_numbers(5) == [1, 3], "odd_numbers(5) should return [1, 3]"

def test_odd_numbers_8():
    assert odd_numbers(8) == [1, 3, 5, 7], "odd_numbers(8) should return [1, 3, 5, 7]"

def test_odd_numbers_20():
    assert odd_numbers(20) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], "odd_numbers(20) should return [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]"

def test_odd_numbers_return_type():
    assert isinstance(odd_numbers(10), list), "odd_numbers(10) should return a list"