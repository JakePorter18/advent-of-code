import itertools

with open("2021//2021-day4.txt", "r", encoding="utf8") as f:
    lines = [line.rstrip("\n") for line in f]


drawn: list[int] = [int(x) for x in lines.pop(0).split(",")]


class Bingo:
    def __init__(self, n: list[list[int]]):
        self.n: list[list[int]] = n
        self.correct: list[list[bool]] = [[False for _ in range(5)] for _ in range(5)]

    def draw(self, num: int) -> bool:
        for i, j in itertools.product(range(5), range(5)):
            if self.n[i][j] == num:
                self.correct[i][j] = True
        return self.check()

    def check(self) -> bool:
        rows: bool = any(all(row) for row in self.correct)
        cols_list = []
        for i in range(5):
            col = [self.correct[j][i] for j in range(5)]
            cols_list.append(col)
        cols: bool = any(all(col) for col in cols_list)
        return rows or cols


def convert_to_input(chunk):
    chunk = filter(lambda x: x != "", chunk)
    return [[int(x) for x in line.split()] for line in chunk]


def main():
    chunks: list[list[str]] = [lines[x : x + 6] for x in range(0, len(lines), 6)]
    games: list[Bingo] = [Bingo(convert_to_input(chunk)) for chunk in chunks]

    for x in drawn:
        last: int = x
        round_res: list[bool] = [game.draw(x) for game in games]
        if any(round_res):
            break

    win_no: int = round_res.index(True)
    winning_game: Bingo = games[win_no]

    total_incorrect: int = 0
    for i, row in enumerate(winning_game.n):
        for j, val in enumerate(row):
            if not winning_game.correct[i][j]:
                total_incorrect += val

    print(win_no, total_incorrect, last, last * total_incorrect)


def win_last():
    chunks: list[list[str]] = [lines[x : x + 6] for x in range(0, len(lines), 6)]
    games: list[Bingo] = [Bingo(convert_to_input(chunk)) for chunk in chunks]

    for x in drawn:
        last: int = x
        round_res: list[bool] = [game.draw(x) for game in games]
        if all(round_res):
            break
        if any(round_res):
            games = [game for (game, remove) in zip(games, round_res) if not remove]

    winning_game: Bingo = games[0]

    total_incorrect: int = 0
    for i, row in enumerate(winning_game.n):
        for j, val in enumerate(row):
            if not winning_game.correct[i][j]:
                total_incorrect += val

    print(total_incorrect, last, last * total_incorrect)


win_last()
