import numpy as np

def calculate_basin_size(i,j,basin_size):
    basin_topology[i][j] = 1
    if d[i-1][j] < 9 and basin_topology[i-1][j] == 0:
        basin_size = calculate_basin_size(i-1,j,basin_size)
    if d[i+1][j] < 9 and basin_topology[i+1][j] == 0:
        basin_size = calculate_basin_size(i+1,j,basin_size)
    if d[i][j-1] < 9 and basin_topology[i][j-1] == 0:
        basin_size = calculate_basin_size(i,j-1,basin_size) 
    if d[i][j+1] < 9 and basin_topology[i][j+1] == 0:
        basin_size = calculate_basin_size(i,j+1,basin_size)
    return basin_size + 1

with open('input.txt') as f:
    d = f.readlines()
    d = [list(x.strip()) for x in d]
    d = [[int(x) for x in y] for y in d]

d = np.asarray(d)

# Add tall features on all edges
d = np.vstack((np.ones(len(d[0]))*np.inf,d,np.ones(len(d[0]))*np.inf))
d = np.hstack((np.ones([len(d[:,0]),1])*np.inf,d,np.ones([len(d[:,0]),1])*np.inf))

basin_sizes = []
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
        basin_topology = np.zeros([len(d[:,0]),len(d[0])])
        basin_sizes.append(calculate_basin_size(i,j,0))

largest_3_basins = list(reversed(sorted(basin_sizes)))
print(largest_3_basins[0] * largest_3_basins[1] * largest_3_basins[2])