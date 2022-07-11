import re

with open('input.txt') as f:
    instructions = f.readlines()
    instructions = [x.strip() for x in instructions]

instructions = [re.split(r" |, ", x) for x in instructions]
for i, row in enumerate(instructions):
    for j, val in enumerate(row):
        if '+' in val or '-' in val:
            instructions[i][j] = int(val)

# register = {'a': 0, 'b': 0} # Part 1
register = {'a': 1, 'b': 0} # Part 2
i = 0

while(i < len(instructions)):
    instruction = instructions[i][0]
    if instruction == "hlf":
        register[instructions[i][1]] /= 2
        i += 1
    elif instruction == "tpl":
        register[instructions[i][1]] *= 3
        i += 1
    elif instruction == "inc":
        register[instructions[i][1]] += 1
        i += 1
    elif instruction == "jmp":
        i += instructions[i][1]
    elif instruction == "jie":
        if register[instructions[i][1]] % 2 == 0:
            i += instructions[i][2]
        else:
            i += 1
    elif instruction == "jio":
        if register[instructions[i][1]] == 1:
            i += instructions[i][2]
        else:
            i += 1

print(register)