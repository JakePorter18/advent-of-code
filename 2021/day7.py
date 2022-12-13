from typing import Callable, Optional


with open("2021\\day7.txt", "r", encoding="utf8") as f:
    data: list[str] = [line.split(",") for line in f][0]

numbers: list[int] = [int(x) for x in data]


def triangular(num: int) -> int:
    return num * (num + 1) // 2


class Crab:
    def __init__(self, x: int, fuel: int = 0, fuel_burn: Optional[Callable] = None):
        self.x: int = x
        self.fuel_used: int = fuel
        self.fuel_burn = (lambda x: x) if fuel_burn is None else fuel_burn

    def move_to_pos(self, x):
        self.fuel_used += self.fuel_burn(abs(self.x - x))
        self.x = x
        return self.fuel_used


fuel_usage: dict[int, int] = {}
for x in range(min(numbers), max(numbers) + 1):
    crabs: list[Crab] = [Crab(i, fuel_burn=triangular) for i in numbers]
    fuel_usage[x] = sum(crab.move_to_pos(x) for crab in crabs)

print(min(fuel_usage.values()))
