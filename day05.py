from aocd import data, submit
import re

data = data.split("\n")


def read_initial_stacks_config(n_lines: int, n_stacks: int) -> dict(list()):
    stacks = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    for line in data[:n_lines]:
        for stack_idx in range(n_stacks):
            stack_pos = stack_idx * 4 + 1
            if line[stack_pos].isalpha():
                stacks[stack_idx + 1].insert(0, line[stack_pos])
    return stacks


stacks = read_initial_stacks_config(8, 9)
for line in data[10:]:
    # "Move n from a to b"
    n, a, b = re.match(r"move (\d+) from (\d+) to (\d+)", line).groups()
    n_crates = int(n)
    a_stack_idx = int(a)
    b_stack_idx = int(b)
    for i in range(n_crates):
        crate = stacks[a_stack_idx].pop()
        stacks[b_stack_idx].append(crate)

top_crates_a = "".join(list(stacks[k][-1] for k in stacks.keys()))
# submit(top_crates_a, part="a", day=5, year=2022)

stacks = read_initial_stacks_config(8, 9)
for line in data[10:]:
    # "Move n from a to b"
    n, a, b = re.match(r"move (\d+) from (\d+) to (\d+)", line).groups()
    n_crates = int(n)
    a_stack_idx = int(a)
    b_stack_idx = int(b)
    crates = stacks[a_stack_idx][-n_crates:]
    stacks[b_stack_idx].extend(crates)
    del stacks[a_stack_idx][-n_crates:]

top_crates_b = "".join(list(stacks[k][-1] for k in stacks.keys()))
# submit(top_crates_b, part="b", day=4, year=2022)
