import unittest
from LAB1 import calculate


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate(2, 3, 'add'), 5)

    def test_sub(self):
        self.assertEqual(calculate(5, 2, 'sub'), 3)

    def test_mult(self):
        self.assertEqual(calculate(4, 2, 'mult'), 8)

    def test_div(self):
        self.assertEqual(calculate(10, 2, 'div'), 5)

    def test_div_by_zero(self):
        with self.assertRaises(ValueError):
            calculate(10, 0, 'div')


if __name__ == '__main__':
    unittest.main()
