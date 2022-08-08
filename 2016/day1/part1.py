import numpy as np


with open("input.txt") as f:
    d = f.readline().strip()
    d = d.split(', ')
    d = [[x[0], int(x[1:])] for x in d]

rot = dict()
rot["R"] = np.array([[0, 1], [-1, 0]])
rot["L"] = np.array([[0, -1], [1, 0]])

position = np.array([[0], [0]])
direction = np.array([[0], [1]])

for direc, blocks in d:
    direction = np.matmul(rot[direc], direction)
    position += direction * blocks

print(sum(abs(x) for x in position))