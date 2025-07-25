import sys
import os
import math

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import path_length
except ImportError:
    def path_length(x, y):
        raise NotImplementedError("Function path_length is not defined")

def test_path_length_straight():
    result = path_length([0, 0, 0, 0, 0], [0, 1, 2, 3, 4])
    assert math.isclose(result, 4), f"path_length([0,0,0,0,0],[0,1,2,3,4]) should be 4, got {result}"

def test_path_length_zero():
    result = path_length([0, 0, 0, 0, 0], [0, 0, 0, 0, 0])
    assert math.isclose(result, 0), f"path_length([0,0,0,0,0],[0,0,0,0,0]) should be 0, got {result}"

def test_path_length_triangle():
    result = path_length([1, 2, 1, 1], [1, 1, 2, 1])
    expected = 1 + math.sqrt(2) + 1
    assert math.isclose(result, expected), f"path_length([1,2,1,1],[1,1,2,1]) should be {expected}, got {result}"

def test_path_length_function_signature():
    import inspect
    sig = inspect.signature(path_length)
    params = list(sig.parameters.keys())
    assert params == ['x', 'y'], "path_length function should have parameters (x, y)"

def test_path_length_return_type():
    result = path_length([0, 1], [0, 1])
    assert isinstance(result, float) or isinstance(result, int), f"path_length([0,1],[0,1]) should return float or int, got {type(result).__name__}" 