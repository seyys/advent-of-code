with open('input.txt') as f:
    d = f.readlines()

zeros = [0 for i in range(12)]
ones = [0 for i in range(12)]
gamma = [0 for i in range(12)]
episilon = [0 for i in range(12)]
for l in d:
    for i in range(12):
        if l[i] == "0":
            zeros[i] += 1
        else:
            ones[i] += 1

for i in range(12):
    if zeros[i] > ones[i]:
        gamma[i] = 0
        episilon[i] = 1
    else:
        gamma[i] = 1
        episilon[i] = 0

gamma = int("".join(map(str,gamma)),2)
episilon = int("".join(map(str,episilon)),2)

print(gamma*episilon)