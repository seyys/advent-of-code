from collections import Counter

with open('input.txt') as f:
    d = f.readlines()
    d = [list(x.strip()) for x in d]
    d = Counter(d[0])

print(d['('] - d[')'])