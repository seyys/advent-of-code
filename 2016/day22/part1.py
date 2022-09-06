import re


class node:
    def __init__(self, s):
        self.x = int(re.search(r"(?<=x)\d+", s).group(0))
        self.y = int(re.search(r"(?<=y)\d+", s).group(0))
        __, self.size, self.used, self.avail, self.use_perc = [int(re.search(r"\d+", x).group(0)) for x in filter(None, re.split(r"\s+", s))]
    
    def is_empty(self):
        return self.used == 0

with open("input.txt") as f:
    d = f.readlines()
d = d[2:]

nodes = [node(x) for x in d]
num_viable_pairs = 0

for n in nodes:
    ns = nodes[:]
    ns.remove(n)
    num_viable_pairs += len([1 for x in ns if n.used <= x.avail and not n.is_empty()])

print(num_viable_pairs)