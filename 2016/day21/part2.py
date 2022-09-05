import re
import typing


class ins:
    rotate_char_lut = [-1,-1,2,-2,1,-3,0,-4]

    def swap_pos(s: str, x: int, y: int) -> str:
        r = list(s)
        r[x] = s[y]
        r[y] = s[x]
        return ''.join(r)

    def swap_letter(s: str, x: str, y: str) -> str:
        r = list(s)
        r[s.index(x)] = y
        r[s.index(y)] = x
        return ''.join(r)
    
    def rotate_steps(s: str, direction: str, x: int) -> str:
        r = list(s)
        if direction == "left":
            x = -x
        x = x % len(s)
        r = r[x:] + r[:x]
        return ''.join(r)

    def rotate_char(s: str, x: str) -> str:
        idx = s.index(x)
        idx = ins.rotate_char_lut[idx]
        return ins.rotate_steps(s, "left", idx)

    def reverse(s: str, x: int, y: int) -> str:
        r = list(s)
        r = r[:x] + r[x:y+1][::-1] + r[y+1:]
        return ''.join(r)
    
    def move(s: str, x: int, y: int) -> str:
        r = list(s)
        c = r.pop(y)
        r = r[:x] + [c] + r[x:]
        return ''.join(r)

with open("input.txt") as f:
    d = f.readlines()
d = [x.strip() for x in d]

inp = "fbgdceah"

for row in d[::-1]:
    if "swap position" in row:
        x, y = re.findall(r"(?<=position )\d+", row)
        inp = ins.swap_pos(inp, int(x), int(y))
    elif "swap letter" in row:
        x, y = re.findall(r"(?<=letter )[a-z]+", row)
        inp = ins.swap_letter(inp, x, y)
    elif "step" in row:
        direction = re.findall(r"(?<=rotate )[a-z]+", row)[0]
        x = re.findall(r"\d+(?= step)", row)[0]
        inp = ins.rotate_steps(inp, direction, int(x))
    elif "rotate based on" in row:
        x = re.findall(r"(?<=letter )[a-z]+", row)[0]
        inp = ins.rotate_char(inp, x)
    elif "reverse" in row:
        row = row.replace("reverse positions ", '')
        x, y = row.split(" through ")
        inp = ins.reverse(inp, int(x), int(y))
    elif "move" in row:
        x, y = re.findall(r"(?<=position )\d+", row)
        inp = ins.move(inp, int(x), int(y))

print(inp)