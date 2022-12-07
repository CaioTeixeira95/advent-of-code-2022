def generate_range(start: int, end: int) -> set[int]:
    return set(range(start, end + 1, 1))


pairs = 0
while True:
    try:
        elv_1, elv_2 = input().split(",")

        elv_1_assignments = generate_range(*list(map(int, elv_1.split("-"))))
        elv_2_assignments = generate_range(*list(map(int, elv_2.split("-"))))

        if elv_1_assignments.intersection(elv_2_assignments):
            pairs += 1
    except EOFError:
        break

print(pairs)
