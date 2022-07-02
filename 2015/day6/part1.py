import numpy as np
import re

with open('input.txt') as f:
    dd = f.readlines()
    dd = [x.strip() for x in dd]
    d = []
    for row in dd:
        foo = []
        foo.append(re.findall(r"[a-zA-Z\ ]*(?=\d+,\d+ through)",row)[0].strip())
        coords = [x.split(',') for x in re.findall(r"\d+,\d+",row)]
        foo.append(min([int(coords[0][0]),int(coords[1][0])])) # x min
        foo.append(max([int(coords[0][0]),int(coords[1][0])])) # x max
        foo.append(min([int(coords[0][1]),int(coords[1][1])])) # y min
        foo.append(max([int(coords[0][1]),int(coords[1][1])])) # y max
        d.append(foo)

grid = np.zeros((1000,1000), dtype=bool)

for row in d:
    x_min, x_max, y_min, y_max = row[1:]
    if row[0] == "turn on":
        grid[y_min:y_max+1,x_min:x_max+1] = True
    elif row[0] == "turn off":
        grid[y_min:y_max+1,x_min:x_max+1] = False
    elif row[0] == "toggle":
        grid[y_min:y_max+1,x_min:x_max+1] = ~grid[y_min:y_max+1,x_min:x_max+1]

print(len(np.where(grid)[0]))