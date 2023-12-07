# pylint: disable=missing-module-docstring, missing-docstring


def process_data(
    data: list[str],
) -> tuple[list[int], list[list[tuple[int, int, int]]]]:
    """Parses raw input data into more readily usable format as described below.

    Args:
        data:
            Raw data in the common "list of strings" format output by the
            `data_io` module.

    Returns:
        A tuple of two elements, the first being the list of initial seeds for
        part 1 and the initial seed _ranges_ for part 2, the second being an
        ordered list of the required mappings, where each element is in turn a
        lists of tuples of integers, where each tuple corresponds to the
        (destination range start, source range start, range length) format, as
        per the puzzle description.
    """
    seeds = [int(n) for n in data[0].replace("seeds: ", "").split()]
    mappings = []
    for line in data[1:]:
        if line and line[0].isalpha():
            mappings.append([])
        elif line and line[0].isnumeric():
            mappings[-1].append(tuple(int(x) for x in line.split()))
    return (seeds, mappings)


def map_seed2loc(seed: int, mappings: list[list[tuple[int, int, int]]]) -> int:
    src = seed
    for mapping in mappings:
        for dest_min, src_min, rng_len in mapping:
            dest = src
            if src_min <= src < src_min + rng_len:
                dest = dest_min + src - src_min
                src = dest
                break
    return dest


def simplify_maps(
    mappings: list[list[tuple[int, int, int]]]
) -> list[list[tuple[int, int, int]]]:
    """Convert mappings to more readily understandable format

    Args:
        mappings: A list of lists of 3-tuples in the original format described
        in the puzzle where each tuple is a (destination range start, source
        range start, range length) tuple.

    Returns:
        A list of lists of 3-tuples where the tuples correspond to the format:
        (source range start, source range end, offset to be applied in order to
        get to destination). Also the tuples in each sub-list are sorted by
        source range start.
    """
    better_mappings = []
    for m in mappings:
        better_mappings.append([])
        for interval in m:
            src_start = interval[1]
            src_end = interval[1] + interval[2]
            offset = interval[0] - interval[1]
            better_mappings[-1].append((src_start, src_end, offset))
        better_mappings[-1].sort(key=lambda x: x[0])
    return better_mappings


def map_intervals(
    spans_in: list[tuple[int, int]], mappings: list[list[tuple[int, int, int]]]
) -> list[tuple[int, int]]:
    spans_out = []
    return spans_out


def solve_part_1(
    init_seeds: list[int], mappings: list[list[tuple[int, int, int]]]
) -> int:
    locations = []
    for seed in init_seeds:
        locations.append(map_seed2loc(seed, mappings))
    return min(locations)


def solve_part_2(
    init_seeds: list[int], mappings: list[list[tuple[int, int, int]]]
) -> int:
    better_maps = simplify_maps(mappings)
    seed_ranges = list(zip(init_seeds[::2], init_seeds[1::2]))
    intervals = seed_ranges
    for map_level in better_maps:
        intervals = map_intervals(intervals, map_level)
    return min(interval[0] for interval in intervals)


def solve(data: list[str], part: int) -> int:
    init_seeds, mappings = process_data(data)
    if part == 1:
        solution = solve_part_1(init_seeds, mappings)
    else:  # part == 2
        solution = solve_part_2(init_seeds, mappings)
    return solution
