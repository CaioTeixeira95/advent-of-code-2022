calories = 0
try:
    partial_calories = 0
    while True:
        quantity = input()
        if not quantity:
            if partial_calories > calories:
                calories = partial_calories
            partial_calories = 0
            continue
        partial_calories += int(quantity)
except EOFError:
    pass

print(calories)
