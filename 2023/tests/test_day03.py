# pylint: disable=missing-module-docstring, missing-docstring

import os
from pathlib import Path

from data_io import load_data
from solvers import day03

test_data_file_path = os.path.join("data", f"{Path(__file__).stem}.txt")

TEST_DATA = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
with open(test_data_file_path, "w", encoding="utf-8") as f:
    f.write(TEST_DATA)

EXPECTED_SOLUTION_PART_1_WITH_TEST_DATA = 4361
EXPECTED_SOLUTION_PART_1_WITH_REAL_DATA = 546312

EXPECTED_SOLUTION_PART_2_WITH_TEST_DATA = 467835
EXPECTED_SOLUTION_PART_2_WITH_REAL_DATA = 87449461


def test_part_1_with_test_data():
    data = load_data(day=3, year=2023, is_testmode=True)
    solution = day03.solve(data, part=1)
    assert solution == EXPECTED_SOLUTION_PART_1_WITH_TEST_DATA


def test_part_1_with_real_data():
    data = load_data(day=3, year=2023, is_testmode=False)
    solution = day03.solve(data, part=1)
    assert solution == EXPECTED_SOLUTION_PART_1_WITH_REAL_DATA


def test_part_2_with_test_data():
    data = load_data(day=3, year=2023, is_testmode=True)
    solution = day03.solve(data, part=2)
    assert solution == EXPECTED_SOLUTION_PART_2_WITH_TEST_DATA


def test_part_2_with_real_data():
    data = load_data(day=3, year=2023, is_testmode=False)
    solution = day03.solve(data, part=2)
    assert solution == EXPECTED_SOLUTION_PART_2_WITH_REAL_DATA
