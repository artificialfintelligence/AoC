from aocd import data

# with open("test.txt", "r") as f:
#     data = f.read()

data = data.strip().split("\n")

head = (0, 0)
tail = (0, 0)
tail_hist = {tail}

dir_to_step = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}


def take_one_step(direction: str, current_pos: (int, int)) -> (int, int):
    step = dir_to_step[direction]
    return tuple(map(lambda x, y: x + y, current_pos, step))


for row in data:
    move = row.split(" ")
    direction = move[0]
    n_steps = int(move[1])
    for _ in range(n_steps):
        head = take_one_step(direction, head)
        diff = tuple(map(lambda x, y: x - y, head, tail))
        if abs(diff[0]) == 2 or abs(diff[1]) == 2:
            step = tuple(map(lambda x: int(x / abs(x)) if x != 0 else 0, diff))
            tail = tuple(map(lambda x, y: x + y, tail, step))
            tail_hist.add(tail)

solution_a = len(tail_hist)
print(f"{solution_a = }")


head = (0, 0)
tails = [
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
]
last_tail_hist = {tails[-1]}

for row in data:
    move = row.split(" ")
    direction = move[0]
    n_steps = int(move[1])
    for _ in range(n_steps):
        head = take_one_step(direction, head)
        for i, tail in enumerate(tails):
            if i == 0:
                diff = tuple(map(lambda x, y: x - y, head, tail))
            else:
                diff = tuple(map(lambda x, y: x - y, tails[i - 1], tail))
            if abs(diff[0]) == 2 or abs(diff[1]) == 2:
                step = tuple(
                    map(lambda x: int(x / abs(x)) if x != 0 else 0, diff)
                )
                tails[i] = tuple(map(lambda x, y: x + y, tail, step))
        last_tail_hist.add(tails[-1])

solution_b = len(last_tail_hist)
print(f"{solution_b = }")
