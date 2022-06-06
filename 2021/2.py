with open('2.input') as f:
    d = f.readlines()

# Convert list of str to int
d = list(map(int,d))

#d = [199,200,208,210,200,207,240,269,260,263]

dd = []
for i in range(2,len(d)):
    dd.append(sum(d[i-2:i+1]))

n = 0
for i in range(1,len(dd)):
    if dd[i] > dd[i-1]:
        n += 1

print(n)