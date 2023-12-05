# pylint: disable=missing-module-docstring, missing-docstring

import re


def process_data(data: list[str]) -> tuple[list[list[int]], list[list[int]]]:
    """Parses raw input data into more readily usable format as described below.

    Args:
        data:
            Raw data in the common "list of strings" format output by the
            `data_io` module.
            example:

            ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
             "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19"]

    Returns:
        A tuple of two lists of lists of ints. The first element of the tuple is
        all the winning numbers on the cards and the second elements is the list
        of the numbers we have on the corresponding cards.
        example:

        (
            [[41, 48, 83, 86, 17], [13, 32, 20, 16, 61]],
            [[83, 86, 6, 31, 17, 9, 48, 53], [61, 30, 68, 82, 17, 32, 24, 19]]
        )
    """
    nums_winning, nums_we_have = [], []
    pattern = re.compile(r"^Card +\d+: +(.+) \| (.+)$")
    for card in data:
        matches = pattern.search(card)
        if matches:
            winning_numbers, our_numbers = matches.groups()
            nums_winning.append([int(n) for n in winning_numbers.split()])
            nums_we_have.append([int(n) for n in our_numbers.split()])
    return nums_winning, nums_we_have


def solve_part_1(
    nums_winning: list[list[int]], nums_we_have: list[list[int]]
) -> int:
    total_points = 0
    for card_idx, nums2check in enumerate(nums_we_have):
        winning_set = set(nums_winning[card_idx])
        match_count = sum(1 for n in nums2check if n in winning_set)
        card_points = 2 ** (match_count - 1) if match_count else 0
        # print(
        #     f"Card #{card_idx+1} has {match_count} matches and is worth {card_points} points."
        # )
        total_points += card_points
    return total_points


def solve_part_2(
    nums_winning: list[list[int]], nums_we_have: list[list[int]]
) -> int:
    n_cards = len(nums_winning)  # which equals `len(nums_we_have)`
    copies = [1] * n_cards
    for card_idx, nums2check in enumerate(nums_we_have):
        match_count = sum(1 for n in nums2check if n in nums_winning[card_idx])
        for idx in range(card_idx + 1, card_idx + match_count + 1):
            copies[idx] += copies[card_idx]
    return sum(copies)


def solve(data: list[str], part: int) -> int:
    nums_winning, nums_we_have = process_data(data)
    if part == 1:
        solution = solve_part_1(nums_winning, nums_we_have)
    else:  # part == 2
        solution = solve_part_2(nums_winning, nums_we_have)
    return solution
