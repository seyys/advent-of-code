import re

def increment_pw(pw):
    i = 1
    while(True):
        if pw[-i] == "z":
            pw[-i] = "a"
        else:
            pw[-i] = chr(ord(pw[-i]) + 1)
            break
        i += 1
    return pw

# pw = "hxbxwxba" # Part 1
pw = "hxbxxyzz" # Part 2
pw = list(pw)

while(True):
    pw = increment_pw(pw)
    if "i" in pw or "j" in pw or "o" in pw:
        continue
    if not re.findall(r"abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz", "".join(pw)):
        continue
    if not re.findall(r"(\w)\1.*(\w)\2", "".join(pw)):
        continue
    break

print("".join(pw))