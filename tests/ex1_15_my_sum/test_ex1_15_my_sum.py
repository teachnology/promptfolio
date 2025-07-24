import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import my_sum
except ImportError:
    def my_sum(x):
        raise NotImplementedError("Function my_sum is not defined")

def test_my_sum_function_exists():
    assert callable(my_sum), "my_sum should be a callable function"

def test_my_sum_1():
    assert my_sum([1, 3, 5, -5]) == 4, "my_sum([1, 3, 5, -5]) should be 4"

def test_my_sum_empty():
    assert my_sum([]) == 0, "my_sum([]) should be 0"

def test_my_sum_float():
    assert abs(my_sum([2.1, 98, -451, 273, 1111, 23.98]) - 1057.08) < 1e-2, "my_sum([2.1, 98, -451, 273, 1111, 23.98]) should be 1057.08"

def test_my_sum_large():
    assert my_sum(list(range(1, 101))) == 5050, "my_sum(range(1, 101)) should be 5050"

def test_my_sum_0():
    assert my_sum([0]) == 0, "my_sum([0]) should be 0"

def test_my_sum_1_single():
    assert my_sum([1]) == 1, "my_sum([1]) should be 1"

def test_my_sum_123():
    assert my_sum([1, 2, 3]) == 6, "my_sum([1, 2, 3]) should be 6"

def test_my_sum_10_neg10_5():
    assert my_sum([10, -10, 5]) == 5, "my_sum([10, -10, 5]) should be 5"

def test_my_sum_negatives():
    assert my_sum([-1, -2, -3]) == -6, "my_sum([-1, -2, -3]) should be -6"

def test_my_sum_return_type():
    assert isinstance(my_sum([1, 2, 3]), (int, float)), "my_sum([1, 2, 3]) should be int or float"
