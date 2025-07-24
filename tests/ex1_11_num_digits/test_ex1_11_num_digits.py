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
    assert num_digits(0) == 1, "num_digits(0) should return 1"

def test_num_digits_five():
    assert num_digits(5) == 1, "num_digits(5) should return 1"

def test_num_digits_seventy_three():
    assert num_digits(73) == 2, "num_digits(73) should return 2"

def test_num_digits_large_number():
    assert num_digits(12345) == 5, "num_digits(12345) should return 5"

def test_num_digits_nine_nines():
    assert num_digits(999999999) == 9, "num_digits(999999999) should return 9"

def test_num_digits_one_hundred_thousand():
    assert num_digits(100000) == 6, "num_digits(100000) should return 6"

def test_num_digits_negative():
    try:
        result = num_digits(-123)
        assert isinstance(result, int), "num_digits(-123) should return an integer or raise"
    except Exception:
        pass

def test_num_digits_return_type():
    assert isinstance(num_digits(123), int), "num_digits(123) should return an integer"