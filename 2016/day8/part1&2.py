def view_screen(pixels):
    for y in range(display_height):
        line = ''
        for x in range(display_width):
            line += '#' if (x,y) in pixels else '.'
        print(line)

with open("input.txt") as f:
    d = f.readlines()
d = [x.strip() for x in d]

display_width = 50
display_height = 6

display = []

# d = ["rect 3x2", "rotate column x=1 by 1", "rotate row y=0 by 4", "rotate column x=1 by 1"]

for instruction in d:
    if "rect" in instruction:
        a, b = instruction.replace("rect ","").split('x')
        a = int(a)
        b = int(b)
        display.extend((x,y) for x in range(a) for y in range(b))
        display = list(set(display)) # remove dupes
    elif "rotate column" in instruction:
        col, increment = instruction.replace("rotate column x=",'').split(" by ")
        col = int(col)
        increment = int(increment)
        display = [(x, (y + increment) % display_height) if x == col else (x,y) for x,y in display]
    elif "rotate row" in instruction:
        row, increment = instruction.replace("rotate row y=",'').split(" by ")
        row = int(row)
        increment = int(increment)
        display = [((x + increment) % display_width, y) if y == row else (x,y) for x,y in display]

print(len(display))
print()
view_screen(display)