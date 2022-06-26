def read_file(filename):
    with open(filename) as f:
        d = f.readlines()
    d = [x.strip().split() for x in d]
    d = [[x[0], x[1].split(',')] for x in d]
    d = [[x1,x2[0],x2[1],x2[2]] for x1,x2 in d]
    return d

def check_cuboid_intersection(c1,c2):
    if c2[1][0] > c1[1][1] or c2[1][1] < c1[1][0]:
        return False
    if c2[2][0] > c1[2][1] or c2[2][1] < c1[2][0]:
        return False
    if c2[3][0] > c1[3][1] or c2[3][1] < c1[3][0]:
        return False
    return True

def get_cuboid_intersection(c1,c2):
    x = sorted([c1[1][0],c1[1][1],c2[1][0],c2[1][1]])
    y = sorted([c1[2][0],c1[2][1],c2[2][0],c2[2][1]])
    z = sorted([c1[3][0],c1[3][1],c2[3][0],c2[3][1]])
    xmin = x[1]
    xmax = x[2]
    ymin = y[1]
    ymax = y[2]
    zmin = z[1]
    zmax = z[2]
    c = [-1 * c1[0] * c2[0],[xmin,xmax],[ymin,ymax],[zmin,zmax]]
    return c

def add_cuboid(cuboid_test, all_cuboids):
    if cuboid_test[0] == 1:
        cuboids_to_add = [cuboid_test]
    else:
        cuboid_test[0] = 1
        cuboids_to_add = []
    for c in all_cuboids:
        if check_cuboid_intersection(c, cuboid_test):
            cuboids_to_add.append(get_cuboid_intersection(c,cuboid_test))
    for c in cuboids_to_add:
        all_cuboids.append(c)
    return all_cuboids

def calculate_volume(all_cuboids):
    v = 0
    for c in all_cuboids:
        v += c[0] * (c[1][1]-c[1][0]) * (c[2][1]-c[2][0]) * (c[3][1]-c[3][0])
    return v

def main():
    d = read_file("input.txt")

    instructions = []

    for row in d:
        __on = 1 if row[0] == 'on' else -1
        __x = [int(x) for x in row[1][2:].split('..')]
        __y = [int(y) for y in row[2][2:].split('..')]
        __z = [int(z) for z in row[3][2:].split('..')]
        instructions.append([__on,__x,__y,__z])

    for i in range(len(instructions)):
        for j in range(1,4):
            for k in range(2):
                if k % 2 == 0:
                    instructions[i][j][k] -= 0.5
                else:
                    instructions[i][j][k] += 0.5

    all_cuboids = []

    for row in instructions:
        all_cuboids = add_cuboid(row, all_cuboids)

    print(str(int(calculate_volume(all_cuboids))))

if __name__=="__main__":
    main()