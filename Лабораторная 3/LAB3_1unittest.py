import unittest
from LAB3_1 import calculate

class TestCalculator(unittest.TestCase):
    def test_add_tolerance(self):
        self.assertAlmostEqual(calculate(2.123456789, 3.987654321, 'add', tolerance=1e-3), 6.111, places=3)

    def test_sub_tolerance(self):
        self.assertAlmostEqual(calculate(5.123456789, 2.987654321, 'sub', tolerance=1e-2), 2.13, places=2)

    def test_mult_tolerance(self):
        self.assertAlmostEqual(calculate(4.123456789, 2.987654321, 'mult', tolerance=1e-4), 12.3333, places=4)

    def test_div_tolerance(self):
        self.assertAlmostEqual(calculate(10.123456789, 2.987654321, 'div', tolerance=1e-5), 3.38889, places=5)

    def test_div_by_zero_tolerance(self):
        with self.assertRaises(ValueError):
            calculate(10, 0, 'div', tolerance=1e-6)

    def test_convert_precision(self):
        self.assertEqual(convert_precision(1e-6), 6)
        self.assertEqual(convert_precision(1e-3), 3)
        self.assertEqual(convert_precision(1e-1), 1)

if __name__ == '__main__':
    unittest.main()