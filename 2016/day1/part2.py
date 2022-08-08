import numpy as np


with open("input.txt") as f:
    d = f.readline().strip()
d = d.split(', ')
d = [[x[0], int(x[1:])] for x in d]

rot = dict()
rot["R"] = np.array([[0, 1], [-1, 0]])
rot["L"] = np.array([[0, -1], [1, 0]])

position = [np.array([[0], [0]])]
direction = np.array([[0], [1]])
found = False

for direc, blocks in d:
    direction = np.matmul(rot[direc], direction)
    for __ in range(blocks):
        pos = direction + position[-1]
        if any([all(x == pos) for x in position]):
            print(sum(abs(x) for x in pos))
            found = True
            break
        position.append(pos)
    if found:
        break