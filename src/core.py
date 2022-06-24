
import json
import os


here = os.path.abspath(os.path.dirname(__file__))

def load_json(file_name: str):
    with open(f"{here}/{file_name}.json") as json_file:
        json_loaded = json.load(json_file)
    return json_loaded

def save_json(json_data, file_name: str,
                indent: int = 4, sort_keys: bool = False):
    cfg = json.dumps(json_data, indent=indent, sort_keys=sort_keys)
    with open(f"{here}/{file_name}.json","w") as json_file:
        json_file.writelines(cfg)
    return None