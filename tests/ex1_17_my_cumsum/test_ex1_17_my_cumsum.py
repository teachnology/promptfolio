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

def test_my_cumsum_basic():
    assert my_cumsum([1, 4, 2, 5, 3]) == [1, 5, 7, 12, 15], "my_cumsum([1,4,2,5,3]) should return [1,5,7,12,15]"
    assert my_cumsum([]) == [], "my_cumsum([]) should return []"
    assert my_cumsum([0]) == [0], "my_cumsum([0]) should return [0]"

def test_my_cumsum_param():
    cases = [
        ([1, 2, 3], [1, 3, 6]),
        ([5, -2, 7], [5, 3, 10]),
        ([10, 0, 0, 10], [10, 10, 10, 20]),
        ([100], [100])
    ]
    for arr, expected in cases:
        assert my_cumsum(arr) == expected, f"my_cumsum({arr}) should return {expected}"

def test_my_cumsum_large():
    arr = list(range(100))
    out = my_cumsum(arr)
    assert out[-1] == sum(arr)
    assert len(out) == 100

def test_my_cumsum_return_type():
    assert isinstance(my_cumsum([1, 2, 3]), list), "my_cumsum should return a list"

def test_my_cumsum_function_signature():
    import inspect
    sig = inspect.signature(my_cumsum)
    params = list(sig.parameters.keys())
    assert len(params) == 1, f"my_cumsum should accept 1 parameter, got {len(params)}"
    assert params[0] in ['x', 'lst', 'arr', 'numbers'], f"Parameter name should be 'x' or similar, got '{params[0]}'" 