import unittest
from LAB3_1 import calculate, convert_precision


class TestCalculator(unittest.TestCase):
    def test_add_(self):
        self.assertAlmostEqual(calculate(5, 3, 'add', tolerance=1e-3), 8)

    def test_sub_(self):
        self.assertAlmostEqual(calculate(14, 10, 'sub', tolerance=1e-2), 4)

    def test_mult_(self):
        self.assertAlmostEqual(calculate(6, 2, 'mult', tolerance=1e-4), 12.0)

    def test_div_tolerance(self):
        self.assertAlmostEqual(calculate(45, 5, 'div', tolerance=1e-5), 9)

    def test_div_by_zero_tolerance(self):
        with self.assertRaises(ValueError):
            calculate(10, 0, 'div', tolerance=1e-6)

    def test_convert_precision(self):
        self.assertEqual(convert_precision(1e-6), 6)
        self.assertEqual(convert_precision(1e-3), 3)
        self.assertEqual(convert_precision(1e-1), 1)


if __name__ == '__main__':
    unittest.main()
