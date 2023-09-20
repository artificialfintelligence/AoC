# from aocd import get_data
# import ast
import json


class Packet:
    def __init__(self, data):
        self.data = data.copy()

    def __lt__(self, other):
        if not isinstance(other, Packet):
            raise ValueError("Cannot compare Packet with non-Packet object.")
        left = self.data
        right = other.data
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
            result = Packet(l) < Packet(r)
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


def get_list_of_pairs(raw_data: str) -> list[tuple[list, list]]:
    data_list = raw_data.strip().split()
    # Can also use ast.literal_eval() instead of json.loads() below
    data_list_no_str = [json.loads(x) for x in data_list]
    list_of_pairs = list(zip(data_list_no_str[::2], data_list_no_str[1::2]))
    return list_of_pairs


def get_solution_part_1(pairs: list[tuple[list, list]]) -> int:
    sum_of_correct_indices = 0
    for idx, (left, right) in enumerate(pairs):
        # print(f"\n{idx=} , {left=} , {right=}")
        # print(Packet(left) < Packet(right))
        if Packet(left) < Packet(right):
            sum_of_correct_indices += idx + 1
    return sum_of_correct_indices


def get_solution_part_2(pairs: list[tuple[list, list]]) -> int:
    pass


def main() -> None:
    # data = get_data(day=13, year=2022)

    with open("data/day13.txt", "r") as f:
        data = f.read()
    pairs = get_list_of_pairs(data)
    print(get_solution_part_1(pairs))

    pairs_extended = pairs + [([[2]], [[6]])]
    print(get_solution_part_1(pairs_extended))


if __name__ == "__main__":
    main()
