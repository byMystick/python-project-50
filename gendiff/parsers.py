import yaml
import json



def parse_json(data):
    return json.loads(data)


def parse_file(file_path):
    with open(file_path) as file:
        extension = file_path.rsplit('.', 1)[-1]
        if extension in ['yml', 'yaml']:
            return yaml.safe_load(file)
        elif extension == 'json':
            return parse_json(file.read())
        else:
            raise ValueError(f"Unsupported file format: {extension}")
