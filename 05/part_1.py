from collections import defaultdict
import re


def parse_crane(line: str) -> list[str]:
    empty_spaces = 0
    cranes = []
    for elem in line.split(" "):
        if elem or empty_spaces == 3:
            cranes.append(elem)
            empty_spaces = 0
        elif not elem and empty_spaces < 3:
            empty_spaces += 1

    return cranes


def parse_instruction(instruction: str) -> list[int]:
    return list(map(int, re.findall(r"\d+", instruction)))


cranes: list[str] = []
crane_indexes: list[int] = []
instructions: list[str] = []
while True:
    try:
        line = input()
        if re.findall(r"\[", line):
            cranes.append(parse_crane(line))
        elif "move" in line:
            instructions.append(line)
        elif line != "":
            crane_indexes = list(map(int, line.split()))
    except EOFError:
        break


cargo: dict[int, list[str]] = defaultdict(list)
for idx in crane_indexes:
    for crane in cranes:
        elem = crane[idx - 1]
        if elem:
            cargo[idx].insert(0, elem)


for instruction in instructions:
    quantity_to_move, from_crane, to_crane = parse_instruction(instruction)
    for _ in range(quantity_to_move):
        cargo[to_crane].append(cargo[from_crane].pop())


stack = ""
for idx, crane in cargo.items():
    stack += crane[-1][1]

print(stack)
