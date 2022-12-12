import math
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Knot:
    head: Point
    tail: Point


# This distance means that the tail won't need to be updated
MAX_DISTANCE_BETWEEN_HEAD_AND_TAIL = 1


def calculate_distance(head: Point, tail: Point) -> int:
    """Euclidean distance"""
    distance = math.pow(tail.x - head.x, 2) + math.pow(tail.y - head.y, 2)
    return int(math.sqrt(distance))


def update_tail_position(head: Point, tail: Point) -> Point:
    if head.x == tail.x:
        if head.y > tail.y:
            tail.y += 1
        else:
            tail.y -= 1
    elif head.y == tail.y:
        if head.x > tail.x:
            tail.x += 1
        else:
            tail.x -= 1
    else:
        if head.x > tail.x:
            tail.x += 1
        else:
            tail.x -= 1

        if head.y > tail.y:
            tail.y += 1
        else:
            tail.y -= 1

    return tail


def update_position(
    head: Point, tail: Point, direction: str, distance: int
) -> tuple[Point, Point]:
    for _ in range(distance):
        match direction:
            case "R":
                head.x += 1
            case "L":
                head.x -= 1
            case "U":
                head.y += 1
            case "D":
                head.y -= 1

        distance_between_tail_and_head = calculate_distance(head, tail)
        if distance_between_tail_and_head > MAX_DISTANCE_BETWEEN_HEAD_AND_TAIL:
            tail = update_tail_position(head, tail)
            tail_visited_locations[(tail.x, tail.y)] = None

    return head, tail


tail_visited_locations: dict[tuple[int, int], None] = {}

head = Point(0, 0)
tail = Point(0, 0)

tail_visited_locations[(0, 0)] = None
while True:
    try:
        direction, distance = input().split()
        head, tail = update_position(head, tail, direction, int(distance))
    except EOFError:
        break

print(len(tail_visited_locations.keys()))
