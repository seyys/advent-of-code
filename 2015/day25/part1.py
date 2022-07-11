import re

def calc(code):
    return (code * 252533) % 33554393

with open('input.txt') as f:
    d = f.readlines()
    d = [x.strip() for x in d]

b, a = [int(x) for x in re.findall(r"\d+", d[0])]
code = 20151125

# a is col, b is row
target = int(a*(a-1)/2 + (a+b-2)*(a+b-1)/2 - (a-1)*(a-2)/2)

for i in range(target):
    code = calc(code)

print(code)