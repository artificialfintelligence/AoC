# pylint: disable=missing-module-docstring, missing-docstring

import re


def solve_part_1(data: list[str]) -> int:
    n_lines = len(data)
    line_len = len(data[0])
    sum_part_nums = 0

    for line_num, line in enumerate(data):
        for match in re.finditer(r"\d+", line):
            span = match.span()
            search_start_idx = max(0, span[0] - 1)
            search_end_idx = min(line_len, span[1] + 1)
            # print(f"Found {match.group()} on line {line_num} at {span}.")
            if line_num > 0:
                search_str = data[line_num - 1][search_start_idx:search_end_idx]
                if not all(char == "." for char in search_str):
                    sum_part_nums += int(match.group())
                    continue
            if line_num < n_lines - 1:
                search_str = data[line_num + 1][search_start_idx:search_end_idx]
                if not all(char == "." for char in search_str):
                    sum_part_nums += int(match.group())
                    continue
            if span[0] > 0:
                if line[span[0] - 1] != ".":
                    sum_part_nums += int(match.group())
                    continue
            if span[1] < line_len - 1:
                if line[span[1]] != ".":
                    sum_part_nums += int(match.group())
                    continue
    return sum_part_nums


def solve_part_2(data: list[str]) -> int:
    return 0


def solve(data: list[str], part: int) -> int:
    if part == 1:
        solution = solve_part_1(data)
    else:  # part == 2
        solution = solve_part_2(data)
    return solution
