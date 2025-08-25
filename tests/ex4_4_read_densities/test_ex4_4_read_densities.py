import sys
import os
import numbers
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Ensure densities data file exists at runtime by copying bundled assets
ASSET_PATH = os.path.join(os.path.dirname(__file__), "data", "densities.dat")
RUNTIME_DIR = os.path.join("data")
RUNTIME_PATH = os.path.join(RUNTIME_DIR, "densities.dat")

os.makedirs(RUNTIME_DIR, exist_ok=True)
if not os.path.exists(RUNTIME_PATH):
    if os.path.exists(ASSET_PATH):
        with open(ASSET_PATH, "r", encoding="utf-8") as fin, open(RUNTIME_PATH, "w", encoding="utf-8") as fout:
            fout.write(fin.read())
    else:
        raise FileNotFoundError("Bundled test data not found: " + ASSET_PATH)


try:
    from submission import read_densities_join, read_densities_substrings
except ImportError:
    def read_densities_join(filename):
        raise NotImplementedError("Function read_densities_join is not defined")
    def read_densities_substrings(filename):
        raise NotImplementedError("Function read_densities_substrings is not defined")


def test_densities_results_and_values():
    res_join = read_densities_join(os.path.join("data", "densities.dat"))
    res_sub = read_densities_substrings(os.path.join("data", "densities.dat"))

    assert "Earth_core" in res_join.keys(), 'Key "Earth_core" should be present in join result'
    assert np.isclose(res_join["gold"], 18.9), f"gold density (join) should be 18.9, got {res_join['gold']}"

    assert "Earth_core" in res_sub.keys(), 'Key "Earth_core" should be present in substrings result'
    assert np.isclose(res_sub["gold"], 18.9), f"gold density (substrings) should be 18.9, got {res_sub['gold']}"


def test_densities_types_and_length():
    res_join = read_densities_join(os.path.join("data", "densities.dat"))
    res_sub = read_densities_substrings(os.path.join("data", "densities.dat"))

    assert isinstance(res_join, dict) and isinstance(res_sub, dict), "Both functions should return dict"
    assert all(isinstance(k, str) and isinstance(v, numbers.Real) for k, v in res_join.items()), "join result types invalid"
    assert all(isinstance(k, str) and isinstance(v, numbers.Real) for k, v in res_sub.items()), "substrings result types invalid"
    assert len(res_join) == 19 and len(res_sub) == 19, f"Both results should contain 19 entries, got {len(res_join)} and {len(res_sub)}"


