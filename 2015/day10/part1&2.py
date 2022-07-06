def calc_next(s):
    num = None
    count = 0
    r = ""
    for i in range(len(s)):
        if count == 0:
            num = s[i]
            count = 1
            continue
        if num == s[i]:
            count += 1
        else:
            r += str(count) + num
            num = s[i]
            count = 1
    r += str(count) + num
    return r

d = "1321131112"

for i in range(50):
    d = calc_next(d)

print(len(d))