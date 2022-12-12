import re
from typing import Any
from tqdm import tqdm
import math


with open("day11.txt", "r", encoding="utf8") as f:
    lines: list[str] = [line.rstrip("\n") for line in f]


chunks = [lines[7 * i : 7 * (i + 1)] for i in range(len(lines) // 7 + 1)]

# print(chunks)


class Item:
    def __init__(self, val):
        self.initial_val = int(val)
        self.val: int = int(val)
        self.log_history: list[Any] = []


class Monkey:
    def __init__(self, chunk):
        self.number = int(re.findall(r"\d+", chunk[0])[0])
        items: list[str] = re.findall(r"\d+", chunk[1])
        self.items: list[Item] = [Item(item) for item in items]
        self.operation = self.get_function(chunk[2][13:])
        self.test = int(re.findall(r"\d+", chunk[3])[0])
        self.is_true = int(re.findall(r"\d+", chunk[4])[0])
        self.is_false = int(re.findall(r"\d+", chunk[5])[0])
        self.inspected: int = 0
        self.log_increase = self.get_log_increase(chunk[2][13:])

    def __str__(self):
        return f"{self.number=} {self.items=} {self.operation=} {self.test=} {self.is_true=} {self.is_false=}"

    def inspect(self, item: Item, max_rem) -> tuple[int, Item]:
        worry: int = self.operation(item.val)
        self.inspected += 1
        item.log_history.append(self.log_increase)
        item.log_history.insert(0, "(")
        if (worry) % self.test == 0:
            item.val = worry % max_rem
            return (self.is_true, item)
        else:
            item.val = worry % max_rem
            return (self.is_false, item)

    def get_log_increase(self, string) -> str:
        if string == "new = old * old":
            return "x2"
        elif "+" in string or "*" not in string:
            return "0"
        else:
            return "1" if string == "new = old * 11" else "2"

    def inspect_all_items(self, max_rem) -> list[tuple[int, Item]]:
        inspections: list[tuple[int, Item]] = [
            self.inspect(item, max_rem) for item in self.items
        ]
        self.items.clear()
        return inspections

    def get_function(self, string):
        def operation(old) -> int:
            operations: dict[str, Any] = {
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
            new: int = operations[string]
            return new

        return operation

    def operate(self, val) -> int:
        return self.operation(val)


monkeys: list[Monkey] = [Monkey(chunk) for chunk in chunks]

rem: int = math.prod([monkey.test for monkey in monkeys])


def inspection_round(monkeys_list, max_rem):
    for monkey in monkeys_list:
        inspections = monkey.inspect_all_items(max_rem)
        for inspection in inspections:
            monkeys_list[inspection[0]].items.append(inspection[1])


for _ in tqdm(range(10000)):
    inspection_round(monkeys, rem)


inspected: list[int] = [monkey.inspected for monkey in monkeys]
inspected.sort(reverse=True)
print(inspected)
print(inspected[0] * inspected[1])

all_items = []
for m in monkeys:
    all_items.extend(m.items)


for item in all_items:
    val = int(round(math.log10(item.initial_val), 0))
    for step in item.log_history:
        if step == "x2":
            val *= 2
        elif step == "1":
            val += 1
        elif step == "2":
            val += 2
    print(f"{math.log10(val)=}")
