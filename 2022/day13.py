# from aocd import get_data
# import ast
import json


def get_list_of_pairs(raw_data: str) -> list[tuple[list, list]]:
    data_list = raw_data.strip().split()
    # Can also use ast.literal_eval() instead of json.loads() below
    data_list_no_str = [json.loads(x) for x in data_list]
    list_of_pairs = list(zip(data_list_no_str[::2], data_list_no_str[1::2]))
    return list_of_pairs


def is_valid_list_pair(left: list, right: list) -> bool:
    # print(f"{left=} , {right=}")
    while len(left) > 0 and len(right) > 0:
        l = left.pop(0)
        r = right.pop(0)
        # print(f"{l=} , {r=}")
        if isinstance(l, int) and isinstance(r, int):
            if l > r:
                return False
            elif l < r:
                return True
            else:
                continue
        if isinstance(l, int):
            l = [l]
        if isinstance(r, int):
            r = [r]
        result = is_valid_list_pair(l, r)
        if result == None:
            continue
        else:
            return result
    if len(left) == 0 and len(right) > 0:
        return True
    elif len(right) == 0 and len(left) > 0:
        return False
    else:
        return None


def get_solutionn_part_1(pairs: list[tuple[list, list]]) -> int:
    sum_of_correct_indices = 0
    for idx, (left, right) in enumerate(pairs):
        # print(f"\n{idx=} , {left=} , {right=}")
        # print(is_valid_list_pair(left, right))
        if is_valid_list_pair(left.copy(), right.copy()):
            sum_of_correct_indices += idx + 1
    return sum_of_correct_indices


def get_solution_part_2(raw_data: str) -> int:
    pass


def main() -> None:
    # data = get_data(day=13, year=2022)

    with open("data/day13.txt", "r") as f:
        data = f.read()

    pairs = get_list_of_pairs(data)
    print(get_solutionn_part_1(pairs))


if __name__ == "__main__":
    main()
