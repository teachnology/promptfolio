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
    expected = 31603718.929927427  # 1 Earth year in seconds
    result = period(a, m_earth)
    assert abs(result - expected) < 1e3, f"period(earth) should be about {expected}, got {result}"

def test_period_mars():
    a_earth = 1.5e11
    a_mars = 1.5 * a_earth
    m_earth = 6e24
    m_mars = 0.1 * m_earth
    expected = 58059817.3950661  # Mars year in seconds
    result = period(a_mars, m_mars)
    assert abs(result - expected) < 1e3, f"period(mars) should be about {expected}, got {result}"

def test_period_param():
    cases = [
        (1e11, 1e24, 2e30, 6.67e-11, 18229576.0),
        (2e11, 1e24, 2e30, 6.67e-11, 51569713.0)
    ]
    for a, m, M, G, expected in cases:
        result = period(a, m, M, G)
        assert abs(result - expected) < 1e3

def test_period_large():
    a = 1e12
    m = 1e25
    result = period(a, m)
    assert result > 0

def test_period_return_type():
    a = 1.5e11
    m = 6e24
    result = period(a, m)
    assert isinstance(result, float), "period should return a float"

def test_period_function_signature():
    import inspect
    sig = inspect.signature(period)
    params = list(sig.parameters.keys())
    assert params[:2] == ['a', 'm_planet'], f"period should have (a, m_planet, ...) as parameters, got {params}" 