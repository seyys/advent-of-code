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

loc = np.array([-2, 0])

digit = [[0, 2], [-1, 1], [0, 1], [1, 1], [-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0], [-1, -1], [0, -1], [1, -1], [0, -2]]

for row in d:
    for move in row:
        new_loc = loc + instruction[move]
        if sum(abs(new_loc)) >= 3:
            continue
        loc = new_loc
    code.append(format(digit.index(loc.tolist()) + 1, 'x'))

print("".join(str(x) for x in code))