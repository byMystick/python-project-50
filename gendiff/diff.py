import json


def load_data(file_path):
    with open(file_path) as f:
        return json.load(f)


def generate_diff(file_path1, file_path2):
    data1 = load_data(file_path1)
    data2 = load_data(file_path2)
    diff_lines = []

    for key, value1 in data1.items():
        if key in data2:
            value2 = data2[key]
            if value1 != value2:
                diff_lines.append(f"- {key}: {value1}")
                diff_lines.append(f"+ {key}: {value2}")
        else:
            diff_lines.append(f"- {key}: {value1}")

    for key, value2 in data2.items():
        if key not in data1:
            diff_lines.append(f"+ {key}: {value2}")

    return "\n".join(["{"] + sorted(diff_lines) + ["}"])
