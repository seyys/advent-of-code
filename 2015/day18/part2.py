import numpy as np

def read_input(filename):
    with open(filename) as f:
        bar = f.readlines()
        bar = [x.strip() for x in bar]
    bar = [x.replace("#", "1").replace(".","0") for x in bar]
    bar = np.asarray([[int(x) for x in y] for y in bar],dtype=int)

    return bar

def tick(d):
    d = np.pad(d,1)
    r = d.copy()
    len_x,len_y = d.shape
    for x in range(1,len_x-1):
        for y in range(1,len_y-1):
            if (x == 1 and y == 1) or (x == 1 and y == len_y-2) or (x == len_x-2 and y == 1) or (x == len_x-2 and y == len_y-2):
                r[x,y] = 1
            elif d[x,y] == 0:
                if sum(sum(d[x-1:x+2, y-1:y+2])) == 3:
                    r[x,y] = 1
            else:
                if not (sum(sum(d[x-1:x+2, y-1:y+2])) == 3 or sum(sum(d[x-1:x+2, y-1:y+2])) == 4):
                    r[x,y] = 0
    return r[1:len_x-1,1:len_y-1]
                    
def visualise_image(image):
    for row in image:
        print_row = ''
        for c in row:
            if c == 0:
                print_row += '.'
            else:
                print_row += '#'
        print(print_row)

def main():
    d = read_input('input.txt')
    d[0,0] = 1
    d[0,-1] = 1
    d[-1,0] = 1
    d[-1,-1] = 1
    for _ in range(100):
        d = tick(d)
    print(sum(sum(d)))

if __name__=="__main__":
    main()