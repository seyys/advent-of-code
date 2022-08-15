import regex as re


def is_abba(matches):
    is_abba = False
    for pattern in matches:
        if len(set(pattern[0])) == 2:
            is_abba = True
            break
    return is_abba

with open("input.txt") as f:
    d = f.readlines()
d = [x.strip() for x in d]

count = 0

for ip in d:
    check_in_brackets = re.findall(r"((?<=\[[^\]]*)([a-zA-Z])([a-zA-Z])\3\2(?=[^\[]*\]))", ip)
    if check_in_brackets and is_abba(check_in_brackets):
        continue
    check_outside_brackets = re.findall(r"((?<!\[[^\]]*)([a-zA-Z])([a-zA-Z])\3\2(?![^\[]*\]))", ip)
    if check_outside_brackets and is_abba(check_outside_brackets):
        count += 1

print(count)