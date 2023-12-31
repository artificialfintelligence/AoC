# pylint: disable=missing-module-docstring, missing-docstring

import operator
import re
from functools import reduce


def process_data(data: list[str]) -> dict[int : list[dict[str:int]]]:
    """Parses raw input data into more readily usable format as described below.

    Args:
        data:
            Raw data in the common "list of strings" format output by the
            `data_io` module.
            example:

            ["Game 1: 3 blue, 4 red; 1 red, 2 green; 2 green",
             "Game 2: 1 blue, 2 green, 1 red; 4 blue, 1 red"]

    Returns:
        A dict with keys corresponding to game (row) IDs and values being
        a list of dictionaries, where each contained dictionary is one set of
        revelations showing the number of cubes drawn of each colour.
        example:

        {1: [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2}, {'green': 2}],
         2: [{'blue': 1, 'green': 2, 'red': 1}, {'blue': 4, 'red': 1}]}
    """
    output = {}
    for row in [r for r in data if r != ""]:
        parsed_row = re.match(r"^Game (\d+): (.*)", row)
        row_id, row_data = int(parsed_row.group(1)), parsed_row.group(2)
        row_data_list_of_lists = [r.split(",") for r in row_data.split(";")]
        output[row_id] = [
            {k.strip(): int(v) for v, k in (item.split() for item in sublist)}
            for sublist in row_data_list_of_lists
        ]
    return output


def solve_part_1(data: dict[int : list[dict[str:int]]]) -> int:
    sum_of_valid_ids = 0
    cube_counts_total = {"red": 12, "green": 13, "blue": 14}
    for row_id, record in data.items():
        is_valid = True
        for draw in record:
            if not is_valid:
                break
            for colour, count in draw.items():
                if count > cube_counts_total[colour]:
                    is_valid = False
                    break
        if is_valid:
            sum_of_valid_ids += row_id
    return sum_of_valid_ids


def solve_part_2(data: dict[int : list[dict[str, int]]]) -> int:
    total_power = 0
    for _, record in data.items():
        min_counts = {"red": 0, "green": 0, "blue": 0}
        for draw in record:
            for colour, count in draw.items():
                min_counts[colour] = max(min_counts[colour], count)
        power = reduce(operator.mul, min_counts.values(), 1)
        total_power += power
    return total_power


def solve(data: list[str], part: int) -> int:
    data_processed = process_data(data)
    if part == 1:
        solution = solve_part_1(data_processed)
    else:  # part == 2
        solution = solve_part_2(data_processed)
    return solution
