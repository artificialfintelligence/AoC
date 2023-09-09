from aocd import data, submit

data = data.split("\n")


def get_start_end(assigned_sections_range: str) -> (int, int):
    section_range_start_end = assigned_sections_range.split("-")
    start = int(section_range_start_end[0])
    end = int(section_range_start_end[1])
    return start, end


n_fully_contain = 0
for line in data:
    elves = line.split(",")
    e1_start, e1_end = get_start_end(elves[0])
    e2_start, e2_end = get_start_end(elves[1])
    e1_contains_e2 = (e1_start <= e2_start) and (e1_end >= e2_end)
    e2_contains_e1 = (e1_start >= e2_start) and (e1_end <= e2_end)
    if e1_contains_e2 or e2_contains_e1:
        n_fully_contain += 1

# submit(n_fully_contain, part="a", day=4, year=2022)

n_overlap = 0
for line in data:
    elves = line.split(",")
    e1_start, e1_end = get_start_end(elves[0])
    e2_start, e2_end = get_start_end(elves[1])

    if not (e1_start > e2_end or e1_end < e2_start):
        n_overlap += 1
# submit(n_overlap, part="b", day=4, year=2022)
