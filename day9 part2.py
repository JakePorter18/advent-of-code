with open("day9.txt", "r") as f:
    text = f.read()

lines = text.split("\n")


def sign(x):
    try:
        return x // abs(x)
    except ZeroDivisionError:
        return 0


moves = []
for line in lines:
    dir, r = line.split(" ")
    r = int(r)
    if dir == "L" or dir == "D":
        r = r * -1
    if dir == "R" or dir == "L":
        x = sign(r)
        y = 0
    elif dir == "U" or dir == "D":
        x = 0
        y = sign(r)
    move = (x, y)
    for i in range(abs(r)):
        moves.append(move)


class Head:
    def __init__(self, tail):
        self.x = 0
        self.y = 0
        self.visit = [(0,0)]
        self.tail = tail
    def move_head(self, move):
        x, y = move
        self.x += x
        self.y += y
        self.visit.append((self.x, self.y))
        if self.tail is not None:
            self.move_tail()

    def distance(self):
        x_d = self.x - self.tail.x
        y_d = self.y - self.tail.y
        return x_d**2 + y_d**2

    def move_tail(self):
        self.visit.append((self.x, self.y))
        if self.tail is None:
            return
        if self.distance() <= 2:
            return

        y_d = self.y - self.tail.y
        x_d = self.x - self.tail.x

        if x_d != 0 and y_d != 0:
            self.tail.x += sign(x_d)
            self.tail.y += sign(y_d)
            
        if abs(x_d) != 0 and y_d == 0:
            self.tail.x += sign(x_d)
            
        if abs(y_d) != 0 and x_d == 0:
            self.tail.y += sign(y_d)
            
        self.tail.move_tail()

def main(length, moves):
    tail = None
    for i in range(length):
        tail = Head(tail)

    for move in moves:
        tail.move_head(move)

    visited = {}
    for x in range(length):
        if tail is not None:
            visited[x] = len(set(tail.visit))
            tail = tail.tail
    print(visited)

if __name__ == "__main__":
    main(10, moves)