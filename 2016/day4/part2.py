from collections import Counter
import re


def calculate_checksum(name):
    r = Counter(name)
    del r['-']
    r = sorted(list(r.most_common()), key=lambda x: (-x[1], x[0]))
    r = ''.join([x[0] for i, x in enumerate(r) if i < 5])
    return r

def decrypt_cipher(name, rot):
    r = ""
    for c in name:
        if c == '-':
            r += '-'
            continue
        r += chr((ord(c) - ord('a') + rot) % 26 + ord('a'))
    return r

with open("input.txt") as f:
    d = f.readlines()
d = [x.strip() for x in d]
d = [[re.search(r"[a-z\-]+", x).group(0), int(re.search(r"\d+", x).group(0)), re.search(r"(?<=\[)[a-z]+(?=\])", x).group(0)] for x in d]

for name, sector_id, checksum in d:
    if calculate_checksum(name) == checksum:
        print(decrypt_cipher(name, sector_id), sector_id)