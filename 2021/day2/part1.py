with open('input.txt') as f:
    d = f.readlines()

# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.

x = 0
z = 0
for l in d:
    [dir,dist] = l.split()
    dist = int(dist)
    if dir == "forward":
        x += dist
    if dir == "down":
        z += dist
    if dir == "up":
        z -= dist

print(x*z)