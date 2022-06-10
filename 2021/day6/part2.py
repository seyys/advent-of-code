from collections import Counter

with open('input.txt') as f:
    d = [x.split(",") for x in f.readlines()]
    d = [int(x) for x in d[0]]

# pop[0] is -1 days
pop = [0 for x in range(10)]
for p in d:
    pop[p] += 1

for day in range(256):
    # print("Day ", day, ": ", pop)
    pop[7] += pop[0]
    pop[9] += pop[0]
    pop[0] = 0
    # Shift list one to the left
    pop.append(pop.pop(0))

print(sum(pop))