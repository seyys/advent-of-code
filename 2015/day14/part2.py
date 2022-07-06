import re
import numpy as np

with open('input.txt') as f:
    d = f.readlines()
    d = [x.strip() for x in d]

# d = ["Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.","Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."]

reindeer = {}
t_contest = 2503
max_dist = 0

for row in d:
    name = re.search(r"^\w*", row).group(0)
    speed = int(re.search(r"\d*(?= km/s)", row).group(0))
    t_speed = int(re.search(r"(?<=km/s for )\d*", row).group(0))
    t_rest = int(re.search(r"(?<= rest for )\d*", row).group(0))
    reindeer[name] = [speed, t_speed, t_rest, 0, 0]

for t in range(t_contest):
    max_dist = 0
    for r in reindeer:
        if (t % (reindeer[r][1] + reindeer[r][2])) < reindeer[r][1]:
            reindeer[r][3] += reindeer[r][0]
    for r in reindeer:
        max_dist = max(max_dist, reindeer[r][3])
    for r in reindeer:
        if reindeer[r][3] == max_dist:
            reindeer[r][4] += 1

max_points = 0
for r in reindeer:
    max_points = max(max_points, reindeer[r][4])

print(max_points)