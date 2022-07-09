import itertools

with open('input.txt') as f:
    d = f.readlines()
    d = [int(x.strip()) for x in d]

num_combos = 0

for i in range(len(d) + 1):
    for combinations in itertools.combinations(d, i):
        if sum(combinations) == 150:
            num_combos += 1

print(num_combos)