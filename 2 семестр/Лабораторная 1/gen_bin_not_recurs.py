"""
Лабораторная работа 2.

Реализовать нерекурсивный вариант функции для построения бинарного дерева.

Можно разбить данную задачу на 2 этапа:
1) построение корней дерева полностью (список списков, в котором, каждый "уровень" дерева - это список) (roots)

2) итерация по этому списку списков (roots) с выборкой элементов оттуда и помещением их в "правильное" место нашего дерева

"""
def gen_bin_tree(root, height):
    tree = {}

    if height == 0:
        return {root: []}
    stack = [(root, height)]

    while stack:
        current, current_height = stack.pop()

        if current_height > 0:
            tree[current] = []
            left_leaf = current + 2
            right_leaf = current * 3

            stack.append((left_leaf, current_height - 1))
            stack.append((right_leaf, current_height - 1))
            tree[current].append(left_leaf)
            tree[current].append(right_leaf)

    return tree

def main():
    root = 3
    height = 4
    print(gen_bin_tree(root, height))

if __name__ == "__main__":
    main()
