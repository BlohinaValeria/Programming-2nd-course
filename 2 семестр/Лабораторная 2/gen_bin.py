def gen_bin_tree(root=3, height=0):
    """
    Генерирует бинарное дерево в виде словаря, где ключи - значения узлов,
    а значения - список из двух элементов: левого и правого потомков.

    Args:
        root: Значение корня дерева
        height: Высота дерева
    """

    tree = {}


    def tree_build(root2, height2):
        if height2 > 0:
            tree[root2] = []
            left_leaf = root2 + 2
            right_leaf = root2 * 3

            tree[root2].append(tree_build(left_leaf, height2 - 1))
            tree[root2].append(tree_build(right_leaf, height2 - 1))

        return root2
    if height == 0:
        return {root: []}
    tree_build(root, height)
    return tree

def main():
    root = 3
    height = 4
    print(gen_bin_tree(root, height))

if __name__ == "__main__":
    main()