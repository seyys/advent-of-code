import math
import numpy as np


def calc(d):
    d = list(range(1, d + 1))
    idx = 0

    while len(d) > 1:
        pop_idx = idx - int(np.ceil(len(d)/2))
        if pop_idx < 0:
            pop_idx += len(d)
        d.pop(pop_idx)
        if idx < pop_idx:
            idx += 1
        if idx >= len(d):
            idx = 0
    return d[0]

# for d in range(1,1000):
#     print(d, calc(d))

d = 3001330
# d = 488
lower_pow3 = int(np.floor(math.log(d, 3)))
higher_pow3 = int(np.ceil(math.log(d, 3)))
distance_from_lower_pow3 = d - 3**lower_pow3
distance_between_pow3 = 3**higher_pow3 - 3**lower_pow3
cutoff_between_pow3 = distance_between_pow3 / 2
if distance_from_lower_pow3 >= cutoff_between_pow3:
    distance_from_lower_pow3 = int(distance_from_lower_pow3 + (distance_from_lower_pow3 - cutoff_between_pow3))

print(distance_from_lower_pow3)