import json


def to_dict(json_file_name):
    with open(json_file_name, 'r') as config_file:
        config = json.load(config_file)
    return config
