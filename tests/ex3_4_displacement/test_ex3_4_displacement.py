import sys
import os
import numbers

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import displacement
except ImportError:
    def displacement(*args, **kwargs):
        raise NotImplementedError("Function displacement is not defined")


def test_displacement_exists():
    assert callable(displacement), "displacement should be a callable function"


def test_displacement_basic_values():
    result = displacement(t=0, v0=0, g=0)
    assert result == 0, f"displacement(0, 0, 0) should be 0, got {result}"

    result = displacement(t=1, v0=1, g=1)
    assert abs(result - 0.5) < 1e-12, f"displacement(1, 1, 1) should be 0.5, got {result}"


def test_displacement_negative_inputs_raise():
    import pytest
    with pytest.raises(ValueError):
        displacement(t=-5, v0=0, g=0)
    with pytest.raises(ValueError):
        displacement(t=10, v0=-10, g=10)


def test_displacement_return_type():
    result = displacement(t=0, v0=0, g=0)
    assert isinstance(result, numbers.Real), f"displacement(0, 0, 0) should be a real number, got {type(result).__name__}"


