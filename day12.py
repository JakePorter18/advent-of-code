with open("day12.txt", "r", encoding="utf8") as f:
    lines: list[str] = [line.rstrip("\n") for line in f]

height = list("abcdefghijklmnopqrstuvwxyz")

s_row, s_column, e_row, e_column = [0, 0, 0, 0]

for i, row in enumerate(lines):
    if "S" in row:
        s_row = i
        s_column = row.index("S")
    if "E" in row:
        e_row = i
        e_column = row.index("E")

# print((s_row, s_column), (e_row, e_column))


def get_height(char, heights):
    if char == "S":
        return 0
    elif char == "E":
        return 25
    else:
        return heights.index(char)


height_map = [[get_height(char, height) for char in row] for row in lines]


def get_near_height(heights, x: int, y: int) -> int:
    try:
        return 999 if x < 0 or y < 0 else heights[x][y]
    except IndexError:
        return 999


graph = {}
edges = []
for i, row in enumerate(height_map):
    for j, height in enumerate(row):
        moves = []
        can_left: bool = get_near_height(height_map, i, j - 1) <= height + 1
        can_right: bool = get_near_height(height_map, i, j + 1) <= height + 1
        can_down: bool = get_near_height(height_map, i + 1, j) <= height + 1
        can_up: bool = get_near_height(height_map, i - 1, j) <= height + 1
        if can_left:
            moves.append((i, j - 1))
            edges.append(((i, j), (i, j - 1), 1))
        if can_right:
            moves.append((i, j + 1))
            edges.append(((i, j), (i, j + 1), 1))
        if can_down:
            moves.append((i + 1, j))
            edges.append(((i, j), (i + 1, j), 1))
        if can_up:
            moves.append((i - 1, j))
            edges.append(((i, j), (i - 1, j), 1))
        graph[(i, j)] = moves

# print(graph)
# print(edges)


class Graph:
    def __init__(self, g):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = g
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        # self.edges[from_node].append(to_node)
        # self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight


g = Graph(graph)
for edge in edges:
    g.add_edge(*edge)


def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {
            node: shortest_paths[node] for node in shortest_paths if node not in visited
        }
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path


lengths = []
for i, row in enumerate(height_map):
    for j, height in enumerate(row):
        if height == 0:
            s_path = dijsktra(g, (i, j), (e_row, e_column))
            if s_path != "Route Not Possible":
                lengths.append(len(s_path) - 1)


lengths.sort()
print(lengths)
print(min(lengths))
