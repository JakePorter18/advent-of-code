import pandas as pd

with open("day5.txt", "r", encoding="utf8") as f:
    lines = [line.rstrip("\n") for line in f]


moves = lines[10:]

data = pd.DataFrame(moves, columns=["moves"])
data[["a", "move", "c", "from", "e", "to"]
     ] = data["moves"].str.split(" ", expand=True)
data.drop(columns=["a", "c", "e", "moves"], inplace=True)
data = data.apply(pd.to_numeric)

print(data)


class Stack:
    stack = {
        1: ["F", "H", "M", "T", "V", "L", "D"],
        2: ["P", "N", "T", "C", "J", "G", "Q", "H"],
        3: ["H", "P", "M", "D", "S", "R"],
        4: ["F", "V", "B", "L"],
        5: ["Q", "L", "G", "H", "N"],
        6: ["P", "M", "R", "G", "D", "B", "W"],
        7: ["Q", "L", "H", "C", "R", "N", "M", "G"],
        8: ["W", "L", "C"],
        9: ["T", "M", "Z", "J", "Q", "L", "D", "R"],
    }

    def move(self, amount, source, to):
        for _ in range(amount):
            item = self.stack[source].pop(0)
            self.stack[to].insert(0, item)

    def move_multiple(self, amount, source, to):
        items = [self.stack[source].pop(0) for _ in range(amount)]
        self.stack[to] = items + self.stack[to]


stack = Stack()
for index, row in data.iterrows():
    stack.move_multiple(row["move"], row["from"], row["to"])

print(stack.stack)

for i in range(9):
    print(stack.stack[i + 1][0], end="")
