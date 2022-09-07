def cpy(x,y):
    if isinstance(y, int):
        return
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
    global register
    if (isinstance(x, int) and x == 0) or (not isinstance(x, int) and register[x] == 0):
        return
    if isinstance(y, str):
        y = register[y]
    idx += y - 1

def tgl(offset):
    global idx
    global d
    global register
    if isinstance(offset, str):
        offset = register[offset]
    if idx + offset >= len(d):
        return
    if len(d[idx + offset]) == 2:
        ins, arg = d[idx + offset]
        if ins == "inc":
            ins = "dec"
        else:
            ins = "inc"
        d[idx + offset] = [ins, arg]
    elif len(d[idx + offset]) == 3:
        ins, arg1, arg2 = d[idx + offset]
        if ins == "jnz":
            ins = "cpy"
        else:
            ins = "jnz"
        d[idx + offset] = [ins, arg1, arg2]
        

with open("input.txt") as f:
    d = f.readlines()
# d = ["cpy 2 a", "tgl a", "tgl a", "tgl a", "cpy 1 a", "dec a", "dec a"] # Example
d = [x.strip().split(' ') for x in d]
d = [[int(x) if any(map(str.isdigit, x)) else x for x in row] for row in d]

register = {'a':7,'b':0,'c':0,'d':0}
instruction = dict()
instruction["cpy"] = cpy
instruction["inc"] = inc
instruction["dec"] = dec
instruction["jnz"] = jnz
instruction["tgl"] = tgl

idx = 0

while idx < len(d):
    instruction[d[idx][0]](*d[idx][1:])
    idx += 1

print(register['a'])