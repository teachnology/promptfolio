import sys
import os
import math
import numbers

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Accept either compute_wave_speeds or wave_speeds
compute = None
try:
    from submission import calc_material_velocity as compute
except ImportError:
    def compute(*args, **kwargs):
        raise NotImplementedError("Function calc_material_velocity is not defined")


def test_wave_speeds_exists():
    assert callable(compute), "compute_wave_speeds should be a callable function"


def test_wave_speeds_values():
    k = 140e9
    mu = 80e9
    rho = 2700.0
    vp, vs = compute(k, mu, rho)

    expected_vs = math.sqrt(mu / rho)
    expected_vp = math.sqrt((k + (4.0 * mu) / 3.0) / rho)

    assert abs(vs - expected_vs) < 1e-6 * max(1.0, expected_vs), f"Vs should be {expected_vs}, got {vs}"
    assert abs(vp - expected_vp) < 1e-6 * max(1.0, expected_vp), f"Vp should be {expected_vp}, got {vp}"


def test_wave_speeds_input_validation():
    import pytest
    with pytest.raises(ValueError):
        compute(1.0, 1.0, -1.0)
    with pytest.raises(ValueError):
        compute(-1.0, 1.0, 1000.0)
    with pytest.raises(ValueError):
        compute(1.0, -1.0, 1000.0)


def test_wave_speeds_return_types():
    k = 10.0
    mu = 5.0
    rho = 1000.0
    vp, vs = compute(k, mu, rho)
    assert isinstance(vp, numbers.Real), f"Vp should be a real number, got {type(vp).__name__}"
    assert isinstance(vs, numbers.Real), f"Vs should be a real number, got {type(vs).__name__}"


