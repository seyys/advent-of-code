import itertools
import numpy as np

with open('input.txt') as f:
    d = f.readlines()
    d = set([int(x.strip()) for x in d])

target_weight = int(sum(d)/3)
optimal_arrangement = []

for i in range(len(d)):
    for arrangement in itertools.combinations(d, i):
        if sum(arrangement) == target_weight:
            legal_arrangement = False
            remainder = d - set(arrangement)
            for j in range(len(remainder)):
                for arr in itertools.combinations(remainder, j):
                    if sum(arr) == target_weight:
                        legal_arrangement = True
                        break
                if legal_arrangement:
                    break
            if not legal_arrangement:
                continue
            if optimal_arrangement == []:
                optimal_arrangement = arrangement
            if len(arrangement) < len(optimal_arrangement):
                optimal_arrangement = arrangement
            elif len(arrangement) == len(optimal_arrangement) and np.product(arrangement) < np.product(optimal_arrangement):
                optimal_arrangement = arrangement
    if optimal_arrangement:
        break

print(optimal_arrangement)
print(np.product(optimal_arrangement))