def cpy(x,y):
    if isinstance(x, str):
        register[y] = register[x]
    elif isinstance(x, int):
        register[y] = x

def inc(x):
    register[x] += 1

def dec(x):
    register[x] -= 1

def jnz(x,y):
    global idx
    if (isinstance(x, int) and x == 0) or (not isinstance(x, int) and register[x] == 0):
        return
    idx += y - 1

with open("input.txt") as f:
    d = f.readlines()
# d = ["cpy 41 a","inc a","inc a","dec a","jnz a 2","dec a"""] # Example
d = [x.strip().split(' ') for x in d]
d = [[int(x) if any(map(str.isdigit, x)) else x for x in row] for row in d]

# register = {'a':0,'b':0,'c':0,'d':0} # Part 1
register = {'a':0,'b':0,'c':1,'d':0} # Part 2
instruction = dict()
instruction["cpy"] = cpy
instruction["inc"] = inc
instruction["dec"] = dec
instruction["jnz"] = jnz

idx = 0

while idx < len(d):
    instruction[d[idx][0]](*d[idx][1:])
    idx += 1

print(register['a'])