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
    result = my_cumsum([1, 4, 2, 5, 3])
    assert result == [1, 5, 7, 12, 15], f"my_cumsum([1, 4, 2, 5, 3]) should be [1, 5, 7, 12, 15], got {result}"

def test_my_cumsum_empty():
    result = my_cumsum([])
    assert result == [], f"my_cumsum([]) should be [], got {result}"

def test_my_cumsum_0():
    result = my_cumsum([0])
    assert result == [0], f"my_cumsum([0]) should be [0], got {result}"

def test_my_cumsum_123():
    result = my_cumsum([1, 2, 3])
    assert result == [1, 3, 6], f"my_cumsum([1, 2, 3]) should be [1, 3, 6], got {result}"

def test_my_cumsum_5_neg2_7():
    result = my_cumsum([5, -2, 7])
    assert result == [5, 3, 10], f"my_cumsum([5, -2, 7]) should be [5, 3, 10], got {result}"

def test_my_cumsum_10_0_0_10():
    result = my_cumsum([10, 0, 0, 10])
    assert result == [10, 10, 10, 20], f"my_cumsum([10, 0, 0, 10]) should be [10, 10, 10, 20], got {result}"

def test_my_cumsum_100():
    result = my_cumsum([100])
    assert result == [100], f"my_cumsum([100]) should be [100], got {result}"

def test_my_cumsum_large():
    arr = list(range(100))
    out = my_cumsum(arr)
    assert out[-1] == sum(arr), f"my_cumsum(range(100))[-1] should be {sum(arr)}, got {out[-1]}"
    assert len(out) == 100, f"my_cumsum(range(100)) should be 100 elements, got {len(out)}"

def test_my_cumsum_return_type():
    result = my_cumsum([1, 2, 3])
    assert isinstance(result, list), f"my_cumsum([1, 2, 3]) should be list, got {type(result).__name__}"
