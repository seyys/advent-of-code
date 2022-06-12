import numpy as np

with open('input.txt') as f:
    d = f.readlines()
    d = [list(x.strip()) for x in d]
    d = [[int(x) for x in y] for y in d]

d = np.asarray(d)

# Add tall features on all edges
d = np.vstack((np.ones(len(d[0]))*np.inf,d,np.ones(len(d[0]))*np.inf))
d = np.hstack((np.ones([len(d[:,0]),1])*np.inf,d,np.ones([len(d[:,0]),1])*np.inf))

risk = 0
for j in range(1,len(d[0])-1):
    for i in range(1,len(d[:,0])-1):
        if d[i][j] >= d[i-1][j]:
            continue
        if d[i][j] >= d[i+1][j]:
            continue
        if d[i][j] >= d[i][j-1]:
            continue
        if d[i][j] >= d[i][j+1]:
            continue
        risk += d[i][j]+1

print(risk)