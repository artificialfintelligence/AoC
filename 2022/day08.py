from aocd import data

# with open("test.txt", "r") as f:
#     data = f.read()

data = data.strip().split("\n")

data = [[int(d) for d in row] for row in data]


def is_visible(i: int, j: int, grid: list[list[int]]) -> bool:
    tree = grid[i][j]
    row = grid[i]
    col = [row[j] for row in grid]
    visible_left = sum(list(map(lambda x: x >= tree, row[:j]))) == 0
    visible_right = sum(list(map(lambda x: x >= tree, row[j + 1 :]))) == 0
    visible_top = sum(list(map(lambda x: x >= tree, col[:i]))) == 0
    visible_bottom = sum(list(map(lambda x: x >= tree, col[i + 1 :]))) == 0
    return visible_left or visible_right or visible_top or visible_bottom


# All trees on the edges are visible
n_visible = 2 * (len(data) + len(data[0])) - 4

for i, row in enumerate(data[1:-1]):
    for j, tree in enumerate(row[1:-1]):
        if is_visible(i + 1, j + 1, data):
            n_visible += 1

solution_a = n_visible
print(f"{solution_a = }")


def calc_score_uni_dir(trees: list[int], tree_at_end: bool) -> int:
    if tree_at_end:
        lst = trees[-1::-1]
    else:
        lst = trees

    this_tree = lst[0]

    score = 0
    for tree in lst[1:]:
        score += 1
        if tree >= this_tree:
            break

    return score


def calc_scenic_score(i: int, j: int, grid: list[list[int]]) -> int:
    tree = grid[i][j]
    row = grid[i]
    col = [row[j] for row in grid]
    score_left = calc_score_uni_dir(row[: j + 1], True)
    score_right = calc_score_uni_dir(row[j:], False)
    score_top = calc_score_uni_dir(col[: i + 1], True)
    score_bottom = calc_score_uni_dir(col[i:], False)
    return score_left * score_right * score_top * score_bottom


scenic_score_grid = []

for i, row in enumerate(data):
    scenic_score_grid.append([])
    for j, tree in enumerate(row):
        scenic_score_grid[i].append(calc_scenic_score(i, j, data))

row_max_scores = [max(row) for row in scenic_score_grid]
overall_max_score = max(row_max_scores)

solution_b = overall_max_score
print(f"{solution_b = }")
