from aocd import data, submit


def first_marker_pos(signal: str, length: int) -> int:
    marker_pos = 0
    for i in range(len(signal) - length):
        if len(set(signal[i : i + length])) == length:
            marker_pos = i + length
            break
    return marker_pos


answer_a = first_marker_pos(data, 4)
# submit(answer_a, part="a", day=6, year=2022)

answer_b = first_marker_pos(data, 14)
# submit(answer_b, part="b", day=6, year=2022)
