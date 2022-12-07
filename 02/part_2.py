"""
A - Rock -> 1
B - Paper -> 2
C - Scissor -> 3

X - Lose
Y - Draw
Z - Win

Lose - 0
Draw - 3
Win - 6
"""


def handle_rock(me: str) -> int:
    match me:
        case "X":
            return 3
        case "Y":
            return 4
        case "Z":
            return 8


def handle_paper(me: str):
    match me:
        case "X":
            return 1
        case "Y":
            return 5
        case "Z":
            return 9


def handle_scissor(me: str):
    match me:
        case "X":
            return 2
        case "Y":
            return 6
        case "Z":
            return 7


handlers = {
    "A": handle_rock,
    "B": handle_paper,
    "C": handle_scissor,
}


def get_game_score(opponent: str, me: str) -> int:
    return handlers[opponent](me)


final_score = 0
while True:
    try:
        opponent, me = input().split()
        final_score += get_game_score(opponent, me)
    except EOFError:
        break

print(final_score)
