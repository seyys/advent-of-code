import re

with open('input.txt') as f:
    d = f.readlines()

nums = [int(x) for x in re.findall(r"\-?\d+", str(d))]

print(sum(nums))