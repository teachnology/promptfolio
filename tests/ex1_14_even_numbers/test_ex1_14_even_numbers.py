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

def test_even_numbers_10():
    assert even_numbers(10) == [0, 2, 4, 6, 8], "even_numbers(10) should be [0, 2, 4, 6, 8]"

def test_even_numbers_1():
    assert even_numbers(1) == [0], "even_numbers(1) should be [0]"

def test_even_numbers_2():
    assert even_numbers(2) == [0], "even_numbers(2) should be [0]"

def test_even_numbers_11():
    assert even_numbers(11) == [0, 2, 4, 6, 8, 10], "even_numbers(11) should be [0, 2, 4, 6, 8, 10]"

def test_even_numbers_0():
    assert even_numbers(0) == [], "even_numbers(0) should be []"

def test_even_numbers_3():
    assert even_numbers(3) == [0, 2], "even_numbers(3) should be [0, 2]"

def test_even_numbers_6():
    assert even_numbers(6) == [0, 2, 4], "even_numbers(6) should be [0, 2, 4]"

def test_even_numbers_8():
    assert even_numbers(8) == [0, 2, 4, 6], "even_numbers(8) should be [0, 2, 4, 6]"

def test_even_numbers_20():
    assert even_numbers(20) == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18], "even_numbers(20) should be [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]"

def test_even_numbers_large():
    res = even_numbers(100)
    assert res[0] == 0, "even_numbers(100)[0] should be 0"
    assert res[-1] == 98, "even_numbers(100)[-1] should be 98"
    assert len(res) == 50, "even_numbers(100) should be 50 elements"

def test_even_numbers_negative():
    try:
        result = even_numbers(-5)
        assert isinstance(result, list), "even_numbers(-5) should be a list or raise"
    except Exception:
        pass

def test_even_numbers_return_type():
    assert isinstance(even_numbers(10), list), "even_numbers(10) should be a list"