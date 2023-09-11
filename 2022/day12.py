from aocd import get_data


class Grid:
    def __init__(self, raw_data: str) -> None:
        self.data = raw_data.splitlines()
        self.n_rows = len(self.data)
        self.n_cols = len(self.data[0])

    def __getitem__(self, idx: tuple[int, int]) -> dict[tuple[int, int], str]:
        return {(idx[0], idx[1]): self.data[idx[0]][idx[1]]}

    def _get_height(self, idx: tuple[int, int]) -> int:
        height = -1
        v = self[idx][idx]
        if v.islower():
            height = ord(v) - ord("a") + 1
        elif v == "E":
            height = ord("z") - ord("a") + 1
        elif v == "S":
            height = 1
        return height

    def get_traversable_neighbours(
        self, idx: tuple[int, int]
    ) -> list[dict[tuple[int, int], str]]:
        neighbours = []
        height = self._get_height(idx)
        i, j = idx
        idx_up = (i - 1, j)
        idx_right = (i, j + 1)
        idx_down = (i + 1, j)
        idx_left = (i, j - 1)

        if i > 0 and self._get_height(idx_up) - height <= 1:
            neighbours.append(self[idx_up])
        if i < self.n_rows - 1 and self._get_height(idx_down) - height <= 1:
            neighbours.append(self[idx_down])
        if j > 0 and self._get_height(idx_left) - height <= 1:
            neighbours.append(self[idx_left])
        if j < self.n_cols - 1 and self._get_height(idx_right) - height <= 1:
            neighbours.append(self[idx_right])

        return neighbours


def main() -> None:
    # data = get_data(day=12, year=2022)

    with open("data/day12_test.txt", "r") as f:
        data = f.read()

    grid = Grid(data)

    test_idx = (1, 5)
    print(grid[test_idx])
    print(grid.get_traversable_neighbours(test_idx))


if __name__ == "__main__":
    main()
