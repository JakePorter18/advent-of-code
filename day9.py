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
    def __init__(self):
        self.x = 0
        self.y = 0
        self.t_x = 0
        self.t_y = 0
        self.t_visit = [(0, 0)]

    def move_head(self, move):
        x, y = move
        self.x += x
        self.y += y
        self.move_tail()

    def distance(self):
        x_d = self.x - self.t_x
        y_d = self.y - self.t_y
        return x_d**2 + y_d**2

    def move_tail(self):
        self.t_visit.append((self.t_x, self.t_y))
        if self.distance() <= 2:
            return (0, 0)

        x_d = self.x - self.t_x
        y_d = self.y - self.t_y

        if x_d != 0 and y_d != 0:
            self.t_x += sign(x_d)
            self.t_y += sign(y_d)
            return
        if abs(x_d) != 0 and y_d == 0:
            self.t_x += sign(x_d)
            return
        if abs(y_d) != 0 and x_d == 0:
            self.t_y += sign(y_d)
            return
        raise ValueError


head = Head()
for move in moves:
    head.move_head(move)
    # print(head.t_x, head.t_y, head.x, head.y)

visited = set(head.t_visit)
print(len(visited))
