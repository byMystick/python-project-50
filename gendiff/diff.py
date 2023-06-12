import json


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))
    diff = {}
    for key in sorted(set(data1.keys()) | set(data2.keys())):
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
        if isinstance(value, str):
            value = f"{value}"
        else:
            value = str(value).lower()
        result.append(f'  {key}: {value}\n')
    result.append('}\n')
    return ''.join(result)
