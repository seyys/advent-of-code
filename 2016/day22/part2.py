import re


class node:
    def __init__(self, s):
        self.x = int(re.search(r"(?<=x)\d+", s).group(0))
        self.y = int(re.search(r"(?<=y)\d+", s).group(0))
        __, self.size, self.used, self.avail, self.use_perc = [int(re.search(r"\d+", x).group(0)) for x in filter(None, re.split(r"\s+", s))]
    
    def is_empty(self):
        return self.used == 0

def visualise_grid(n):
    for y in range(max(n[0]) + 1):
        r = ''
        for x in range(max(n) + 1):
            if n[x][y].used == 0:
                r += 'x'
            elif n[x][y].used > 400:
                r += '-'
            else:
                r += '.'
        print(r)

with open("input.txt") as f:
    d = f.readlines()
d = d[2:]

ns = [node(x) for x in d]
ns_keys_x = [a.x for a in ns]
ns_keys_y = [a.y for a in ns]

nodes = dict()

for x in range(max(ns_keys_x) + 1):
    nodes[x] = {k:v for (k,v) in zip(ns_keys_y, ns) if v.x == x}

visualise_grid(nodes)