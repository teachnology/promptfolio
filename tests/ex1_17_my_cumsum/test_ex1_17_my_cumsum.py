import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import my_cumsum
except ImportError:
    def my_cumsum(x):
        raise NotImplementedError("Function my_cumsum is not defined")

def test_my_cumsum_function_exists():
    assert callable(my_cumsum), "my_cumsum should be a callable function"

def test_my_cumsum_1():
    assert my_cumsum([1, 4, 2, 5, 3]) == [1, 5, 7, 12, 15], "my_cumsum([1, 4, 2, 5, 3]) should be [1, 5, 7, 12, 15]"

def test_my_cumsum_empty():
    assert my_cumsum([]) == [], "my_cumsum([]) should be []"

def test_my_cumsum_0():
    assert my_cumsum([0]) == [0], "my_cumsum([0]) should be [0]"

def test_my_cumsum_123():
    assert my_cumsum([1, 2, 3]) == [1, 3, 6], "my_cumsum([1, 2, 3]) should be [1, 3, 6]"

def test_my_cumsum_5_neg2_7():
    assert my_cumsum([5, -2, 7]) == [5, 3, 10], "my_cumsum([5, -2, 7]) should be [5, 3, 10]"

def test_my_cumsum_10_0_0_10():
    assert my_cumsum([10, 0, 0, 10]) == [10, 10, 10, 20], "my_cumsum([10, 0, 0, 10]) should be [10, 10, 10, 20]"

def test_my_cumsum_100():
    assert my_cumsum([100]) == [100], "my_cumsum([100]) should be [100]"

def test_my_cumsum_large():
    arr = list(range(100))
    out = my_cumsum(arr)
    assert out[-1] == sum(arr), f"my_cumsum(range(100))[-1] should be {sum(arr)}"
    assert len(out) == 100, "my_cumsum(range(100)) should be 100 elements"

def test_my_cumsum_return_type():
    assert isinstance(my_cumsum([1, 2, 3]), list), "my_cumsum([1, 2, 3]) should be a list"
