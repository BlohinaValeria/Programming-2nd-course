import unittest
from gen_bin import gen_bin_tree

class TestGenBinTree(unittest.TestCase):

    def test_height_0(self):
        tree = gen_bin_tree(root=3, height=0)
        self.assertEqual(tree, {3: []})

    def test_height_1(self):
        tree = gen_bin_tree(root=3, height=1)
        self.assertEqual(tree, {3: [5, 9]})

    def test_height_2(self):
        tree = gen_bin_tree(root=3, height=2)
        expected_tree = {3: [5, 9], 5: [7, 15], 9: [11, 27]}
        self.assertEqual(tree, expected_tree)


if __name__ == '__main__':
    unittest.main()