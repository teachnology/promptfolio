import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from submission import reverse_dict
except ImportError:
    def reverse_dict(dictionary):
        raise NotImplementedError("Function reverse_dict is not defined")


def test_reverse_dict_sample():
    res = reverse_dict({"dog": "Hund", "cat": "Katze", "house": "Haus", "bicycle": "Fahrrad"})
    assert "Katze" in res.keys(), 'Key "Katze" should be present'
    assert res.get("Hund") == "dog", f"res['Hund'] should be 'dog', got {res.get('Hund')}"


def test_reverse_dict_types_and_length():
    res = reverse_dict({"a": "b", "c": "d", "e": "f", "g": "h"})
    assert isinstance(res, dict), f"reverse_dict should return a dict, got {type(res).__name__}"
    assert all(isinstance(k, str) and isinstance(v, str) for k, v in res.items()), "Keys and values should be strings"
    assert len(res) == 4, f"Result should contain 4 pairs, got {len(res)}"


