from aocd import get_data


class Point:
    def __init__(self, coords: tuple[int, int], value: str) -> None:
        self._x = coords[0]
        self._y = coords[1]
        self.value = value

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @property
    def coords(self) -> tuple[int, int]:
        return self._x, self._y

    @property
    def height(self) -> int:
        height = -1  # invalid height
        if self.value.islower():
            height = ord(self.value) - ord("a") + 1
        elif self.value == "E":
            height = ord("z") - ord("a") + 1
        elif self.value == "S":
            height = 1
        return height

    def __repr__(self) -> str:
        return f"{self.coords}: {self.value}"


class Grid:
    def __init__(self, raw_data: str) -> None:
        self.data = raw_data.splitlines()
        self.n_rows = len(self.data)
        self.n_cols = len(self.data[0])

    def __getitem__(self, idx: tuple[int, int]) -> Point:
        return Point(idx, self.data[idx[0]][idx[1]])

    def get_traversable_neighbours(self, idx: tuple[int, int]) -> list[Point]:
        neighbours = []
        height = self[idx].height

        i, j = idx
        idx_up = (i - 1, j)
        idx_right = (i, j + 1)
        idx_down = (i + 1, j)
        idx_left = (i, j - 1)

        if i > 0 and self[idx_up].height - height <= 1:
            neighbours.append(self[idx_up])
        if i < self.n_rows - 1 and self[idx_down].height - height <= 1:
            neighbours.append(self[idx_down])
        if j > 0 and self[idx_left].height - height <= 1:
            neighbours.append(self[idx_left])
        if j < self.n_cols - 1 and self[idx_right].height - height <= 1:
            neighbours.append(self[idx_right])

        return neighbours


def main() -> None:
    # data = get_data(day=12, year=2022)

    with open("data/day12_test.txt", "r") as f:
        data = f.read()

    grid = Grid(data)

    test_idx = (1, 5)
    print(grid[test_idx])
    valid_neighbs = grid.get_traversable_neighbours(test_idx)
    print(valid_neighbs)
    print([p.height for p in valid_neighbs])


if __name__ == "__main__":
    main()
