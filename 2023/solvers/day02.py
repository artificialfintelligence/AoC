# pylint: disable=missing-module-docstring, missing-docstring

import re


def solve(data: list[str], part: int) -> int:
    sum_of_valid_ids = 0

    cube_counts_total = {"red": 12, "green": 13, "blue": 14}

    if part == 1:
        for row in [r for r in data if r != ""]:
            is_valid = True
            cube_counts = {"red": 0, "green": 0, "blue": 0}
            parsed_row = re.match(r"^Game (\d+): (.*)", row)
            row_id, row_data = int(parsed_row.group(1)), parsed_row.group(2)
            pairs_flat = [
                item.strip()
                for sublist in [r.split(",") for r in row_data.split(";")]
                for item in sublist
            ]
            for item in pairs_flat:
                key, value_str = item.split()[::-1]
                if int(value_str) > cube_counts_total[key]:
                    is_valid = False
                    break
            if is_valid:
                sum_of_valid_ids += row_id
    else:  # part == 2
        raise NotImplementedError(
            f"Solver for part {part} not implemented yet."
        )

    return sum_of_valid_ids
