from collections import Counter
import re

with open('input.txt') as f:
    d = f.readlines()
    d = [x.strip() for x in d]

count_nice = 0

for s in d:
    if len(re.findall(r"(\w{2})\w*\1", s)) == 0:
        continue
    if len(re.findall(r"(\w)\w\1", s)) == 0:
        continue
    count_nice += 1

print(count_nice)