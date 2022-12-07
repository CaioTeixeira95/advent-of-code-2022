"""
A & X - Rock -> 1
B & Y - Paper -> 2
C & Z - Scissor -> 3

Lose - 0
Draw - 3
Win - 6
"""


scores = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def is_equal(opponent: str, me: str) -> bool:
    return (
        (opponent == "A" and me == "X")
        or (opponent == "B" and me == "Y")
        or (opponent == "C" and me == "Z")
    )


def get_game_score(opponent: str, me: str) -> int:
    score = scores[me]
    if is_equal(opponent, me):
        return score + 3

    result = 0
    match opponent:
        case "A":
            if me == "Y":
                result = 6
        case "B":
            if me == "Z":
                result = 6
        case "C":
            if me == "X":
                result = 6

    return score + result


final_score = 0
while True:
    try:
        opponent, me = input().split()
        final_score += get_game_score(opponent, me)
    except EOFError:
        break

print(final_score)
