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

def test_my_sum_basic():
    assert my_sum([1, 3, 5, -5]) == 4, "my_sum([1,3,5,-5]) should return 4"
    assert my_sum([]) == 0, "my_sum([]) should return 0"
    assert abs(my_sum([2.1, 98, -451, 273, 1111, 23.98]) - 1057.08) < 1e-2

def test_my_sum_large():
    assert my_sum(list(range(1, 101))) == 5050, "my_sum(range(1,101)) should return 5050"

def test_my_sum_param():
    cases = [
        ([0], 0), ([1], 1), ([1, 2, 3], 6), ([10, -10, 5], 5), ([-1, -2, -3], -6)
    ]
    for arr, expected in cases:
        assert my_sum(arr) == expected, f"my_sum({arr}) should return {expected}"

def test_my_sum_return_type():
    assert isinstance(my_sum([1, 2, 3]), (int, float)), "my_sum should return int or float"

def test_my_sum_function_signature():
    import inspect
    sig = inspect.signature(my_sum)
    params = list(sig.parameters.keys())
    assert len(params) == 1, f"my_sum should accept 1 parameter, got {len(params)}"
    assert params[0] in ['x', 'lst', 'arr', 'numbers'], f"Parameter name should be 'x' or similar, got '{params[0]}'" 