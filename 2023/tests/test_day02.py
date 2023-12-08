# pylint: disable=missing-module-docstring, missing-docstring

import os
from pathlib import Path

from data_io import load_data
from solvers import day02

test_data_file_path = os.path.join("data", f"{Path(__file__).stem}.txt")

TEST_DATA = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

EXPECTED_SOLUTION_PART_1_WITH_TEST_DATA = 8
EXPECTED_SOLUTION_PART_1_WITH_REAL_DATA = 2541

EXPECTED_SOLUTION_PART_2_WITH_TEST_DATA = 2286
EXPECTED_SOLUTION_PART_2_WITH_REAL_DATA = 66016


def test_part_1_with_test_data():
    with open(test_data_file_path, "w", encoding="utf-8") as f:
        f.write(TEST_DATA)
    data = load_data(day=2, year=2023, is_testmode=True)
    solution = day02.solve(data, part=1)
    assert solution == EXPECTED_SOLUTION_PART_1_WITH_TEST_DATA


def test_part_1_with_real_data():
    data = load_data(day=2, year=2023, is_testmode=False)
    solution = day02.solve(data, part=1)
    assert solution == EXPECTED_SOLUTION_PART_1_WITH_REAL_DATA


def test_part_2_with_test_data():
    with open(test_data_file_path, "w", encoding="utf-8") as f:
        f.write(TEST_DATA)
    data = load_data(day=2, year=2023, is_testmode=True)
    solution = day02.solve(data, part=2)
    assert solution == EXPECTED_SOLUTION_PART_2_WITH_TEST_DATA


def test_part_2_with_real_data():
    data = load_data(day=2, year=2023, is_testmode=False)
    solution = day02.solve(data, part=2)
    assert solution == EXPECTED_SOLUTION_PART_2_WITH_REAL_DATA
