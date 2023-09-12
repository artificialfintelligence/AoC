from aocd import get_data


class Point:
    def __init__(self, *coords: int, value: str) -> None:
        if len(coords) == 2:  # x & y supplied as separate args
            self._x = coords[0]
            self._y = coords[1]
        else:  # (x, y) supplied as a tuple
            self._x = coords[0][0]
            self._y = coords[0][1]
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
        self.sPoint = None
        self.ePoint = None
        for i, row in enumerate(self.data):
            if "S" in row:
                j = row.find("S")
                self.sPoint = Point(i, j, value="S")
            if "E" in row:
                j = row.find("E")
                self.ePoint = Point(i, j, value="E")

    def __getitem__(self, idx: tuple[int, int]) -> Point:
        return Point(idx, value=self.data[idx[0]][idx[1]])

    def __repr__(self) -> str:
        return "\n".join(self.data)

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


class Problem:
    def __init__(self, grid: Grid) -> None:
        self.grid = grid

    def solve_part_1(self, from_coords: tuple[int, int]) -> int:
        found = False
        n_steps_till_found = -1

        curr_coords = from_coords
        curr_dist = 0
        queue = [(curr_coords, curr_dist)]
        seenCoords = {curr_coords}
        while queue and not found:
            curr_node = queue.pop(0)
            curr_coords, curr_dist = curr_node[0], curr_node[1]
            for neighb in self.grid.get_traversable_neighbours(curr_coords):
                if not neighb.coords in seenCoords:
                    seenCoords.add(neighb.coords)
                    queue.append((neighb.coords, curr_dist + 1))
                    if neighb.coords == self.grid.ePoint.coords:
                        found = True
                        n_steps_till_found = curr_dist + 1
        return n_steps_till_found

    def solve_part_2(self) -> None:
        min_dist = float("inf")
        for i, row in enumerate(self.grid.data):
            for j, value in enumerate(row):
                if self.grid[i, j].value in ["a", "S"]:
                    dist = self.solve_part_1((i, j))
                    if 0 < dist < min_dist:
                        min_dist = dist
        return min_dist


def main() -> None:
    # data = get_data(day=12, year=2022)

    with open("data/day12.txt", "r") as f:
        data = f.read()

    grid = Grid(data)
    problem = Problem(grid)

    n_steps = problem.solve_part_1(grid.sPoint.coords)
    print(f"Part 1: From S to E in {n_steps} steps.")

    print("Part 2: The minimum 'a' to 'z' distance is ...")
    min_steps = problem.solve_part_2()
    print(f"... {min_steps} steps.")

    # print(grid.sPoint, grid.ePoint)
    # print(grid.sPoint.height, grid.ePoint.height)

    # test_idx = (1, 5)
    # print(grid[test_idx])
    # valid_neighbs = grid.get_traversable_neighbours(test_idx)
    # print(valid_neighbs)
    # print([p.height for p in valid_neighbs])


if __name__ == "__main__":
    main()
