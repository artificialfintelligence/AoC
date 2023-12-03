#!/usr/bin/env python
# coding: utf-8

# pylint: disable=missing-module-docstring, missing-docstring

import argparse
import importlib
from datetime import datetime

from data_io import load_data


def main(params: list[str]) -> None:
    part_num = params.part
    is_testmode = params.testmode
    day = params.day
    year = 2023

    data = load_data(day, year, is_testmode)

    try:
        module = importlib.import_module(f"solvers.day{day:02}")
    except ModuleNotFoundError as e:
        raise NotImplementedError(
            f"Solver for day {day:02} not implemented yet."
        ) from e

    solution = module.solve(data, part_num)

    print(f"Part {part_num} Solution: {solution}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Advent of Code 2023 Puzzle Solver"
    )

    parser.add_argument(
        "--day",
        "-d",
        help="Day to solve",
        type=int,
        choices=range(1, 26),
        default=datetime.today().day,
        required=False,
    )
    parser.add_argument(
        "--part",
        "-p",
        help="Part to solve",
        type=int,
        choices=[1, 2],
        required=True,
    )
    parser.add_argument(
        "--testmode",
        "-t",
        help="Whether to use sample data ('test_day##.txt')",
        type=bool,
        default=False,
        choices=[True, False],
        required=False,
    )

    args = parser.parse_args()
    main(args)
