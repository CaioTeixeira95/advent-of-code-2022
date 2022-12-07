import string

lower_case_priority = {
    letter: priority + 1 for priority, letter in enumerate(string.ascii_lowercase)
}

upper_case_priority = {
    letter: priority + 27 for priority, letter in enumerate(string.ascii_uppercase)
}


def get_priority_from_common_element(group: list[set[str]]) -> int:
    a, b, c = group
    common_element = a.intersection(b).intersection(c).pop()
    try:
        return lower_case_priority[common_element]
    except KeyError:
        return upper_case_priority[common_element]


total_priorities = 0
group = []
while True:
    try:
        content = input()
        group.append(set(content[:]))
        if len(group) == 3:
            total_priorities += get_priority_from_common_element(group)
            group = []
    except EOFError:
        break

print(total_priorities)
