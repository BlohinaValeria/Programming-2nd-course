from LAB2_2 import calculate


def test_add():
    assert calculate(1, 2, 'add') == 3
    return ('Test passed')


def test_sub():
    assert calculate(8, 6, 'sub') == 2
    return ('Test passed')


def test_div():
    assert calculate(64, 8, 'div') == 8
    return ('Test passed')


def test_mult():
    assert calculate(6, 9, 'mult') == 54
    return ('Test passed')


if __name__ == "__main__":
    print(test_add())
    print(test_sub())
    print(test_mult())
    print(test_div())