import regex as re


with open("input.txt") as f:
    d = f.readlines()
d = [x.strip() for x in d]

count = 0

for ip in d:
    # re.findall only finds non-overlapped matches by default
    find_aba = re.findall(r"(?<!\[[^\]]*)(([a-zA-Z])([a-zA-Z])\2)(?![^\[]*\])", ip, overlapped=True)
    for aba in find_aba:
        if len(set(aba[0])) != 2:
            continue
        bab = aba[2] + aba[1] + aba[2]
        if re.search(r"(?<=\[[^\]]*)" + bab + r"(?=[^\[]*\])", ip):
            count += 1
            break

print(count)