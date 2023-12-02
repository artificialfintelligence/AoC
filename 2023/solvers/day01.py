# pylint: disable=missing-module-docstring, missing-docstring

import re


def solve(data: list[str], part: int) -> int:
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

    if part == 1:
        search_pattern = r"\d"
    else:  # part == 2
        search_pattern = rf"(?=(\d|{'|'.join(str2int.keys())}))"

    calibration_total = 0

    matches = [re.findall(search_pattern, line, re.IGNORECASE) for line in data]
    digits_str = [
        [str2int[i] if i in str2int else i for i in line] for line in matches
    ]
    calibration_values = [int(l[0] + l[-1]) for l in digits_str if l != []]
    calibration_total = sum(calibration_values)

    return calibration_total
