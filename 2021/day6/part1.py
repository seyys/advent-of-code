with open('test.txt') as f:
    pop = [x.split(",") for x in f.readlines()]
    pop = [int(x) for x in pop[0]]

for day in range(80):
    # print("Day ", day, ": ", pop)
    pop = [x-1 for x in pop]
    for i in range(len(pop)):
        if pop[i] < 0:
            pop[i] = 6
            pop.append(8)

print(len(pop))