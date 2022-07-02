import numpy as np

class grid:
    def __init__(self,d):
        self.grid = np.array(d)
        self.size_x = len(d[0])
        self.size_y = len(d)
    
    def tick(self):
        # Flag if cucumbers can move east
        to_check = np.asarray(np.where(self.grid == '>')).T
        can_move = []
        moved = False
        for cell in to_check:
            coords_to_check = cell.copy()
            coords_to_check[1] += 1
            if coords_to_check[1] >= self.size_x:
                coords_to_check[1] = 0
            if self.grid[coords_to_check[0]][coords_to_check[1]] == '.':
                can_move.append(cell)

        for cell in can_move:
            self.grid[cell[0]][cell[1]] = '.'
            cell[1] += 1
            if cell[1] >= self.size_x:
                cell[1] = 0
            self.grid[cell[0]][cell[1]] = '>'

        if not can_move == []:
            moved = True

        # Flag if cucumbers can move east
        to_check = np.asarray(np.where(self.grid == 'v')).T
        can_move = []
        for cell in to_check:
            coords_to_check = cell.copy()
            coords_to_check[0] += 1
            if coords_to_check[0] >= self.size_y:
                coords_to_check[0] = 0
            if self.grid[coords_to_check[0]][coords_to_check[1]] == '.':
                can_move.append(cell)

        for cell in can_move:
            self.grid[cell[0]][cell[1]] = '.'
            cell[0] += 1
            if cell[0] >= self.size_y:
                cell[0] = 0
            self.grid[cell[0]][cell[1]] = 'v'

        if not can_move == []:
            moved = True

        return moved

    # def visualise(self):
    #     [print(''.join(x)) for x in self.grid]

with open('input.txt') as f:
    d = f.readlines()
    d = [list(x.strip()) for x in d]

grid = grid(d)
# grid.visualise()

i = 1

while(grid.tick()):
    i += 1
    # grid.visualise()
    pass

print(i)