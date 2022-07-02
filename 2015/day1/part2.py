from collections import Counter

with open('input.txt') as f:
    d = f.readlines()
    d = [list(x.strip()) for x in d]
    d = d[0]

floor = 0
i = 0
for c in d:
    if c == '(':
        floor += 1
    else:
        floor -= 1
    i += 1
    if floor == -1:
        break
print(i)