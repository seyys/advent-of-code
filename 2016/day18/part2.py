def find_next_row(previous_row):
    previous_row = '.' + previous_row + '.'
    next_row = ''
    for left, centre, right in zip(previous_row[:-2], previous_row[1:-1], previous_row[2:]):
        if (left == '^' and centre == '^' and right == '.') or \
           (left == '.' and centre == '^' and right == '^') or \
           (left == '^' and centre == '.' and right == '.') or \
           (left == '.' and centre == '.' and right == '^'):
            next_row += '^'
        else:
            next_row += '.'
    return next_row

def print_grid(grid):
    [print(x) for x in grid]

with open("input.txt") as f:
    d = f.readline().strip()

grid = [d]

for _ in range(400000-1):
    grid.append(find_next_row(grid[-1]))

print_grid(grid)

print(sum([sum([x.count('.') for x in row]) for row in grid]))