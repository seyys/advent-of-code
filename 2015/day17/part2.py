import itertools

with open('input.txt') as f:
    d = f.readlines()
    d = [int(x.strip()) for x in d]

num_combos = 0
possible = False

for i in range(len(d) + 1):
    for combinations in itertools.combinations(d, i):
        if sum(combinations) == 150:
            possible = True
            num_combos += 1
    if possible:
        break

print(num_combos)