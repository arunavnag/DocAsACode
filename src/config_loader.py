import json


def load_config(file_path):
    """Load configuration settings from a JSON file."""
    with open(file_path, 'r') as config_file:
        return json.load(config_file)
