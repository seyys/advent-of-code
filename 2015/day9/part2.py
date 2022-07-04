import itertools
import re

with open('input.txt') as f:
    d = f.readlines()
    d = [x.strip() for x in d]
    d = [re.split(r" to | = ",x) for x in d]

dist = dict()
cities = []
longest_path_len = 0

for row in d:
    if row[0] not in cities:
        cities.append(row[0])
        dist[row[0]] = dict()
    if row[1] not in cities:
        cities.append(row[1])
        dist[row[1]] = dict()
    dist[row[0]][row[1]] = int(row[2])
    dist[row[1]][row[0]] = int(row[2])

for path in itertools.permutations(cities):
    path_len = 0
    for i in range(len(path) - 1):
        path_len += dist[path[i]][path[i+1]]
    longest_path_len = max(longest_path_len, path_len)

print(longest_path_len)