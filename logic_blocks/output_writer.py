import json
import os

def write_output(filename: str, data: dict):
    os.makedirs("outputs", exist_ok=True)
    filepath = os.path.join("outputs", filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return filepath
