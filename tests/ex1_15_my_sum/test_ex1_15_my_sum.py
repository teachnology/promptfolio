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
    result = my_sum([1, 3, 5, -5])
    assert result == 4, f"my_sum([1, 3, 5, -5]) should be 4, got {result}"

def test_my_sum_empty():
    result = my_sum([])
    assert result == 0, f"my_sum([]) should be 0, got {result}"

def test_my_sum_float():
    result = my_sum([2.1, 98, -451, 273, 1111, 23.98])
    assert abs(result - 1057.08) < 1e-2, f"my_sum([2.1, 98, -451, 273, 1111, 23.98]) should be 1057.08, got {result}"

def test_my_sum_large():
    result = my_sum(list(range(1, 101)))
    assert result == 5050, f"my_sum(range(1, 101)) should be 5050, got {result}"

def test_my_sum_0():
    result = my_sum([0])
    assert result == 0, f"my_sum([0]) should be 0, got {result}"

def test_my_sum_1_single():
    result = my_sum([1])
    assert result == 1, f"my_sum([1]) should be 1, got {result}"

def test_my_sum_123():
    result = my_sum([1, 2, 3])
    assert result == 6, f"my_sum([1, 2, 3]) should be 6, got {result}"

def test_my_sum_10_neg10_5():
    result = my_sum([10, -10, 5])
    assert result == 5, f"my_sum([10, -10, 5]) should be 5, got {result}"

def test_my_sum_negatives():
    result = my_sum([-1, -2, -3])
    assert result == -6, f"my_sum([-1, -2, -3]) should be -6, got {result}"

def test_my_sum_return_type():
    result = my_sum([1, 2, 3])
    assert isinstance(result, (int, float)), f"my_sum([1, 2, 3]) should be int or float, got {type(result).__name__}"
