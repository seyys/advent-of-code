import numpy as np
from collections import Counter

with open('input.txt') as f:
    d = f.readlines()
    d = d[0].strip()

coords = np.array([0,0])
visited = Counter({tuple(coords)})

for c in d:
    if c == '^':
        direction = np.array([-1,0])
    elif c == '>':
        direction = np.array([0,1])
    elif c == 'v':
        direction = np.array([1,0])
    elif c == '<':
        direction = np.array([0,-1])
    coords += direction
    visited.update({tuple(coords)})

print(len(visited.values()))