calories = []
try:
    partial_calories = 0
    while True:
        quantity = input()
        if not quantity:
            calories.append(partial_calories)
            partial_calories = 0
            continue
        partial_calories += int(quantity)
except EOFError:
    pass

print(sum(sorted(calories, reverse=True)[0:3]))
