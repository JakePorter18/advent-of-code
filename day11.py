import re
from tqdm import tqdm
import math


with open("day11.txt", "r", encoding="utf8") as f:
    lines: list[str] = [line.rstrip("\n") for line in f]


chunks = [lines[7 * i : 7 * (i + 1)] for i in range(len(lines) // 7 + 1)]

# print(chunks)


class Monkey:
    def __init__(self, chunk):
        self.number = int(re.findall(r"\d+", chunk[0])[0])
        items = re.findall(r"\d+", chunk[1])
        self.items = [int(item) for item in items]
        self.operation = self.get_function(chunk[2][13:])
        self.test = int(re.findall(r"\d+", chunk[3])[0])
        self.is_true = int(re.findall(r"\d+", chunk[4])[0])
        self.is_false = int(re.findall(r"\d+", chunk[5])[0])
        self.inspected: int = 0

    def __str__(self):
        return f"{self.number=} {self.items=} {self.operation=} {self.test=} {self.is_true=} {self.is_false=}"

    def inspect(self, item, max_rem) -> tuple[int, int]:
        worry: int = self.operation(item)
        self.inspected += 1
        if (worry) % self.test == 0:
            return (self.is_true, worry % max_rem)
        else:
            return (self.is_false, worry % max_rem)

    def inspect_all_items(self, max_rem) -> list[tuple[int, int]]:
        inspections: list[tuple[int, int]] = [
            self.inspect(item, max_rem) for item in self.items
        ]
        self.items.clear()
        return inspections

    def get_function(self, string):
        def operation(old):
            operations = {
                "new = old * 11": old * 11,
                "new = old + 1": old + 1,
                "new = old * 7": old * 7,
                "new = old + 3": old + 3,
                "new = old + 6": old + 6,
                "new = old + 5": old + 5,
                "new = old * old": old * old,
                "new = old + 7": old + 7,
                "new = old * 19": old * 19,
            }
            new = operations[string]
            return new

        return operation

    def operate(self, val):
        return self.operation(val)


monkeys: list[Monkey] = [Monkey(chunk) for chunk in chunks]

rem = math.prod([monkey.test for monkey in monkeys])


def inspection_round(monkeys_list, max_rem):
    for monkey in monkeys_list:
        inspections = monkey.inspect_all_items(max_rem)
        for inspection in inspections:
            monkeys_list[inspection[0]].items.append(inspection[1])


for _ in tqdm(range(10000)):
    inspection_round(monkeys, rem)


inspected = [monkey.inspected for monkey in monkeys]
inspected.sort(reverse=True)
print(inspected)
print(inspected[0] * inspected[1])
