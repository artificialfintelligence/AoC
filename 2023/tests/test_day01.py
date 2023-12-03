# pylint: disable=missing-module-docstring, missing-docstring

import os
from pathlib import Path

from data_io import load_data
from solvers import day01

test_data_file_path = os.path.join("data", f"{Path(__file__).stem}.txt")

EXPECTED_SOLUTION_PART_1_WITH_TEST_DATA = 142
EXPECTED_SOLUTION_PART_2_WITH_TEST_DATA = 281

EXPECTED_SOLUTION_PART_1_WITH_REAL_DATA = 54239
EXPECTED_SOLUTION_PART_2_WITH_REAL_DATA = 55343


def test_part_1_with_test_data():
    test_data_part_1 = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
    with open(test_data_file_path, "w", encoding="utf-8") as f:
        f.write(test_data_part_1)
    data = load_data(day=1, year=2023, is_testmode=True)
    solution = day01.solve(data, part=1)
    assert solution == EXPECTED_SOLUTION_PART_1_WITH_TEST_DATA


def test_part_2_with_test_data():
    test_data_part_2 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""
    with open(test_data_file_path, "w", encoding="utf-8") as f:
        f.write(test_data_part_2)
    data = load_data(day=1, year=2023, is_testmode=True)
    solution = day01.solve(data, part=2)
    assert solution == EXPECTED_SOLUTION_PART_2_WITH_TEST_DATA


def test_part_1_with_real_data():
    data = load_data(day=1, year=2023, is_testmode=False)
    solution = day01.solve(data, part=1)
    assert solution == EXPECTED_SOLUTION_PART_1_WITH_REAL_DATA


def test_part_2_with_real_data():
    data = load_data(day=1, year=2023, is_testmode=False)
    solution = day01.solve(data, part=2)
    assert solution == EXPECTED_SOLUTION_PART_2_WITH_REAL_DATA
