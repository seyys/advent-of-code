import re

with open('input.txt') as f:
    d = f.readlines()
    d = [x.strip() for x in d]

mem_lit = 0
mem_str = 0

for row in d:
    mem_l = len(row)

    row = row[1:-1]

    mem_s = mem_l + 4
    mem_s += len(re.findall(r"\\\\", row)) * 2
    mem_s += len(re.findall(r"\\\"", row)) * 2
    mem_s += len(re.findall(r"\\x[0-9a-f]{2}", row))

    mem_lit += mem_l
    mem_str += mem_s

print(mem_str - mem_lit)