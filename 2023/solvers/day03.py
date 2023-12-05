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
    n_lines = len(data)
    line_len = len(data[0])
    sum_gear_ratios = 0
    for line_num, line in enumerate(data):
        for match in re.finditer(r"\*", line):
            adjacent_numbers = []
            idx = match.start()
            search_start_idx = max(0, idx - 1)
            search_end_idx = min(line_len, idx + 2)
            # print(f"Found {match.group()} on line {line_num} at index {idx}.")
            for line_idx in range(
                max(line_num - 1, 0), 1 + min(line_num + 1, n_lines)
            ):
                search_str = data[line_idx][search_start_idx:search_end_idx]

                for m in re.finditer(r"\d+", search_str):
                    seq = m.group()
                    i = search_start_idx + m.start() - 1
                    while i >= 0:
                        prev_char = data[line_idx][i]
                        if prev_char.isnumeric():
                            seq = prev_char + seq
                        else:
                            break
                        i -= 1

                    i = search_start_idx + m.end()
                    while i < line_len:
                        next_char = data[line_idx][i]
                        if next_char.isnumeric():
                            seq = seq + next_char
                        else:
                            break
                        i += 1
                    adjacent_numbers.append(int(seq))

            if len(adjacent_numbers) == 2:
                sum_gear_ratios += adjacent_numbers[0] * adjacent_numbers[1]

    return sum_gear_ratios


def solve(data: list[str], part: int) -> int:
    if part == 1:
        solution = solve_part_1(data)
    else:  # part == 2
        solution = solve_part_2(data)
    return solution
