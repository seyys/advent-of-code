import re
import random

class molecule_stage:
    def __init__(self, formula, stage):
        self.formula = formula
        self.stage = stage

    def len(self):
        return len(self.formula)

with open('input.txt') as f:
    d = []
    foo = f.readline()
    while(foo != "\n"):
        d.append(foo)
        foo = f.readline()
    d = [x.strip() for x in d]
    d = [x.split(" => ") for x in d]
    seed = f.readline()
    seed = seed.strip()

is_stuck = False
molecule = seed
iterations = 0

while(molecule != "e"):
    if is_stuck:
        molecule = seed
        iterations = 0
        random.shuffle(d)
    is_stuck = True
    for transform in d:
        if transform[1] in molecule:
            molecule = molecule.replace(transform[1], transform[0],1)
            iterations += 1
            is_stuck = False

print(iterations)