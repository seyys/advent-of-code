with open('1.input') as f:
    d = f.readlines()

n = 0
for i in range(1,len(d)):
    if int(d[i]) > int(d[i-1]):
        n += 1

print(n)