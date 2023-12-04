# pylint: disable=missing-module-docstring, missing-docstring

import os
from pathlib import Path

from data_io import load_data
from solvers import day04

test_data_file_path = os.path.join("data", f"{Path(__file__).stem}.txt")

TEST_DATA = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
with open(test_data_file_path, "w", encoding="utf-8") as f:
    f.write(TEST_DATA)

EXPECTED_SOLUTION_PART_1_WITH_TEST_DATA = 13
EXPECTED_SOLUTION_PART_2_WITH_TEST_DATA = 30

EXPECTED_SOLUTION_PART_1_WITH_REAL_DATA = 25571
EXPECTED_SOLUTION_PART_2_WITH_REAL_DATA = 8805731


def test_part_1_with_test_data():
    data = load_data(day=4, year=2023, is_testmode=True)
    solution = day04.solve(data, part=1)
    assert solution == EXPECTED_SOLUTION_PART_1_WITH_TEST_DATA


def test_part_2_with_test_data():
    data = load_data(day=4, year=2023, is_testmode=True)
    solution = day04.solve(data, part=2)
    assert solution == EXPECTED_SOLUTION_PART_2_WITH_TEST_DATA


def test_part_1_with_real_data():
    data = load_data(day=4, year=2023, is_testmode=False)
    solution = day04.solve(data, part=1)
    assert solution == EXPECTED_SOLUTION_PART_1_WITH_REAL_DATA


def test_part_2_with_real_data():
    data = load_data(day=4, year=2023, is_testmode=False)
    solution = day04.solve(data, part=2)
    assert solution == EXPECTED_SOLUTION_PART_2_WITH_REAL_DATA
