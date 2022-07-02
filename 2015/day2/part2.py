import numpy as np

with open('input.txt') as f:
    d = f.readlines()
    d = [x.strip().split('x') for x in d]
    d = [[int(x) for x in y] for y in d]

total = 0

for row in d:
    box = (sum(row) - max(row)) * 2
    total += box + np.prod(row)

print(int(total))