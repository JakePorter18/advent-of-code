from itertools import cycle, zip_longest


def zip_cycle(*iterables, empty_default=None):
    cycles = [cycle(i) for i in iterables]
    for _ in zip_longest(*iterables):
        yield tuple(next(i, empty_default) for i in cycles)


# day5
with open("2021//day5.txt", "r", encoding="utf8") as f:
    lines = [line.rstrip("\n") for line in f]

moves = [line.split("->") for line in lines]


def get_axis_range(a: int, b: int) -> list[int]:
    if a == b:
        return [a]
    elif a < b:
        return list(range(a, b + 1))
    elif a > b:
        return list(reversed(range(b, a + 1)))
    else:
        raise ValueError


class Line:
    def __init__(self, input_str: list[str]) -> None:
        left, right = input_str
        l_x, l_y = left.split(",")
        r_x, r_y = right.split(",")

        self.l_x = int(l_x)
        self.r_x = int(r_x)
        self.l_y = int(l_y)
        self.r_y = int(r_y)

        self.is_simple: bool = (self.l_x == self.r_x) or (self.r_y == self.l_y)

        self.x: list[int] = get_axis_range(self.l_x, self.r_x)
        self.y: list[int] = get_axis_range(self.l_y, self.r_y)

        self.coordinates: list[tuple[int, int]] = list(zip_cycle(self.x, self.y))  # type: ignore

        self.is_invalid: bool = not all(self.coordinates)


lines: list[Line] = [Line(move) for move in moves]
# lines = [line for line in lines if line.is_simple]
invalid_lines = [line for line in lines if line.is_invalid]
# print(len(invalid_lines))


record: dict[tuple[int, int], int] = {}
for line in lines:
    if not line.is_simple:
        print(line.coordinates)
    for coord in line.coordinates:
        if coord in record:
            record[coord] += 1
        else:
            record[coord] = 1


more_than_one: dict[tuple[int, int], int] = {
    key: value for key, value in record.items() if value > 1
}
# print(more_than_one.keys())
print(len(more_than_one))
