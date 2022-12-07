import string

lower_case_priority = {
    letter: priority + 1 for priority, letter in enumerate(string.ascii_lowercase)
}

upper_case_priority = {
    letter: priority + 27 for priority, letter in enumerate(string.ascii_uppercase)
}


def get_priority_from_common_element_of_compartments(content: str):
    middle = len(content) // 2

    first_compartment = set(content[0:middle])
    second_compartment = set(content[middle:])

    common_element = first_compartment.intersection(second_compartment).pop()

    try:
        return lower_case_priority[common_element]
    except KeyError:
        return upper_case_priority[common_element]


total_priorities = 0
while True:
    try:
        content = input()
        total_priorities += get_priority_from_common_element_of_compartments(content)
    except EOFError:
        break

print(total_priorities)
