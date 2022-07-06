import itertools
import re
import numpy as np

with open('input.txt') as f:
    d = f.readlines()
    d = [x.strip() for x in d]

happiness = {}
names = []
max_points = -np.inf

for row in d:
    person = re.search(r"^\w*", row).group(0)
    partner = re.search(r"\w*(?=\.)", row).group(0)
    points = int(re.search(r"\d*(?= happiness)", row).group(0))
    points_direction = -1 if "lose" in row else 1
    points *= points_direction
    if person not in names:
        names.append(person)
        happiness[person] = {}
    happiness[person][partner] = points

# Part 2
names.append("me")
happiness["me"] = {}
for n in names:
    happiness["me"][n] = 0
    happiness[n]["me"] = 0

for arrangement in itertools.permutations(names):
    points = 0
    for i in range(len(arrangement)):
        points += happiness[arrangement[i]][arrangement[i-1]]
        points += happiness[arrangement[i-1]][arrangement[i]]
    max_points = max(max_points, points)

print(max_points)