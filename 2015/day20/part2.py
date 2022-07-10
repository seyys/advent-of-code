d = 29000000
i = 665280

while(True):
    if sum(x * 11 for x in range(1,i+1) if x * 50 >= i and i % x == 0) >= d:
        break
    i += 2

print(i)