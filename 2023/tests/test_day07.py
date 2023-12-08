# pylint: disable=missing-module-docstring, missing-docstring

import os
from pathlib import Path

from data_io import load_data
from solvers import day07

test_data_file_path = os.path.join("data", f"{Path(__file__).stem}.txt")

TEST_DATA = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

EXPECTED_SOLUTION_PART_1_WITH_TEST_DATA = 6440
EXPECTED_SOLUTION_PART_1_WITH_REAL_DATA = 0

EXPECTED_SOLUTION_PART_2_WITH_TEST_DATA = 0
EXPECTED_SOLUTION_PART_2_WITH_REAL_DATA = 0


def test_part_1_with_test_data():
    with open(test_data_file_path, "w", encoding="utf-8") as f:
        f.write(TEST_DATA)
    data = load_data(day=7, year=2023, is_testmode=True)
    solution = day07.solve(data, part=1)
    assert solution == EXPECTED_SOLUTION_PART_1_WITH_TEST_DATA


def test_part_1_with_real_data():
    data = load_data(day=7, year=2023, is_testmode=False)
    solution = day07.solve(data, part=1)
    assert solution == EXPECTED_SOLUTION_PART_1_WITH_REAL_DATA


def test_part_2_with_test_data():
    with open(test_data_file_path, "w", encoding="utf-8") as f:
        f.write(TEST_DATA)
    data = load_data(day=7, year=2023, is_testmode=True)
    solution = day07.solve(data, part=2)
    assert solution == EXPECTED_SOLUTION_PART_2_WITH_TEST_DATA


def test_part_2_with_real_data():
    data = load_data(day=7, year=2023, is_testmode=False)
    solution = day07.solve(data, part=2)
    assert solution == EXPECTED_SOLUTION_PART_2_WITH_REAL_DATA
