import sys
import os
import numbers
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Ensure constants data file exists at runtime by copying a bundled test asset
ASSET_PATH = os.path.join(os.path.dirname(__file__), "data", "constants.txt")
RUNTIME_DIR = os.path.join("data")
RUNTIME_PATH = os.path.join(RUNTIME_DIR, "constants.txt")

os.makedirs(RUNTIME_DIR, exist_ok=True)
if not os.path.exists(RUNTIME_PATH):
    if os.path.exists(ASSET_PATH):
        with open(ASSET_PATH, "r", encoding="utf-8") as fin, open(RUNTIME_PATH, "w", encoding="utf-8") as fout:
            fout.write(fin.read())
    else:
        raise FileNotFoundError("Bundled test data not found: " + ASSET_PATH)


try:
    from submission import read_constants
except ImportError:
    def read_constants(file_path):
        raise NotImplementedError("Function read_constants is not defined")


def test_read_constants_result():
    res = read_constants(os.path.join("data", "constants.txt"))
    assert isinstance(res, dict), f"read_constants should return a dict, got {type(res).__name__}"
    assert "Avogadro number" in res.keys(), 'Key "Avogadro number" should be present'
    assert np.isclose(res.get("speed of light", float('nan')), 299792458.0), f"speed of light should be 299792458.0, got {res.get('speed of light')}"


def test_read_constants_types_and_length():
    res = read_constants(os.path.join("data", "constants.txt"))
    assert all(isinstance(k, str) and isinstance(v, numbers.Real) for k, v in res.items()), "Keys should be str and values should be numbers"
    assert len(res) == 8, f"Result should contain 8 constants, got {len(res)}"


