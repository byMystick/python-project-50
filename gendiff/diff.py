import json


def generate_diff(file_path1, file_path2):
    with open(file_path1) as file1, open(file_path2) as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

    diff = {}
    keys = set(data1.keys()) | set(data2.keys())
    for key in sorted(keys):
        if key not in data1:
            diff[f'+ {key}'] = data2[key]
        elif key not in data2:
            diff[f'- {key}'] = data1[key]
        elif data1[key] != data2[key]:
            diff[f'- {key}'] = data1[key]
            diff[f'+ {key}'] = data2[key]
        else:
            diff[f'  {key}'] = data1[key]

    result = ['{\n']
    for key, value in diff.items():
        value = str(value)
        result.append(f'  {key}: {value}\n')
    result.append('}\n')

    return ''.join(result).lower()
