import numpy as np
import re

with open('input.txt') as f:
    d = f.readlines()
    d = [x.strip() for x in d]

ingredients = []
max_score = 0

for row in d:
    ingredients.append([int(_) for _ in re.findall(r"\-?\d+", row)])

ingredients = np.asarray(ingredients, dtype=int) 

for a in range(1,101):
    for b in range(1,101):
         for c in range(1,101):
            for d in range(1,101):
                if a + b + c + d != 100:
                    continue
                max_score = max(np.product(np.maximum(np.sum(ingredients * np.reshape(np.array([a,b,c,d]*5), (5,4)).T,axis=0),0)[0:4]),max_score)

print(max_score)