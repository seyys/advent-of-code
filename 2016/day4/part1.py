from collections import Counter
import re


def calculate_checksum(name):
    r = list(Counter(name).most_common())
    r = sorted(r, key=lambda x: (-x[1], x[0]))
    r = ''.join([x[0] for i, x in enumerate(r) if i < 5])
    return r

with open("input.txt") as f:
    d = f.readlines()
d = [x.strip() for x in d]
d = [x.replace('-','') for x in d]
d = [[re.search(r"[a-z]+", x).group(0), int(re.search(r"\d+", x).group(0)), re.search(r"(?<=\[)[a-z]+(?=\])", x).group(0)] for x in d]

sum_sector_id = 0

for name, sector_id, checksum in d:
    if calculate_checksum(name) == checksum:
        sum_sector_id += sector_id

print(sum_sector_id)