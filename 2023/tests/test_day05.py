# pylint: disable=missing-module-docstring, missing-docstring

import os
from pathlib import Path

from data_io import load_data
from solvers import day05

test_data_file_path = os.path.join("data", f"{Path(__file__).stem}.txt")

TEST_DATA = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

EXPECTED_SOLUTION_PART_1_WITH_TEST_DATA = 35
EXPECTED_SOLUTION_PART_1_WITH_REAL_DATA = 227653707

EXPECTED_SOLUTION_PART_2_WITH_TEST_DATA = 46
EXPECTED_SOLUTION_PART_2_WITH_REAL_DATA = 78775051


def test_part_1_with_test_data():
    with open(test_data_file_path, "w", encoding="utf-8") as f:
        f.write(TEST_DATA)
    data = load_data(day=5, year=2023, is_testmode=True)
    solution = day05.solve(data, part=1)
    assert solution == EXPECTED_SOLUTION_PART_1_WITH_TEST_DATA


def test_part_1_with_real_data():
    data = load_data(day=5, year=2023, is_testmode=False)
    solution = day05.solve(data, part=1)
    assert solution == EXPECTED_SOLUTION_PART_1_WITH_REAL_DATA


def test_part_2_with_test_data():
    with open(test_data_file_path, "w", encoding="utf-8") as f:
        f.write(TEST_DATA)
    data = load_data(day=5, year=2023, is_testmode=True)
    solution = day05.solve(data, part=2)
    assert solution == EXPECTED_SOLUTION_PART_2_WITH_TEST_DATA


def test_part_2_with_real_data():
    data = load_data(day=5, year=2023, is_testmode=False)
    solution = day05.solve(data, part=2)
    assert solution == EXPECTED_SOLUTION_PART_2_WITH_REAL_DATA
