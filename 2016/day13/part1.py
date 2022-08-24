import numpy as np


class node:
    def __init__(self, coords, path_length, goal, parent):
        self.coords = coords
        self.g = path_length
        self.h = int(sum([abs(np.diff(x)) for x in zip(coords, goal)]))
        self.f = self.g + self.h
        self.parent = parent

def check_empty(seed, x, y):
    if x < 0 or y < 0:
        return False
    return str(bin(x*x + 3*x + 2*x*y + y + y*y + seed)).count('1') % 2 == 0

seed = 1362
target = (31,39)
start = (1,1)

list_open = [node(start, 0, target, None)]
list_closed = []

while list_open:
    list_open.sort(key=lambda x: x.f, reverse=True)
    q = list_open.pop()
    for direction in [(0,1), (0,-1), (1,0), (-1,0)]:
        successor_coord = tuple([sum(x) for x in zip(q.coords, direction)])
        if not check_empty(seed, *successor_coord):
            continue
        if successor_coord == target:
            length = q.g + 1
            list_open = []
            break
        proposed_node = node(successor_coord, q.g + 1, target, q)

        check_f = [x for x in list_open if x.coords == proposed_node.coords]
        lowest_f = True
        for n in check_f:
            if n.f < proposed_node.f:
                lowest_f = False
                break
        if not lowest_f:
            continue

        check_f = [x for x in list_closed if x.coords == proposed_node.coords]
        lowest_f = True
        for n in check_f:
            if n.f < proposed_node.f:
                lowest_f = False
                break
        if not lowest_f:
            continue
        list_open.append(proposed_node)
        
    list_closed.append(q)

print(length)