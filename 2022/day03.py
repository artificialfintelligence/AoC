from aocd import get_data

data = get_data(day=3, year=2022).split("\n")


def get_priority(item_str: str) -> int:
    if item_str.isupper():
        return ord(item_str) - 38
    else:
        return ord(item_str) - 96


sum_of_priorities_a = 0
for line in data:
    first_half = line[: len(line) // 2]
    second_half = line[len(line) // 2 :]
    for item in line:
        if item in second_half:
            sum_of_priorities_a += get_priority(item)
            break

# submit(sum_of_priorities_a, part="a", day=3, year=2022)

sum_of_priorities_b = 0
n_groups = len(data) // 3
for group_number in range(n_groups):
    elf_1_items = data[group_number * 3]
    elf_2_items = data[group_number * 3 + 1]
    elf_3_items = data[group_number * 3 + 2]
    for item in elf_1_items:
        if item in elf_2_items and item in elf_3_items:
            sum_of_priorities_b += get_priority(item)
            break

# submit(sum_of_priorities_b, part="b", day=3, year=2022)
