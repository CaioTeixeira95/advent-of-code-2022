import re
from itertools import chain


def get_trees(line: str) -> list[int]:
    return list(map(int, re.findall(r"\d", line)))


def calculate_visible_trees(trees: list[list[int]]) -> int:
    visible_trees = len(trees) * 2
    visible_trees += (len(trees[0]) - 2) * 2

    trees_columns: list[list[int]] = [[] for _ in range(len(trees))]
    for row in trees:
        for column, tree in enumerate(row):
            trees_columns[column].append(tree)

    for row, trees_row in enumerate(trees[1 : len(trees) - 1]):
        row += 1  # Fix the index value
        for column, tree in enumerate(trees_row[1 : len(trees_row) - 1]):
            column += 1

            trees_same_column = trees_columns[column]

            is_visible_left = all(tree > t for t in trees_row[0:column])
            is_visible_right = all(tree > t for t in trees_row[column + 1 :])
            is_visible_up = all(tree > t for t in trees_same_column[0:row])
            is_visible_down = all(tree > t for t in trees_same_column[row + 1 :])

            if any([is_visible_left, is_visible_right, is_visible_up, is_visible_down]):
                visible_trees += 1

    return visible_trees


trees: list[list[int]] = []
while True:
    try:
        line = input()
        trees.append(get_trees(line))
    except EOFError:
        break

print(calculate_visible_trees(trees))
