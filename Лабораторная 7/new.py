
#задание 3
import pytest
import os


@pytest.fixture
def params_ini(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    params_file = d / "params.ini"
    with open(params_file, 'w') as f:
        f.write("precision=0.00001\n")
        f.write("dest=output.txt\n")

    return str(params_file)


def test_load_params(params_ini):
    global PARAMS


PARAMS = {'precision': 0.00001, 'dest': 'output.txt'}

loaded_params = load_params(file=params_ini)

assert loaded_params['precision'] == 0.00001
assert loaded_params['dest'] == 'output.txt'