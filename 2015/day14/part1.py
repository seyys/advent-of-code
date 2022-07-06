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
    reindeer[name] = [speed, t_speed, t_rest]

for r in reindeer:
    speed, t_speed, t_rest = reindeer[r]
    full_rounds = np.floor_divide(t_contest, (t_rest + t_speed))
    ticks = full_rounds * t_speed
    ticks += min(t_contest % (t_rest + t_speed) , t_speed)
    dist = ticks * speed
    max_dist = max(dist, max_dist)

print(max_dist)