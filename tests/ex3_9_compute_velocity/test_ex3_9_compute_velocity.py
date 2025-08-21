import sys
import os
import numbers
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Ensure acceleration data file exists at runtime by copying a bundled test asset
ASSET_PATH = os.path.join(os.path.dirname(__file__), "data", "acc.dat")
RUNTIME_DIR = os.path.join("data")
RUNTIME_PATH = os.path.join(RUNTIME_DIR, "acc.dat")

os.makedirs(RUNTIME_DIR, exist_ok=True)
if not os.path.exists(RUNTIME_PATH):
    if os.path.exists(ASSET_PATH):
        with open(ASSET_PATH, "r", encoding="utf-8") as fin, open(RUNTIME_PATH, "w", encoding="utf-8") as fout:
            fout.write(fin.read())
    else:
        raise FileNotFoundError("Bundled test data not found: " + ASSET_PATH)


try:
    from submission import compute_velocity
except ImportError:
    def compute_velocity(dt, k, a):
        raise NotImplementedError("Function compute_velocity is not defined")


def _try_import(name):
    try:
        module = __import__("submission", fromlist=[name])
        return getattr(module, name)
    except Exception:
        return None


time_array = _try_import("time_array")
acc_array = _try_import("acc_array")


def test_compute_velocity_basic():
    assert compute_velocity(1, 3, [1, 1, 1, 1]) == 3, f"compute_velocity(1, 3, [1,1,1,1]) should be 3, got {compute_velocity(1, 3, [1,1,1,1])}"
    assert compute_velocity(1, 3, [0, 0, 0, 0]) == 0, f"compute_velocity(1, 3, [0,0,0,0]) should be 0, got {compute_velocity(1, 3, [0,0,0,0])}"


def test_arrays_exist_and_shapes():
    assert isinstance(acc_array, np.ndarray), f"acc_array should be a numpy array, got {type(acc_array).__name__}"
    assert isinstance(time_array, np.ndarray), f"time_array should be a numpy array, got {type(time_array).__name__}"
    assert acc_array.shape == (101,), f"acc_array should have shape (101,), got {acc_array.shape}"
    assert time_array.shape == (101,), f"time_array should have shape (101,), got {time_array.shape}"


def test_arrays_values_and_types():
    assert np.isclose(acc_array[0], -0.00506375204384), f"acc_array[0] should be -0.00506375204384, got {acc_array[0]}"
    assert np.isclose(acc_array[-1], 0.479565276825), f"acc_array[-1] should be 0.479565276825, got {acc_array[-1]}"
    assert np.isclose(time_array[0], 0.0), f"time_array[0] should be 0.0, got {time_array[0]}"
    assert np.isclose(time_array[-1], 50.0), f"time_array[-1] should be 50.0 for dt=0.5 and 101 points, got {time_array[-1]}"
    assert all(isinstance(v, numbers.Real) for v in time_array), "time_array values should be numbers"
    assert all(isinstance(v, numbers.Real) for v in acc_array), "acc_array values should be numbers"


