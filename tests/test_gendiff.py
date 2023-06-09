from gendiff.diff import generate_diff


def test_generate_diff_json():
    f1 = 'tests/fixtures/file1.json'
    f2 = 'tests/fixtures/file2.json'
    with open('tests/fixtures/correct_diff', mode='r') as f:
        assert generate_diff(f1, f2) == f.read()


def test_generate_diff_yaml():
    f1 = 'tests/fixtures/file1.yaml'
    f2 = 'tests/fixtures/file2.yml'
    with open('tests/fixtures/correct_diff', mode='r') as f:
        assert generate_diff(f1, f2) == f.read()
