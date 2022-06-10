def parse_input(input):
    input = input.strip()
    input = input.split(" -> ")
    input = [x.split(",") for x in input]
    input = [[int(x) for x in y] for y in input]
    return input

def init_board(d):
    grid_size = max(max(max(d))) + 2
    board = [[0 for x in range(grid_size)] for y in range(grid_size)]
    return board

with open("input.txt") as f:
    d = [parse_input(x) for x in f.readlines()]

board = init_board(d)

for i in d:
    x1,y1 = i[0]
    x2,y2 = i[1]
    if x1 == x2:
        x = x1
        y_start = min(y1,y2)
        y_end = max(y1,y2)
        for y in range(y_start,y_end+1):
            board[y][x] += 1
        x = 1
    elif y1 == y2:
        y = y1
        x_start = min(x1,x2)
        x_end = max(x1,x2)
        for x in range(x_start,x_end+1):
            board[y][x] += 1

board = [x for xs in board for x in xs]

danger = len([x for x in board if x >= 2])

print(danger)