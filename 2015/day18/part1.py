import numpy as np

def read_input(filename:str):
    with open(filename) as f:
        bar = f.readlines()
        bar = [x.strip() for x in bar]
    bar = [x.replace("#", "1").replace(".","0") for x in bar]
    bar = np.asarray([[int(x) for x in y] for y in bar],dtype=int)

    return bar

def tick(d:np.ndarray):
    d = np.pad(d,1)
    r = d.copy()
    len_x,len_y = d.shape
    for x in range(1,len_x-1):
        for y in range(1,len_y-1):
            if d[x,y] == 0:
                if sum(sum(d[x-1:x+2, y-1:y+2])) == 3:
                    r[x,y] = 1
            else:
                if not (sum(sum(d[x-1:x+2, y-1:y+2])) == 3 or sum(sum(d[x-1:x+2, y-1:y+2])) == 4):
                    r[x,y] = 0
    return r[1:len_x-1,1:len_y-1]
                    
def visualise_image(image:np.ndarray):
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
    for _ in range(100):
        d = tick(d)
    print(sum(sum(d)))

if __name__=="__main__":
    main()