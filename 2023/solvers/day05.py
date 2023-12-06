# pylint: disable=missing-module-docstring, missing-docstring

from enum import Enum


class Overlap(Enum):
    INVALID = -1
    NO_OVERLAP = 0
    I1_INCLUDES_I2 = 1
    I2_INCLUDES_I1 = 2
    I2_LEFT_OF_I1 = 3
    I2_RIGHT_OF_I1 = 4


def process_data(
    data: list[str],
) -> tuple[list[int], dict[str : list[tuple[int, int, int]]]]:
    """Parses raw input data into more readily usable format as described below.

    Args:
        data:
            Raw data in the common "list of strings" format output by the
            `data_io` module.

    Returns:
        A tuple of two elements, the first being the list of initial seeds and
        the second being a dictionary of the required mappings, where the string
        keys name the mapping and the values are lists of tuples of integers,
        where each tuple corresponds to a (destination range start, source range
        start, range length) as per the puzzle description.
    """
    init_seeds = [int(n) for n in data[0].replace("seeds: ", "").split()]
    mappings = {}
    curr_key = ""
    for line in data[1:]:
        if line and line[0].isalpha():
            curr_key = line.replace(" map:", "")
            mappings[curr_key] = []
        elif line and line[0].isnumeric():
            mappings[curr_key].append(tuple(int(x) for x in line.split()))
    return (init_seeds, mappings)


def get_int_overlaps(
    int1: tuple[int, int, int], int2: tuple[int, int, int]
) -> Overlap:
    if int2[0] >= int1[1] or int2[1] <= int1[0]:
        # "No overlap"
        return Overlap.NO_OVERLAP
    if int2[0] >= int1[0] and int2[1] <= int1[1]:
        # "int1 includes int2"
        return Overlap.I1_INCLUDES_I2
    if int2[0] <= int1[0] and int2[1] >= int1[1]:
        # "int2 includes int1"
        return Overlap.I2_INCLUDES_I1
    if int2[0] < int1[0]:
        # "int2 overlaps int1 on the left side of int1"
        return Overlap.I2_LEFT_OF_I1
    if int2[0] >= int1[0]:
        # "int2 overlaps int1 on the right side of int1"
        return Overlap.I2_RIGHT_OF_I1
    return Overlap.INVALID  # This should never happen


def remap(
    l1_map: list[tuple[int, int, int]], l2_int: tuple[int, int, int]
) -> list[tuple[int, int, int]]:
    new_l1_map = []
    for l1_int in l1_map:
        overlap = get_int_overlaps(l1_int, l2_int)
        if overlap == Overlap.NO_OVERLAP:
            new_l1_map.append(l1_int)
        elif overlap == Overlap.I1_INCLUDES_I2:
            if l1_int[0] != l2_int[0]:
                new_l1_map.append((l1_int[0], l2_int[0], l1_int[2]))
            new_l1_map.append((l2_int[0], l2_int[1], l1_int[2] + l2_int[2]))
            if l1_int[1] != l2_int[1]:
                new_l1_map.append((l2_int[1], l1_int[1], l1_int[2]))
        elif overlap == Overlap.I2_INCLUDES_I1:
            new_l1_map.append((l1_int[0], l1_int[1], l1_int[2] + l2_int[2]))
        elif overlap == Overlap.I2_LEFT_OF_I1:
            new_l1_map.append((l1_int[0], l2_int[1], l1_int[2] + l2_int[2]))
            if l1_int[1] != l2_int[1]:
                new_l1_map.append((l2_int[1], l1_int[1], l1_int[2]))
        elif overlap == Overlap.I2_RIGHT_OF_I1:
            if l1_int[0] != l2_int[0]:
                new_l1_map.append((l1_int[0], l2_int[0], l1_int[2]))
            new_l1_map.append((l2_int[0], l1_int[1], l1_int[2] + l2_int[2]))
    return new_l1_map


def collapse_maps(
    mappings: dict[str : list[tuple[int, int, int]]]
) -> list[tuple[int, int, int]]:
    """Collapse all mappings to a single mapping in (start, end, offset) format.

    Args:
        mappings: A dictionary of consecutieve mappings (seed-to-soil, soil-to-
        fertilizer, ..., humidity-to-location) output by `process_data()`.

    Returns:
        A list of 3-tuples, where the first element of each tuple defines the
        zero-based beginning index of an interval for seeds, the second
        signifies the zero-based end index (exclusive) and the last element is
        the offset to be applied to seeds in that interval in order to get to
        the corresponding location.
    """
    # Sort by source range start
    map_list_sorted = [sorted(m, key=lambda x: x[1]) for m in mappings.values()]
    intuitive_maps = []
    for lst in map_list_sorted:
        level_maps = []
        for tup in lst:
            start = tup[1]
            end = tup[1] + tup[2]
            offset = tup[0] - tup[1]
            level_maps.append((start, end, offset))
        intuitive_maps.append(level_maps)
    seeds_range = [(0, intuitive_maps[0][-1][1], 0)]
    l1_map = seeds_range
    for l2_map in intuitive_maps:
        for interval in l2_map:
            l1_map = remap(l1_map, interval)
    return l1_map


def map_seed2loc(seed: int, seed2loc: list[tuple[int, int, int]]) -> int:
    for start, end, offset in seed2loc:
        if start <= seed < end:
            loc = seed + offset
            break
    return loc


def solve_part_1(
    init_seeds: list[int], mappings: dict[str : list[tuple[int, int, int]]]
) -> int:
    locations = []
    for seed in init_seeds:
        locations.append(map_seed2loc(seed, mappings))
    return min(locations)


def solve_part_2(
    init_seeds: list[int], mappings: dict[str : list[tuple[int, int, int]]]
) -> int:
    seed_ranges = list(zip(init_seeds[::2], init_seeds[1::2]))
    seed2loc = collapse_maps(mappings)
    print("All maps flattened into one! Now searching for min location ID...")
    min_locs = []
    for seed_range in seed_ranges:
        locs = []
        for seed in range(seed_range[0], seed_range[0] + seed_range[1]):
            locs.append(map_seed2loc(seed, seed2loc))
        min_locs.append(min(locs))
    return min(min_locs)


def solve(data: list[str], part: int) -> int:
    init_seeds, mappings = process_data(data)
    if part == 1:
        solution = solve_part_1(init_seeds, mappings)
    else:  # part == 2
        solution = solve_part_2(init_seeds, mappings)
    return solution
