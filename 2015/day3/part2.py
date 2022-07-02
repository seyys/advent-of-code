import numpy as np
from collections import Counter

with open('input.txt') as f:
    d = f.readlines()
    d = d[0].strip()

coords = np.array([0,0])
coords_robo = np.array([0,0])
visited = Counter({tuple(coords),tuple(coords_robo)})
robo_turn = False

for c in d:
    if c == '^':
        direction = np.array([-1,0])
    elif c == '>':
        direction = np.array([0,1])
    elif c == 'v':
        direction = np.array([1,0])
    elif c == '<':
        direction = np.array([0,-1])
    if robo_turn:
        coords_robo += direction
        visited.update({tuple(coords_robo)})
    else:
        coords += direction
        visited.update({tuple(coords)})
    robo_turn = not robo_turn
    
print(len(visited.values()))