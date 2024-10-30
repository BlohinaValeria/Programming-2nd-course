import unittest
from LAB3_2 import calculate


class TestCalculate(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate('add', 1, 4, 3), 8)

    def test_sub(self):
        self.assertEqual(calculate('sub', 25, 5, 10), 10)

    def test_mult(self):
        self.assertEqual(calculate('mult', 2, 3, 4), 24)

    def test_div(self):
        self.assertEqual(calculate('div', 10, 2), 5)

    def test_medium(self):
        self.assertEqual(calculate('medium', 1, 2, 3, 4), 2.5)

    def test_variance(self):
        self.assertEqual(calculate('variance', 1, 2, 3, 4), 1.25)

    def test_std_deviation(self):
        self.assertAlmostEqual(calculate('std_deviation', 1, 2, 3, 4), 1.118033988749895)

    def test_median(self):
        self.assertEqual(calculate('median', 1, 2, 3, 4), 2.5)

    def test_q1(self):
        self.assertEqual(calculate('q1', 1, 2, 3, 4, 5, 6), 2)

    def test_q3(self):
        self.assertEqual(calculate('q3', 1, 2, 3, 4, 5, 6), 5)

    def test_interquartile_range(self):
        self.assertEqual(calculate('interquartile_range', 1, 2, 3, 4, 5, 6), 3)


if __name__ == '__main__':
    unittest.main()
