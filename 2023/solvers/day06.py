# pylint: disable=missing-module-docstring, missing-docstring

import operator
from functools import reduce


def solve_part_1(data: list[str]) -> int:
    times = list(map(int, data[0].replace("Time:", "").strip().split()))
    dists = list(map(int, data[1].replace("Distance:", "").strip().split()))
    ways2win = [0] * len(times)
    for race_idx, time in enumerate(times):
        options = [i * (time - i) for i in range(time + 1)]
        ways2win[race_idx] = sum(1 for x in options if x > dists[race_idx])
    return reduce(operator.mul, ways2win, 1)


def solve_part_2(data) -> int:
    time = int(
        reduce(operator.concat, data[0].replace("Time:", "").strip().split())
    )
    dist = int(
        reduce(
            operator.concat,
            data[1].replace("Distance:", "").strip().split(),
        )
    )
    options = [i * (time - i) for i in range(time + 1)]
    ways2win = sum(1 for x in options if x > dist)
    return ways2win


def solve(data: list[str], part: int) -> int:
    if part == 1:
        solution = solve_part_1(data)
    else:  # part == 2
        solution = solve_part_2(data)
    return solution
