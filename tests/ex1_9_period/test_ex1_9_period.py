import sys
import os
import math

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import period
except ImportError:
    def period(a, m_planet, m_sun=2e30, G=6.67e-11):
        raise NotImplementedError("Function period is not defined")

def test_period_function_exists():
    assert callable(period), "period should be a callable function"

def test_period_earth():
    a = 1.5e11
    m_earth = 6e24
    expected = 31603718.929927427
    result = period(a, m_earth)
    assert abs(result - expected) < 1e3, f"period(1.5e11, 6e24) should be {expected}, got {result}"

def test_period_mars():
    a_earth = 1.5e11
    a_mars = 1.5 * a_earth
    m_earth = 6e24
    m_mars = 0.1 * m_earth
    expected = 58059817.3950661
    result = period(a_mars, m_mars)
    assert abs(result - expected) < 1e3, f"period({a_mars}, {m_mars}) should be {expected}, got {result}"

def test_period_large():
    a = 1e12
    m = 1e25
    result = period(a, m)
    assert result > 0, f"period(1e12, 1e25) should be positive, got {result}"

def test_period_return_type():
    a = 1.5e11
    m = 6e24
    result = period(a, m)
    assert isinstance(result, float), f"period(1.5e11, 6e24) should be float, got {type(result).__name__}" 