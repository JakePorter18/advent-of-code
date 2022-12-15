from typing import Optional, Any
import os

os.system("clear")

with open("day14.txt", "r", encoding="utf8") as f:
    lines: list[str] = [line.rstrip("\n") for line in f]


SOURCE: tuple[int, int] = (500, 0)


class Rock:
    def __init__(self) -> None:
        pass

    def __str__(self):
        return "█"


class Air:
    def __init__(self) -> None:
        pass

    def __str__(self):
        return " "


class Grid:
    def __init__(self, width: int, height: int) -> None:
        self.grid: list[list[Rock | Sand | Air]] = [
            [Air() for _ in range(width + 10)] for _ in range(height + 10)
        ]
        self.width = width
        self.height = height

    def get(self, x: int, y: int) -> Optional[Any]:
        return self.grid[y][x]

    def add_rock(self, x: int, y: int) -> None:
        self.grid[y][x] = Rock()

    def add_floor(self, y_height):
        for i in range(self.width):
            self.grid[y_height][i] = Rock()

    def display(self, x_min=0, x_max=0, y_min=1000, y_max=1000):

        for j, row in enumerate(self.grid):
            if j >= y_min and j <= y_max:
                for i, cell in enumerate(row):
                    if i >= x_min and i <= x_max:
                        print(f"{cell} ", end="")
                print()


class Sand:
    def __init__(self, position: tuple[int, int], grid: Grid) -> None:
        self.x, self.y = position
        self.at_rest: bool = False
        if type(grid.get(self.x, self.y)) == Sand:
            raise ValueError("Can't Add sand")

    def __str__(self) -> str:
        return "O"

    def move(self, grid: Grid):
        while not self.at_rest:
            if type(grid.get(self.x, self.y + 1)) == Air:
                self.y += 1
            elif type(grid.get(self.x - 1, self.y + 1)) == Air:
                self.x -= 1
                self.y += 1
            elif type(grid.get(self.x + 1, self.y + 1)) == Air:
                self.x += 1
                self.y += 1
            else:
                self.at_rest = True
        grid.grid[self.y][self.x] = self


rock_lines: list[list[str]] = [line.split(" -> ") for line in lines]

max_x = 0
max_y = 0

segments = []
for line in rock_lines:
    tuples = [tuple(x.split(",")) for x in line]
    rock_line = []
    for i, coord in enumerate(tuples):
        x: int = int(coord[0])
        y: int = int(coord[1])
        max_x: int = max(x, max_x)
        max_y: int = max(y, max_y)
        if i < len(tuples) - 1:
            n_x: int = int(tuples[i + 1][0])
            n_y: int = int(tuples[i + 1][1])
            x_1: int = min(x, n_x)
            x_2: int = max(x, n_x)
            y_1: int = min(y, n_y)
            y_2: int = max(y, n_y)
            if x_1 == x_2:
                seg_y: list[int] = list(range(y_1, y_2 + 1))
                seg_x: list[int] = [x_1] * len(seg_y)
            else:
                seg_x: list[int] = list(range(x_1, x_2 + 1))
                seg_y: list[int] = [y_1] * len(seg_x)

            segment: list[tuple[int, int]] = list(zip(seg_x, seg_y))
            rock_line.extend(segment)
    segments.append(rock_line)

print(max_x, max_y)
grid: Grid = Grid(1000, 1000)


for segment in segments:
    for x, y in segment:
        grid.add_rock(x, y)

grid.add_floor(max_y + 2)


def add_sand() -> int:
    sand_added: int = 0
    while True:
        try:
            s = Sand(SOURCE, grid)
            sand_added += 1
        except ValueError:
            return sand_added
        while not s.at_rest:
            try:
                s.move(grid)
            except IndexError:
                print(f"indexerror at {(s.x,s.y)}")
                return sand_added


print(sand_added := add_sand())
