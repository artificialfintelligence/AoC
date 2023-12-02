#!/usr/bin/env python
# coding: utf-8

# pylint: disable=missing-module-docstring, missing-docstring

import argparse
import re

from data_io import load_data


def main(params: list[str]) -> None:
    part_num = params.part
    is_testmode = params.testmode

    data = load_data(1, 2023, is_testmode)
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
    calibration_values = [int(l[0] + l[-1]) for l in digits_str if l != []]
    calibration_total = sum(calibration_values)

    print(f"Part {part_num} Solution: {calibration_total}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AoC 2023 Day 1 Puzzle Solver")
    parser.add_argument(
        "--part",
        "-p",
        help="Part 1 or 2",
        type=int,
        choices=[1, 2],
        required=True,
    )
    parser.add_argument(
        "--testmode",
        "-t",
        help="Whether to use sample ('_test') data",
        type=bool,
        default=False,
        choices=[True, False],
        required=False,
    )

    args = parser.parse_args()
    main(args)
