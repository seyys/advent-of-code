import itertools

with open('input.txt') as f:
    d = f.readlines()
    d = [x.strip().split('x') for x in d]
    d = [[int(x) for x in y] for y in d]

total = 0

for row in d:
    box = []
    for a in itertools.combinations(row,2):
        box.append(a[0] * a[1] * 2)
    total += sum(box) + min(box)/2

print(int(total))