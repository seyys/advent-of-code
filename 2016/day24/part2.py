import numpy as np
import json
import itertools


class node:
    def __init__(self, coords, path_len, goal, parent):
        self.coords = coords
        self.g = path_len
        self.h = sum(np.abs(np.diff(x)[0]) for x in zip(goal, coords)) * 1.001
        self.f = self.g + self.h
        self.parent = parent

def a_star(grid, a, b):
    start = tuple(x[0] for x in np.where(grid == str(a)))
    goal = tuple(x[0] for x in np.where(grid == str(b)))
    open_list = [node(start, 0, goal, None)]
    closed_list = []
    while len(open_list) > 0:
        q = open_list.pop(open_list.index(min(open_list, key=lambda x: x.f)))
        potential_successors = [node(tuple(sum(y) for y in zip(q.coords, x)), q.g + 1, goal, q) for x in [(-1,0),(1,0),(0,-1),(0,1)]]
        for n in potential_successors:
            if grid[n.coords] == '#':
                continue
            if q.parent is not None and n.coords == q.parent.coords:
                continue

            if n.coords == goal:
                return n.g

            node_in_open_list = [x for x in open_list if x.coords == n.coords]
            if node_in_open_list:
                if node_in_open_list[0].f <= n.f:
                    continue
            
            node_in_closed_list = [x for x in closed_list if x.coords == n.coords]
            if node_in_closed_list:
                if node_in_closed_list[0].f <= n.f:
                    continue
            
            open_list.append(n)
        closed_list.append(q)

with open("input.txt") as f:
    d = f.readlines()
d = [x.strip() for x in d]
grid = np.array([[x if (x == '#' or x == '.') else int(x) for x in row] for row in d])
num_poi = max([int(y) for y in [x for x in [item for sublist in d for item in sublist] if x in "0123456789"]])

# Find distance between nodes
# graph = dict()
# for x in range(num_poi + 1):
#     graph[x] = dict()

# for a in range(num_poi, -1, -1):
#     for b in range(num_poi, a - 1, -1):
#         if a == b:
#             graph[a][b] = 0
#             graph[b][a] = 0
#             continue
#         graph[a][b] = a_star(grid, a, b)
#         graph[b][a] = a_star(grid, a, b)
# 
# with open("graph.txt", 'w') as f:
#     f.write(json.dumps(graph))

with open("graph.txt") as f:
    graph = json.loads(f.readline())

# Travelling salesman
min_path_len = np.inf

for path in itertools.permutations(range(1, num_poi + 1)):
    path = (0,) + path + (0,)
    path_len = 0
    for step in range(len(path) - 1):
        path_len += graph[str(path[step])][str(path[step+1])]
    if path_len < min_path_len:
        min_path_len = path_len

print(min_path_len)