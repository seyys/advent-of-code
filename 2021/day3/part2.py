with open('input.txt') as f:
    d = f.readlines()

for i in range(len(d)):
    d[i] = int(d[i],2)

o2 = d[:]

for i in range(11, -1, -1):
    if len(o2) == 1:
        break
    # Find most common bit
    foo = []
    mcb = -1
    foo = [0 for i in range(len(o2))]
    for j in range(len(o2)):
        foo[j] = (o2[j] & (1 << i)) >> i
    # if there are more 1s than 0s, mcb is 1
    if foo.count(1) >= foo.count(0):
        mcb = 1
    else:
        mcb = 0
    for j in range(len(o2)-1,-1,-1):
        if foo[j] != mcb:
            o2.remove(o2[j])

co2 = d[:]
for i in range(11, -1, -1):
    if len(co2) == 1:
        break
    # Find most common bit
    foo = []
    lcb = -1
    foo = [0 for i in range(len(co2))]
    for j in range(len(co2)):
        foo[j] = (co2[j] & (1 << i)) >> i
    # if there are more 1s than 0s, mcb is 1
    if (foo.count(1) == len(foo)) | (foo.count(0) == len(foo)):
        continue
    if foo.count(1) < foo.count(0):
        lcb = 1
    else:
        lcb = 0
    for j in range(len(co2)-1,-1,-1):
        if foo[j] != lcb:
            co2.remove(co2[j])

print(o2[0] * co2[0])