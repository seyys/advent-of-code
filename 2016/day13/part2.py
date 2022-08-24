import numpy as np


class node:
    def __init__(self, coords, path_length):
        self.coords = coords
        self.g = path_length

def check_empty(seed, x, y):
    if x < 0 or y < 0:
        return False
    return str(bin(x*x + 3*x + 2*x*y + y + y*y + seed)).count('1') % 2 == 0

seed = 1362
start = (1,1)

list_open = [node(start, 0)]
list_closed = []

while list_open:
    q = list_open.pop()
    if q.g > 50:
        continue
    for direction in [(0,1), (0,-1), (1,0), (-1,0)]:
        successor_coord = tuple([sum(x) for x in zip(q.coords, direction)])
        if not check_empty(seed, *successor_coord):
            continue
        proposed_node = node(successor_coord, q.g + 1)
        if [x for x in list_open if x.coords == proposed_node.coords]:
            continue
        if [x for x in list_closed if x.coords == proposed_node.coords]:
            continue
        list_open.append(proposed_node)
        
    list_closed.append(q)

print(len(list_closed))