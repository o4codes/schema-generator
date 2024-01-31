import tempfile
import json


def write_json_to_temp_file(data: dict):
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(data, f)
        f.seek(0)
        return f