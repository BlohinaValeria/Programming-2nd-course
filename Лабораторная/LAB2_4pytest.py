import pytest
from LAB1 import calculate
def test_add():
    assert calculate(2, 3, 'add') == 5
def test_sub():
    assert calculate(5, 2, 'sub') == 3
def test_mult():
    assert calculate(4, 2, 'mult') == 8
def test_div():
    assert calculate(10, 2, 'div') == 5
def test_div_by_zero():
    with pytest.raises(ValueError):
        calculate(10, 0, 'div')