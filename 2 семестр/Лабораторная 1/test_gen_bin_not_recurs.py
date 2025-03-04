import unittest
from gen_bin_not_recurs import gen_bin_tree


class TestGenBinTree(unittest.TestCase):

    def test_height_zero(self):
        self.assertEqual(gen_bin_tree(1, 0), {1: []})

    def test_height_one(self):
        self.assertEqual(gen_bin_tree(3, 1), {3: [5, 9]})

    def test_height_two(self):
        expected_output = {3: [5, 9], 5: [7, 15], 9: [11, 27]}
        self.assertEqual(gen_bin_tree(3, 2), expected_output)

    def test_height_four(self):
        expected_output = {3: [5, 9], 5: [7, 15], 7: [9, 21], 9: [11, 27], 11: [13, 33], 13: [15, 39], 15: [17, 45], 17: [19, 51], 21: [23, 63], 27: [29, 81], 29: [31, 87], 33: [35, 99], 45: [47, 135], 81: [83, 243]}
        self.assertEqual(gen_bin_tree(3, 4), expected_output)

if __name__ == "__main__":
    unittest.main()