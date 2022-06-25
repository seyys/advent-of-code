class player:
    def __init__(self,init_pos:int,roll_generator):
        self.pos = init_pos
        self.points = 0
        self.roll_generator = roll_generator
    
    def roll(self):
        self.pos = (self.pos + next(self.roll_generator) - 1) % 10 + 1
        self.points += self.pos

def roll_3_times():
    i = 1
    while(True):
        roll = 0
        for j in range(3):
            roll += i
            i += 1
            if i > 100:
                i = 1
        yield roll
     
roll_generator = roll_3_times()
p1 = player(2,roll_generator)
p2 = player(8,roll_generator)
num_rolls = 0

while(True):
    p1.roll()
    num_rolls += 3
    if p1.points >= 1000:
        break
    p2.roll()
    num_rolls += 3
    if p2.points >= 1000:
        break

print(min([p1.points,p2.points]) * num_rolls)