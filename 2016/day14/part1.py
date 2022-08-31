import hashlib
import re
import numpy as np


class key:
    def __init__(self, char, idx):
        self.char = char
        self.idx = idx

salt = b"cuanljph"
# salt = b"abc"
idx = 0

valid_key = []
potential_key = []
key_found = False
countdown = np.inf
countdown_set = False

while countdown > 0:
    h = hashlib.md5(salt + bytes(str(idx), "utf-8")).hexdigest()
    potential = re.search(r"(.)(?=\1\1)", h)
    for k in potential_key[:]: # Can't remove item from list while iterating through it - need to iterate through a copy
        if idx > 1000 + k.idx:
            potential_key.remove(k)
        elif (k.char * 5) in h:
            valid_key.append(k)
            potential_key.remove(k)
            if not countdown_set and len(valid_key) >= 64:
                countdown = 1001
                countdown_set = True
    if potential:
        potential_key.append(key(potential.group(0), idx))
    idx += 1
    countdown -= 1

valid_key.sort(key=lambda x: x.idx)
print(valid_key[63].idx)