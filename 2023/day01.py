#!/usr/bin/env python
# coding: utf-8

# pylint: disable=missing-module-docstring, missing-docstring

import argparse
import re

# To just automatically get **today's** data: `from aocd import data`
from aocd import get_data


def main(params: list[str]) -> None:
    part_num = params.part

    data = get_data(day=1, year=2023)

    # with open("data/day01_test.txt", "r", encoding="utf-8") as f:
    #     data = f.read()

    data = data.split("\n")

    str2int = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    if part_num == 1:
        search_pattern = r"\d"
    else:  # part_num == 2
        search_pattern = rf"(?=(\d|{'|'.join(str2int.keys())}))"

    calibration_total = 0

    matches = [re.findall(search_pattern, line, re.IGNORECASE) for line in data]
    digits_str = [
        [str2int[i] if i in str2int else i for i in line] for line in matches
    ]
    calibration_values = [int(l[0] + l[-1]) for l in digits_str]
    calibration_total = sum(calibration_values)

    print(f"Part {part_num} Solution: {calibration_total}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AoC 2023 Day 1 Puzzle Solver")
    parser.add_argument(
        "--part", help="Part 1 or 2", type=int, choices=[1, 2], required=True
    )

    args = parser.parse_args()
    main(args)
