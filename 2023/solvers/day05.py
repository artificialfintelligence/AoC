# pylint: disable=missing-module-docstring, missing-docstring

import re


def process_data(
    data: list[str],
) -> tuple[list[int], dict[str : list[tuple[int, int, int]]]]:
    """Parses raw input data into more readily usable format as described below.

    Args:
        data:
            Raw data in the common "list of strings" format output by the
            `data_io` module.

    Returns:
        A tuple of two elements, the first being the list of initial seeds and
        the second being a dictionary of the required mappings, where the string
        keys name the mapping and the values are lists of tuples of integers,
        where each tuple corresponds to a (destination range start, source range
        start, range length) as per the puzzle description.
    """
    init_seeds = [int(n) for n in data[0].replace("seeds: ", "").split()]
    mappings = {}
    curr_key = ""
    for line in data[1:]:
        if line and line[0].isalpha():
            curr_key = line.replace(" map:", "")
            mappings[curr_key] = []
        elif line and line[0].isnumeric():
            mappings[curr_key].append(tuple(int(x) for x in line.split()))
    return (init_seeds, mappings)


def solve_part_1(
    init_seeds: list[int], mappings: dict[str : list[tuple[int, int, int]]]
) -> int:
    min_loc = 0

    return min_loc


def solve_part_2(
    init_seeds: list[int], mappings: dict[str : list[tuple[int, int, int]]]
) -> int:
    result = 0
    return result


def solve(data: list[str], part: int) -> int:
    init_seeds, mappings = process_data(data)
    if part == 1:
        solution = solve_part_1(init_seeds, mappings)
    else:  # part == 2
        solution = solve_part_2(init_seeds, mappings)
    return solution
