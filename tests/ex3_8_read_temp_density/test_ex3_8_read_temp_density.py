import sys
import os
import numbers

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Ensure test data files exist at runtime by copying from bundled assets under this test folder
ASSET_DIR = os.path.join(os.path.dirname(__file__), "data")
RUNTIME_DIR = os.path.join("data")
os.makedirs(RUNTIME_DIR, exist_ok=True)

for fname in ("density_air.dat", "density_water.dat"):
    src = os.path.join(ASSET_DIR, fname)
    dst = os.path.join(RUNTIME_DIR, fname)
    if not os.path.exists(dst):
        if not os.path.exists(src):
            raise FileNotFoundError("Bundled test data not found: " + src)
        with open(src, "r", encoding="utf-8") as fin, open(dst, "w", encoding="utf-8") as fout:
            fout.write(fin.read())


try:
    from submission import readTempDenFile
except ImportError:
    def readTempDenFile(filename):
        raise NotImplementedError("Function readTempDenFile is not defined")


def _try_import(name):
    try:
        module = __import__("submission", fromlist=[name])
        return getattr(module, name)
    except Exception:
        return None


temp_air_list = _try_import("temp_air_list")
dens_air_list = _try_import("dens_air_list")
temp_water_list = _try_import("temp_water_list")
dens_water_list = _try_import("dens_water_list")


def test_function_returns_lists():
    air = readTempDenFile(os.path.join("data", "density_air.dat"))
    water = readTempDenFile(os.path.join("data", "density_water.dat"))
    assert isinstance(air, tuple) and len(air) == 2, f"readTempDenFile should return a (temps, dens) tuple, got {type(air).__name__}"
    assert isinstance(water, tuple) and len(water) == 2, f"readTempDenFile should return a (temps, dens) tuple, got {type(water).__name__}"
    assert all(isinstance(i, list) for i in air), "Both elements for air should be lists"
    assert all(isinstance(i, list) for i in water), "Both elements for water should be lists"


def test_air_water_values_and_lengths():
    air_t, air_d = readTempDenFile(os.path.join("data", "density_air.dat"))
    water_t, water_d = readTempDenFile(os.path.join("data", "density_water.dat"))

    assert air_t[0] == -10 and air_d[0] == 1.341, f"Air first row should be (-10, 1.341), got ({air_t[0]}, {air_d[0]})"
    assert air_t[-1] == 30 and abs(air_d[-1] - 1.164) < 1e-12, f"Air last row density should be 1.164, got {air_d[-1]}"
    assert len(air_t) == len(air_d) == 9, f"Air arrays should have length 9, got {len(air_t)} and {len(air_d)}"

    assert abs(water_t[0] - 0.0) < 1e-12 and abs(water_d[0] - 999.8425) < 1e-12, f"Water first row should be (0.0, 999.8425), got ({water_t[0]}, {water_d[0]})"
    assert abs(water_t[-1] - 100.0) < 1e-12 and abs(water_d[-1] - 958.3665) < 1e-12, f"Water last row should be (100.0, 958.3665), got ({water_t[-1]}, {water_d[-1]})"


def test_global_lists_exist_and_match():
    assert isinstance(temp_air_list, list), f"temp_air_list should be a list, got {type(temp_air_list).__name__}"
    assert isinstance(dens_air_list, list), f"dens_air_list should be a list, got {type(dens_air_list).__name__}"
    assert isinstance(temp_water_list, list), f"temp_water_list should be a list, got {type(temp_water_list).__name__}"
    assert isinstance(dens_water_list, list), f"dens_water_list should be a list, got {type(dens_water_list).__name__}"

    air_t, air_d = readTempDenFile(os.path.join("data", "density_air.dat"))
    water_t, water_d = readTempDenFile(os.path.join("data", "density_water.dat"))

    assert temp_air_list == air_t, f"temp_air_list should equal temperatures from the file, got {temp_air_list}"
    assert dens_air_list == air_d, f"dens_air_list should equal densities from the file, got {dens_air_list}"
    assert temp_water_list == water_t, f"temp_water_list should equal temperatures from the file, got {temp_water_list}"
    assert dens_water_list == water_d, f"dens_water_list should equal densities from the file, got {dens_water_list}"


def test_values_are_numbers():
    air_t, air_d = readTempDenFile(os.path.join("data", "density_air.dat"))
    assert all(isinstance(v, numbers.Real) for v in air_t), "Temperatures should be numbers"
    assert all(isinstance(v, numbers.Real) for v in air_d), "Densities should be numbers"


