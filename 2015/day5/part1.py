from collections import Counter
import re

with open('input.txt') as f:
    d = f.readlines()
    d = [x.strip() for x in d]

count_nice = 0

for s in d:
    if "ab" in s or "cd" in s or "pq" in s or "xy" in s:
        continue
    if sum([s.count('a'),s.count('e'),s.count('i'),s.count('o'),s.count('u')]) < 3:
        continue
    if len(re.findall(r"(\w)\1", s)) == 0:
        continue
    count_nice += 1

print(count_nice)