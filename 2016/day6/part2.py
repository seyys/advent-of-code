import numpy as np
from collections import Counter


with open("input.txt") as f:
    d = f.readlines()
d = [x.strip() for x in d]
d = [[x for x in row] for row in d]
d = np.asarray(d)

message = ""

for col in d.T:
    message += Counter(col).most_common()[-1][0]
    
print(message)