import json

with open('input.txt') as f:
    d = json.load(f)

stack = [d]
count = 0

while(len(stack) > 0):
    el = stack.pop()
    if type(el) == dict:
        if "red" in el.values():
            continue
        [stack.append(el[x]) for x in el]
    elif type(el) == list:
        [stack.append(x) for x in el]
    elif type(el) == int:
        count += el
          
print(count)