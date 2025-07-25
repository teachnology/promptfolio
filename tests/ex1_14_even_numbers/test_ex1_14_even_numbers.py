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
    result = even_numbers(10)
    assert result == [0, 2, 4, 6, 8], f"even_numbers(10) should be [0, 2, 4, 6, 8], got {result}"

def test_even_numbers_1():
    result = even_numbers(1)
    assert result == [0], f"even_numbers(1) should be [0], got {result}"

def test_even_numbers_2():
    result = even_numbers(2)
    assert result == [0], f"even_numbers(2) should be [0], got {result}"

def test_even_numbers_11():
    result = even_numbers(11)
    assert result == [0, 2, 4, 6, 8, 10], f"even_numbers(11) should be [0, 2, 4, 6, 8, 10], got {result}"

def test_even_numbers_0():
    result = even_numbers(0)
    assert result == [], f"even_numbers(0) should be [], got {result}"

def test_even_numbers_3():
    result = even_numbers(3)
    assert result == [0, 2], f"even_numbers(3) should be [0, 2], got {result}"

def test_even_numbers_6():
    result = even_numbers(6)
    assert result == [0, 2, 4], f"even_numbers(6) should be [0, 2, 4], got {result}"

def test_even_numbers_8():
    result = even_numbers(8)
    assert result == [0, 2, 4, 6], f"even_numbers(8) should be [0, 2, 4, 6], got {result}"

def test_even_numbers_20():
    result = even_numbers(20)
    assert result == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18], f"even_numbers(20) should be [0, 2, 4, 6, 8, 10, 12, 14, 16, 18], got {result}"

def test_even_numbers_large():
    res = even_numbers(100)
    assert res[0] == 0, f"even_numbers(100)[0] should be 0, got {res[0]}"
    assert res[-1] == 98, f"even_numbers(100)[-1] should be 98, got {res[-1]}"
    assert len(res) == 50, f"even_numbers(100) should be 50 elements, got {len(res)}"

def test_even_numbers_negative():
    try:
        result = even_numbers(-5)
        assert isinstance(result, list), f"even_numbers(-5) should be list, got {type(result).__name__}"
    except Exception:
        pass

def test_even_numbers_return_type():
    result = even_numbers(10)
    assert isinstance(result, list), f"even_numbers(10) should be list, got {type(result).__name__}"