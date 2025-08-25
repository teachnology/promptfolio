import sys
import os

# Add current directory to Python path to import student code
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import num_digits
except ImportError:
    def num_digits(a):
        raise NotImplementedError("Function num_digits is not defined")

def test_num_digits_function_exists():
    assert callable(num_digits), "num_digits should be a callable function"

def test_num_digits_zero():
    result = num_digits(0)
    assert result == 1, f"num_digits(0) should be 1, got {result}"

def test_num_digits_five():
    result = num_digits(5)
    assert result == 1, f"num_digits(5) should be 1, got {result}"

def test_num_digits_seventy_three():
    result = num_digits(73)
    assert result == 2, f"num_digits(73) should be 2, got {result}"

def test_num_digits_large_number():
    result = num_digits(12345)
    assert result == 5, f"num_digits(12345) should be 5, got {result}"

def test_num_digits_nine_nines():
    result = num_digits(999999999)
    assert result == 9, f"num_digits(999999999) should be 9, got {result}"

def test_num_digits_one_hundred_thousand():
    result = num_digits(100000)
    assert result == 6, f"num_digits(100000) should be 6, got {result}"

def test_num_digits_negative():
    try:
        result = num_digits(-123)
        assert isinstance(result, int), f"num_digits(-123) should be int, got {type(result).__name__}"
    except Exception:
        pass

def test_num_digits_return_type():
    result = num_digits(123)
    assert isinstance(result, int), f"num_digits(123) should be int, got {type(result).__name__}"