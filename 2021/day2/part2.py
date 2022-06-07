with open('input.txt') as f:
    d = f.readlines()

# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
# It increases your horizontal position by X units.
# It increases your depth by your aim multiplied by X.

x = 0
z = 0
aim = 0
for l in d:
    [dir,dist] = l.split()
    dist = int(dist)
    if dir == "forward":
        x += dist
        z += aim*dist
    if dir == "down":
        aim += dist
    if dir == "up":
        aim -= dist

print(x*z)