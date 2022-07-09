import re

with open('input.txt') as f:
    d = f.readlines()
    d = [x.strip() for x in d]

with open('real_sue.txt') as f:
    dd = f.readlines()
    dd = [x.strip() for x in dd]

sues = []
for row in d:
    row = re.split(r", |: ", row)
    prop = row[1:6:2]
    val = [int(x) for x in row[2:7:2]]
    sues.append(dict(zip(prop,val)))

real_sue = {}
for row in dd:
    real_sue[re.search(r"^\w*(?=:)", row).group(0)] = int(re.search(r"(?<=: )\d*", row).group(0))

for i, row in enumerate(sues):
    is_real_sue = True
    for prop, val in row.items():
        if real_sue[prop] != val:
            is_real_sue = False
            break
    if is_real_sue:
        break

print(i + 1)