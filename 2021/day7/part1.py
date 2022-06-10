with open('input.txt') as f:
    d = [x.split(",") for x in f.readlines()]
    d = [int(x) for x in d[0]]

fuel = [0 for x in range(max(d))]
for i in range(max(d)):
    fuel[i] = sum([abs(x-i) for x in d])

print(min(fuel))