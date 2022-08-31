import hashlib


class state:
    directions = ['U', 'D', 'L','R']
    maxsize = (4,4)

    def __init__(self, h):
        self.passcode = h

    @staticmethod
    def find_coords(passcode):
        x_coord = passcode.count('R') - passcode.count('L')
        y_coord = passcode.count('D') - passcode.count('U')
        return (x_coord, y_coord)

    def find_valid_move(self):
        h = hashlib.md5(bytes(self.passcode,"utf-8")).hexdigest()[:4]
        valid_moves = []
        for idx, direction in enumerate(h):
            if direction in "bcdef":
                proposed_move = self.passcode + self.directions[idx]
                new_coords = state.find_coords(proposed_move)
                if new_coords[0] < 0 or new_coords[0] >= self.maxsize[0] or new_coords[1] < 0 or new_coords[1] >= self.maxsize[1]:
                    continue
                valid_moves.append(proposed_move)
        return valid_moves

    def path_length(self):
        return len([x for x in self.passcode if x in "UDLR"])
    
    def check_if_at_goal(self):
        return state.find_coords(self.passcode) == (self.maxsize[0]-1, self.maxsize[1]-1)

d = "rrrbmfta"
states = [state(d)]
longest_path = 0

while len(states) > 0:
    potential_path = states.pop()
    if potential_path.check_if_at_goal():
        if longest_path < potential_path.path_length():
            longest_path = potential_path.path_length()
        continue
    states.extend([state(x) for x in potential_path.find_valid_move()])

print(longest_path)