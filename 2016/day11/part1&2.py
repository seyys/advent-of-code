import copy


class state:
    def __init__(self):
        # self.objects = {1: [3,1], 2: [0,2], 3: [2,2], 4: [0,0]} # Part 1
        self.objects = {1: [5,3], 2: [0,2], 3: [2,2], 4: [0,0]} # Part 2
        self.num_pairs = sum([x[0] for x in self.objects.values()])
        self.floor = 1
        self.num_moves = 0

    def move(self, new_floor, generators, microchips):
        old_floor = self.floor
        if new_floor < 1 or new_floor > 4:
            return False
        if new_floor > self.floor + 1 or new_floor < self.floor - 1:
            return False
        self.objects[old_floor] = [x - y for x, y in zip(self.objects[old_floor], [generators, microchips])]
        self.objects[new_floor] = [x + y for x, y in zip(self.objects[new_floor], [generators, microchips])]
        self.floor = new_floor
        self.num_moves += 1
        if not self.check_valid():
            return False
        return True
    
    def check_valid(self):
        for generators, microchips in self.objects.values():
            if generators < 0 or microchips < 0:
                return False
            if generators > 0 and microchips > generators:
                return False
        return True
    
    def check_complete(self):
        if self.objects[4] == [self.num_pairs, self.num_pairs]:
            return True
        return False
    
    def __eq__(self, other):
        if not self.objects == other.objects:
            return False
        if not self.floor == other.floor:
            return False
        return True

floor_state = state()

open_list = [floor_state]
closed_list = []

while len(open_list) > 0:
    q = open_list.pop(open_list.index(min(open_list, key=lambda x: (x.num_moves))))
    successors = []
    for new_floor in [q.floor - 1, q.floor + 1]:
        for generators, microchips in [[0, 1], [0, 2], [1, 0], [2, 0], [1, 1]]:
            proposed = copy.deepcopy(q)
            if proposed.move(new_floor, generators, microchips):
                successors.append(proposed)
    for successor in successors:
        if successor.check_complete():
            min_moves = successor.num_moves
            open_list = []
            break

        successor_in_open_list = [x for x in open_list if x == successor]
        if successor_in_open_list:
            if successor_in_open_list[0].num_moves <= successor.num_moves:
                continue

        successor_in_closed_list = [x for x in closed_list if x == successor]
        if successor_in_closed_list:
            if successor_in_closed_list[0].num_moves <= successor.num_moves:
                continue
        
        open_list.append(successor)
    closed_list.append(q)

print(min_moves)