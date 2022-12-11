from typing import Optional
import math

with open("day8.txt", "r", encoding="utf8") as f:
    lines: list[str] = [line.rstrip("\n") for line in f]
    print(len(lines))
    print(len(lines[0]))


class Tree:
    def __init__(self, height) -> None:
        self.height: int = height
        self.visible: dict[str, Optional[bool]] = {
            "left": None,
            "right": None,
            "up": None,
            "down": None,
        }

        self.can_see: dict[str, Optional[int]] = {
            "left": None,
            "right": None,
            "up": None,
            "down": None,
        }

    def check_visible(self, direction: str, max_dir_height: int) -> int:
        self.visible[direction] = self.height > max_dir_height
        return max(self.height, max_dir_height)

    def is_visible(self) -> bool:
        return any(self.visible.values())

    def is_invalid(self) -> bool:
        return None in self.visible.values()

    def scenic_score(self) -> int:
        val: list[int] = self.can_see.values()
        clean: list[int] = filter(lambda x: x is not None, val)
        return math.prod(clean)


forest: list[list[Tree]] = [[Tree(int(x)) for x in string] for string in lines]
directions: list[str] = ["up", "right", "down", "left"]


# left check_visible
for row in forest:
    max_height: int = -1
    for tree in row:
        max_height = tree.check_visible("left", max_height)

# right check_visible
for row in forest:
    max_height: int = -1
    for tree in reversed(row):
        max_height = tree.check_visible("right", max_height)

# up check_visible
rows: int = len(forest)
columns: int = len(forest[0])

for column in range(columns):
    max_height = -1
    for row in range(rows):
        tree: Tree = forest[row][column]
        max_height = tree.check_visible("up", max_height)

# down check_visible

for column in range(columns):
    max_height = -1
    for row in reversed(range(rows)):
        tree: Tree = forest[row][column]
        max_height = tree.check_visible("down", max_height)


visible_trees: int = 0
invisible_trees: int = 0
invalid: int = 0
for row in forest:
    for tree in row:
        if tree.is_visible():
            visible_trees += 1
        else:
            invisible_trees += 1
        if tree.is_invalid():
            invalid += 1
    #     print(tree.is_visible(), end=" ")
    # print("")

print(visible_trees, invisible_trees, visible_trees + invisible_trees, invalid)

max_score = 0

for x, row in enumerate(forest):
    for y, tree in enumerate(row):
        right: int = 0
        left: int = 0
        up: int = 0
        down: int = 0

        # check right
        for i in range(y, columns):
            if y != i:
                right += 1
            if tree.height <= forest[x][i].height and y != i:
                break
        # check left
        for i in reversed(range(y)):
            if y != i:
                left += 1
            if tree.height <= forest[x][i].height and y != i:
                break
        # check up
        for i in reversed(range(x)):
            if x != i:
                up += 1
            if tree.height <= forest[i][y].height and x != i:
                break
        # check down
        for i in range(x, rows):
            if x != i:
                down += 1
            if tree.height <= forest[i][y].height and x != i:
                break
        tree.can_see = {
            "left": left,
            "right": right,
            "up": up,
            "down": down,
        }
        # print(tree.height, x + 1, y + 1, tree.can_see, tree.scenic_score())
        max_score: int = max(max_score, tree.scenic_score())
print(max_score)
