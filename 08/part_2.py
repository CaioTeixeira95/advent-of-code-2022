import re
from enum import Enum


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


def get_trees(line: str) -> list[int]:
    return list(map(int, re.findall(r"\d", line)))


def get_scenic_score_row(row: list[int], column: int, tree: int, direction: Direction):
    row_order_map = {
        Direction.LEFT: list(reversed(row[0:column])),
        Direction.RIGHT: row[column + 1 :],
    }

    score = 0
    for t in row_order_map[direction]:
        score += 1
        if tree <= t:
            break

    return score


def get_scenic_score_column(
    column: list[int], row: int, tree: int, direction: Direction
):
    column_order_map = {
        Direction.UP: list(reversed(column[0:row])),
        Direction.DOWN: column[row + 1 :],
    }

    score = 0
    for t in column_order_map[direction]:
        score += 1
        if tree <= t:
            break

    return score


def get_scenic_scores(trees: list[list[int]]) -> list[int]:
    scores: list[int] = []

    trees_columns: list[list[int]] = [[] for _ in range(len(trees))]
    for row in trees:
        for column, tree in enumerate(row):
            trees_columns[column].append(tree)

    for row, trees_row in enumerate(trees):
        for column, tree in enumerate(trees_row):
            score_left = get_scenic_score_row(trees_row, column, tree, Direction.LEFT)
            score_right = get_scenic_score_row(trees_row, column, tree, Direction.RIGHT)
            score_up = get_scenic_score_column(
                trees_columns[column], row, tree, Direction.UP
            )
            score_down = get_scenic_score_column(
                trees_columns[column], row, tree, Direction.DOWN
            )

            total_score = score_left * score_right * score_up * score_down

            scores.append(total_score)

    return scores


trees: list[list[int]] = []
while True:
    try:
        line = input()
        trees.append(get_trees(line))
    except EOFError:
        break

scores = get_scenic_scores(trees)
print(scores)
print(max(scores))
