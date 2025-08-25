import sys
import os
import math

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import calculate_pi
except ImportError:
    def calculate_pi(n):
        raise NotImplementedError("Function calculate_pi is not defined")

def test_calculate_pi_function_exists():
    assert callable(calculate_pi), "calculate_pi should be a callable function"

def test_calculate_pi_1():
    expected = 4
    result = calculate_pi(1)
    assert abs(result - expected) < 1e-6, f"calculate_pi(1) should be {expected}, but got {result}"

def test_calculate_pi_10():
    expected = 3.0418396189
    result = calculate_pi(10)
    assert abs(result - expected) < 1e-6, f"calculate_pi(10) should be {expected}, but got {result}"

def test_calculate_pi_1000():
    expected = math.pi
    result = calculate_pi(1000)
    assert abs(result - expected) < 1e-2, f"calculate_pi(1000) should be {expected}, but got {result}"

def test_calculate_pi_0():
    expected = 0
    result = calculate_pi(0)
    assert abs(result - expected) < 1e-6, f"calculate_pi(0) should be {expected}, but got {result}"

def test_calculate_pi_2():
    expected = 2.6666666667
    result = calculate_pi(2)
    assert abs(result - expected) < 1e-6, f"calculate_pi(2) should be {expected}, but got {result}"

def test_calculate_pi_5():
    expected = 3.3396825397
    result = calculate_pi(5)
    assert abs(result - expected) < 1e-6, f"calculate_pi(5) should be {expected}, but got {result}"

def test_calculate_pi_100():
    expected = 3.1315929036
    result = calculate_pi(100)
    assert abs(result - expected) < 1e-6, f"calculate_pi(100) should be {expected}, but got {result}"

def test_calculate_pi_large():
    val = calculate_pi(10000)
    assert abs(val - math.pi) < 1e-3, f"calculate_pi(10000) should be {math.pi}, but got {val}"

def test_calculate_pi_return_type():
    result = calculate_pi(10)
    assert isinstance(result, float), f"calculate_pi(10) should be float, but got {type(result).__name__}"