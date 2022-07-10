import re

with open('input.txt') as f:
    d = []
    foo = f.readline()
    while(foo != "\n"):
        d.append(foo)
        foo = f.readline()
    d = [x.strip() for x in d]
    d = [x.split(" => ") for x in d]
    seed = f.readline()

molecules = set()

for row in d:
    for match in re.finditer(row[0], seed):
        split_start, split_end = match.span()
        molecules.add(seed[:split_start] + row[1] + seed[split_end:])

print(len(molecules))