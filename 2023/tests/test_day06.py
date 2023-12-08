# pylint: disable=missing-module-docstring, missing-docstring

import os
from pathlib import Path

from data_io import load_data
from solvers import day06

test_data_file_path = os.path.join("data", f"{Path(__file__).stem}.txt")

TEST_DATA = """Time:      7  15   30
Distance:  9  40  200
"""

EXPECTED_SOLUTION_PART_1_WITH_TEST_DATA = 288
EXPECTED_SOLUTION_PART_1_WITH_REAL_DATA = 3316275

EXPECTED_SOLUTION_PART_2_WITH_TEST_DATA = 71503
EXPECTED_SOLUTION_PART_2_WITH_REAL_DATA = 27102791


def test_part_1_with_test_data():
    with open(test_data_file_path, "w", encoding="utf-8") as f:
        f.write(TEST_DATA)
    data = load_data(day=6, year=2023, is_testmode=True)
    solution = day06.solve(data, part=1)
    assert solution == EXPECTED_SOLUTION_PART_1_WITH_TEST_DATA


def test_part_1_with_real_data():
    data = load_data(day=6, year=2023, is_testmode=False)
    solution = day06.solve(data, part=1)
    assert solution == EXPECTED_SOLUTION_PART_1_WITH_REAL_DATA


def test_part_2_with_test_data():
    with open(test_data_file_path, "w", encoding="utf-8") as f:
        f.write(TEST_DATA)
    data = load_data(day=6, year=2023, is_testmode=True)
    solution = day06.solve(data, part=2)
    assert solution == EXPECTED_SOLUTION_PART_2_WITH_TEST_DATA


def test_part_2_with_real_data():
    data = load_data(day=6, year=2023, is_testmode=False)
    solution = day06.solve(data, part=2)
    assert solution == EXPECTED_SOLUTION_PART_2_WITH_REAL_DATA
