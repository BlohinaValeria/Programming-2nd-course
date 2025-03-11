import time
from random import randint
import matplotlib.pyplot as plt

def gen_bin_tree_rec(root, height):
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


def gen_bin_tree_iter(root, height):
    tree = {}
    if height == 0:
        return {root: []}
    stack = [(root, height)]

    while stack:
        current, current_height = stack.pop()
        tree[current] = []

        if current_height > 0:
            left_leaf = current + 2
            right_leaf = current * 3

            tree[current].append(left_leaf)
            tree[current].append(right_leaf)

            stack.append((right_leaf, current_height - 1))
            stack.append((left_leaf, current_height - 1))
    return tree


def setup_data(n: int) -> list:
    data = []
    for _ in range(n):
        root = randint(0, 3)
        height = randint(0, 10)
        data.append((root, height))
    return data


def calculate_time(data, func) -> float:
    start_time = time.time()
    for root, height in data:
        func(root, height)
    end_time = time.time()
    return (end_time - start_time) / len(data)


def main():
    num_runs = 1
    max_list_length = 50
    step = 1
    list_lengths = range(step, max_list_length + 1, step)

    results_rec = []
    results_iter = []

    for n in list_lengths:
        total_time_rec = 0
        total_time_iter = 0
        for _ in range(num_runs):
            data = setup_data(n)
            total_time_rec += calculate_time(data, gen_bin_tree_rec)
            total_time_iter += calculate_time(data, gen_bin_tree_iter)

        average_time_rec = total_time_rec / num_runs
        average_time_iter = total_time_iter / num_runs
        results_rec.append(average_time_rec)
        results_iter.append(average_time_iter)
        print(
            f"List length {n}: Recursive - {average_time_rec:.6f} seconds, Iterative - {average_time_iter:.6f} seconds"
        )


    plt.plot(list_lengths, results_rec, label="Recursive")
    plt.plot(list_lengths, results_iter, label="Iterative")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()