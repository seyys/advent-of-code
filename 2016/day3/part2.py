import re
import numpy as np


with open("input.txt") as f:
    d = f.readlines()
d = [x.strip() for x in d]
d = [re.findall(r"\d+", x) for x in d]
d = [[int(x) for x in y] for y in d]

d = np.array(d)
d = d.T.reshape(np.floor_divide(d.size, 3), 3).tolist()

valid_triangles = 0

for triangle in d:
    triangle.sort(reverse=True)
    if triangle[0] >= triangle[1] + triangle[2]:
        continue
    valid_triangles += 1

print(valid_triangles)