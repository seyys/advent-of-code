import numpy as np


with open("input.txt") as f:
    d = f.readlines()
d = [x.strip() for x in d]

code = []

instruction = dict()
instruction["U"] = np.array([0, 1])
instruction["R"] = np.array([1, 0])
instruction["D"] = np.array([0, -1])
instruction["L"] = np.array([-1, 0])

loc = np.array([1, 1])

for row in d:
    for move in row:
        loc += instruction[move]
        loc = np.minimum(loc, np.array([2, 2]))
        loc = np.maximum(loc, np.array([0, 0]))
    code.append((2 - loc[1]) * 3 + loc[0] + 1)

print("".join(str(x) for x in code))