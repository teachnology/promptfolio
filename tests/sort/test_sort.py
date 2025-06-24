import pytest
import sys
import os
from typing import List

# Add current directory to Python path to import student code
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Import student submitted function
try:
    from submission import bubble_sort
except ImportError:
    # If import fails, create a placeholder function
    def bubble_sort(arr):
        raise NotImplementedError("Function bubble_sort is not defined")

def test_bubble_sort_function_exists():
    """Test if function exists"""
    assert callable(bubble_sort), "bubble_sort should be a callable function"

def test_bubble_sort_empty_list():
    """Test empty list"""
    result = bubble_sort([])
    assert result == [], f"bubble_sort([]) should return [], but got {result}"

def test_bubble_sort_single_element():
    """Test single element list"""
    result = bubble_sort([1])
    assert result == [1], f"bubble_sort([1]) should return [1], but got {result}"

def test_bubble_sort_sorted_list():
    """Test already sorted list"""
    result = bubble_sort([1, 2, 3, 4, 5])
    assert result == [1, 2, 3, 4, 5], f"bubble_sort([1,2,3,4,5]) should return [1,2,3,4,5], but got {result}"

def test_bubble_sort_reverse_list():
    """Test reverse sorted list"""
    result = bubble_sort([5, 4, 3, 2, 1])
    assert result == [1, 2, 3, 4, 5], f"bubble_sort([5,4,3,2,1]) should return [1,2,3,4,5], but got {result}"

def test_bubble_sort_duplicate_elements():
    """Test list with duplicate elements"""
    result = bubble_sort([3, 1, 4, 1, 5, 9, 2, 6])
    assert result == [1, 1, 2, 3, 4, 5, 6, 9], f"bubble_sort([3,1,4,1,5,9,2,6]) should return [1,1,2,3,4,5,6,9], but got {result}"

def test_bubble_sort_negative_numbers():
    """Test list with negative numbers"""
    result = bubble_sort([-3, 1, -4, 1, -5, 9, -2, 6])
    assert result == [-5, -4, -3, -2, 1, 1, 6, 9], f"bubble_sort([-3,1,-4,1,-5,9,-2,6]) should return [-5,-4,-3,-2,1,1,6,9], but got {result}"

@pytest.mark.parametrize("input_list,expected", [
    ([], []),
    ([1], [1]),
    ([2, 1], [1, 2]),
    ([3, 2, 1], [1, 2, 3]),
    ([1, 2, 3], [1, 2, 3]),
    ([3, 1, 4, 1, 5], [1, 1, 3, 4, 5]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9])
])
def test_bubble_sort_various_inputs(input_list, expected):
    """Parameterized test: verify various inputs"""
    result = bubble_sort(input_list)
    assert result == expected, f"bubble_sort({input_list}) should return {expected}, but got {result}"

def test_bubble_sort_does_not_modify_original():
    """Test that function doesn't modify original list"""
    original = [3, 1, 4, 1, 5]
    result = bubble_sort(original)
    assert original == [3, 1, 4, 1, 5], "bubble_sort should not modify the original list"
    assert result == [1, 1, 3, 4, 5], "bubble_sort should return a new sorted list"

def test_bubble_sort_function_signature():
    """Test function signature"""
    import inspect
    sig = inspect.signature(bubble_sort)
    params = list(sig.parameters.keys())
    
    assert len(params) == 1, f"bubble_sort function should accept 1 parameter, but accepts {len(params)}"
    assert params[0] in ['arr', 'list', 'nums', 'numbers', 'data'], f"Parameter name should be 'arr', but got '{params[0]}'"

def test_bubble_sort_return_type():
    """Test return value type"""
    result = bubble_sort([3, 1, 4])
    assert isinstance(result, list), f"bubble_sort should return a list, but returned {type(result).__name__}"

def test_bubble_sort_large_list():
    """Test performance with large list"""
    large_list = list(range(100, 0, -1))  # [100, 99, 98, ..., 1]
    expected = list(range(1, 101))  # [1, 2, 3, ..., 100]
    
    try:
        result = bubble_sort(large_list)
        assert result == expected, f"bubble_sort result incorrect for large list"
    except RecursionError:
        pytest.fail("bubble_sort caused recursion error with large list")
    except Exception as e:
        pytest.fail(f"bubble_sort raised exception with large list: {type(e).__name__}: {e}")

def test_bubble_sort_with_strings():
    """Test with string list (should fail)"""
    try:
        result = bubble_sort(['c', 'a', 'b'])
        # If function can handle strings, check result
        assert isinstance(result, list), "Return value should be a list"
    except TypeError:
        # This is acceptable since the problem requires handling integer lists
        pass
    except Exception as e:
        pytest.fail(f"Unexpected exception when handling string list: {type(e).__name__}: {e}") 