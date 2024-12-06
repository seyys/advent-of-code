import re
import numpy as np
import copy

MOVEMENT_COST = dict({'A':1, 'B':10, 'C':100, 'D':1000})

class burrow_map:
    def __init__(self, rooms):
        self.hallway = hallway()
        self.rooms = [room(x,y) for x,y in zip(rooms,['A','B','C','D'])]
        self.cost = 0
    
    def complete(self):
        return all(x.complete() for x in self.rooms)

    def move(self,start,end):
        if start in self.hallway.rooms_pos and end in self.hallway.rooms_pos:
            cost, amphipod = self.rooms[self.hallway.rooms_pos.index(start)].pop()
            cost += self.rooms[self.hallway.rooms_pos.index(end)].push(amphipod)
            cost += self.hallway.cost(start, end)
            self.cost += cost * MOVEMENT_COST[amphipod]
            return self

        if start in self.hallway.rooms_pos:
            cost, amphipod = self.rooms[self.hallway.rooms_pos.index(start)].pop()
        else:
            cost, amphipod = self.hallway.pop(start,end)
        if end in self.hallway.rooms_pos:
            cost += self.rooms[self.hallway.rooms_pos.index(end)].push(amphipod)
        else:
            cost += self.hallway.push(start,end,amphipod)
        self.cost += cost * MOVEMENT_COST[amphipod]
        return self

    def possible_moves(self):
        possible_moves = []
        # Hallway to room
        for start in self.hallway.member.keys():
            amphipod = self.hallway.member[start]
            for end in self.hallway.rooms_pos:
                cost = self.hallway.cost(start, end) + self.rooms[self.hallway.rooms_pos.index(end)].push_cost(amphipod)
                cost *= MOVEMENT_COST[amphipod]
                if np.isinf(cost):
                    continue
                # possible_moves.append([cost,start,end])
                return True, [cost,start,end]
        # Room to room
        for start in self.hallway.rooms_pos:
            for end in self.hallway.rooms_pos:
                if start == end:
                    continue
                cost = self.rooms[self.hallway.rooms_pos.index(start)].pop_cost()
                if np.isinf(cost):
                    continue
                amphipod = self.rooms[self.hallway.rooms_pos.index(start)].members[0]
                cost += self.rooms[self.hallway.rooms_pos.index(end)].push_cost(amphipod)
                if np.isinf(cost):
                    continue
                cost += self.hallway.cost(start, end)
                cost *= MOVEMENT_COST[amphipod]
                return True, [cost,start,end]
        # Room to hallway
        for start in self.hallway.rooms_pos:
            for end in [0,1,9,10,3,5,7]:
                cost = self.rooms[self.hallway.rooms_pos.index(start)].pop_cost() + self.hallway.cost(start, end)
                if np.isinf(cost):
                    continue
                amphipod = self.rooms[self.hallway.rooms_pos.index(start)].members[0]
                cost *= MOVEMENT_COST[amphipod]
                possible_moves.append([cost,start,end]) 
        return False, possible_moves

class room:
    def __init__(self, members, amphipod_allowed):
        self.members = members
        self.amphipod_allowed = amphipod_allowed
        self.size = len(members)
        self.dist_door = 1
    
    def pop(self):
        if self.complete() or not self.members:
            return np.inf, ''
        cost = self.dist_door
        self.dist_door += 1
        self.size -= 1
        amphi = self.members[0]
        self.members = self.members[1:]
        return cost, amphi

    def push(self,amphipod):
        if not self.is_allowed(amphipod):
            return np.inf
        cost = self.dist_door - 1
        self.dist_door -= 1
        self.size += 1
        self.members.insert(0, amphipod)
        return cost
    
    def pop_cost(self):
        if self.complete() or not self.members or all(x == self.amphipod_allowed for x in self.members):
            return np.inf
        return self.dist_door
    
    def push_cost(self,amphipod):
        if not self.is_allowed(amphipod):
            return np.inf
        return self.dist_door - 1
            
    def is_allowed(self,amphipod):
        if amphipod is not self.amphipod_allowed:
            return False
        if any(x != self.amphipod_allowed for x in self.members):
            return False
        return True
    
    def complete(self):
        return self.dist_door == 1 and all(x == self.amphipod_allowed for x in self.members)

class hallway:
    #0123456789A#
    ###a#b#c#d#
    def __init__(self):
        self.member = dict()
        self.rooms_pos = [2,4,6,8]
        pass

    def valid_move(self,start,end):
        # Can't move between two positions in hallway
        # if start not in self.rooms_pos and end not in self.rooms_pos:
        #     return False
        # Can't move outside room door
        # if end in self.rooms_pos:
        #     return False
        # Passage is blocked
        if start < end:
            p1 = start
            p2 = end
        else:
            p1 = end
            p2 = start
        for pos in self.member.keys():
            if pos > p1 and pos < p2:
                return False
        return True

    def push(self,start,end,amphipod):
        if not self.valid_move(start,end):
            return np.inf
        cost = abs(end-start)
        self.member[end] = amphipod
        return cost
    
    def pop(self,start,end):
        if not self.valid_move(start,end):
            return np.inf, ''
        cost = abs(end-start)
        return cost, self.member.pop(start)

    def cost(self,start,end):
        if not self.valid_move(start,end):
            return np.inf
        return abs(end-start)

with open('test.txt') as f:
    __ = f.readline()
    __ = f.readline()
    d = []
    foo = f.readline()
    while(foo != "  #########\n"):
        foo = re.search('[A-D]#[A-D]#[A-D]#[A-D]' , foo).group()
        d.append(foo.split('#'))
        foo = f.readline()
    d = [[row[i] for row in d] for i in range(len(d[0]))]

burrow_map = burrow_map(d)
open_list = [burrow_map]
closed_list = []
lowest_cost = np.inf

while(len(open_list) > 0):
    open_list.sort(key=lambda x: x.cost)
    current_map = open_list.pop(0)
    if current_map.complete():
        lowest_cost = min(lowest_cost, current_map.cost)
    forced_move, possible_moves = current_map.possible_moves()
    if forced_move:
        possible_moves = [possible_moves]
    for move in possible_moves:
        new_map = copy.deepcopy(current_map)
        new_map.move(move[1], move[2])
        node_in_closed_list = [x for x in closed_list if (x.rooms == new_map.rooms) and (x.hallway == new_map.hallway)]
        if len(node_in_closed_list) > 1:
            raise Exception("Too many proposed nodes in closed list")
        if len(node_in_closed_list) == 1:
            if node_in_closed_list[0].cost > new_map.cost:
                closed_list.pop(node_in_closed_list[0])
                closed_list.append(new_map)
            continue
        open_list.append(new_map)
    closed_list.append(current_map)

print(lowest_cost)