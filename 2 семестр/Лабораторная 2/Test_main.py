"""
def test_tree_height_0(self):
Тестирует функцию gen_bin_tree_rec при высоте дерева, равной 0.
Проверяет, что функция возвращает словарь с ключом root и пустым списком в качестве значения.

def test_tree_height_1(self):
Тестирует функцию gen_bin_tree_rec при высоте дерева, равной 1.
Проверяет, что функция возвращает словарь (т.е. дерево было создано).

def test_tree_height_greater_than_1(self):
Тестирует функцию gen_bin_tree_rec при высоте дерева больше 1.
Проверяет, что функция возвращает словарь (т.е. дерево было создано).

def test_setup_data_length(self):
Тестирует функцию setup_data на правильность возвращаемой длины списка.
Проверяет, что функция возвращает список с количеством элементов, равным заданному параметру n.

def test_setup_data_elements(self):
Тестирует функцию setup_data на правильность типа элементов списка.
Проверяет, что каждый элемент списка является кортежем.

def test_setup_data_values(self):
Тестирует функцию setup_data на правильность значений в кортежах.
Проверяет, что значения root находятся в диапазоне от 0 до 3, а значения height - в диапазоне от 0 до 10."""

import unittest
from unittest.mock import patch
import sys
import os

from main import gen_bin_tree_rec, gen_bin_tree_iter, setup_data


class TestBinaryTree(unittest.TestCase):

    def test_tree_height_0(self):
        result = gen_bin_tree_rec(5, 0)
        self.assertEqual(result, {5: []})

    def test_tree_height_1(self):
        result = gen_bin_tree_rec(1, 1)
        self.assertTrue(isinstance(result, dict))

    def test_tree_height_greater_than_1(self):
        result = gen_bin_tree_rec(2, 3)
        self.assertTrue(isinstance(result, dict))

    def test_setup_data_length(self):
        n = 10
        data = setup_data(n)
        self.assertEqual(len(data), n)

    def test_setup_data_elements(self):
        data = setup_data(5)
        for element in data:
            self.assertTrue(isinstance(element, tuple))

    def test_setup_data_values(self):
        data = setup_data(10)
        for root, height in data:
            self.assertTrue(0 <= root <= 3)
            self.assertTrue(0 <= height <= 10)


if __name__ == "__main__":
    unittest.main()