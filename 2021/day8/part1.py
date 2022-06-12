with open('input.txt') as f:
    d = f.readlines()
    dd = []
    for row in d:
        foo = row.split(" | ")
        foo = [x.split() for x in foo]
        dd.append(foo)

count = 0
for i in range(len(dd)):
    for item in dd[i][1]:
        if len(item) == 2 or len(item) == 3 or len(item) == 4 or len(item) == 7:
            count += 1

print(count)