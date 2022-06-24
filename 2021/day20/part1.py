import numpy as np

def read_input(filename:str):
    with open(filename) as f:
        line = f.readline()
        foo = ''
        while line != '\n':
            foo += line.strip()
            line = f.readline()
        bar = f.readlines()
        bar = [x.strip() for x in bar]

    foo = foo.replace("#", "1").replace(".","0")
    enhancement_algorithm = dict()
    for i in range(len(foo)):
        enhancement_algorithm[i] = foo[i]

    bar = [x.replace("#", "1").replace(".","0") for x in bar]
    input_image = np.asarray([[int(x) for x in y] for y in bar],dtype=int)

    return enhancement_algorithm, input_image

def trim_rows_cols(input_image:np.ndarray):
    for rot in range(4):
        input_image = np.rot90(input_image)
        for i in range(len(input_image)):
            if sum(input_image[i]) != 0 or sum(input_image[i]) == len(input_image[i]):
                break
        input_image = input_image[i:]
    return input_image

def mat_to_int(mat:np.ndarray):
    bin_digits = mat.flatten()
    i = 0
    result = 0
    for d in bin_digits[::-1]:
        result += d<<i
        i += 1
    return result

def enhance(input_image:np.ndarray, enhancement_algorithm:dict, zero_padding:bool):
    input_image = trim_rows_cols(input_image)
    if zero_padding:
        input_image = np.pad(input_image,4)
        output_image = np.zeros(((len(input_image)),len(input_image[0,:])),dtype=int)
    else:
        input_image = np.pad(input_image,4,constant_values=1)
        output_image = np.ones(((len(input_image)),len(input_image[0,:])),dtype=int)
    for row in range(1,len(input_image)-1):
        for col in range(1,len(input_image)-1):
            output_image[col][row] = enhancement_algorithm[mat_to_int(input_image[col-1:col+2,row-1:row+2])]
    output_image = output_image[1:len(output_image)-1,1:len(output_image[0,:])-1]
    return output_image, not zero_padding

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
    enhancement_algorithm, input_image = read_input('input.txt')
    zero_padding = True
    visualise_image(input_image)
    print()
    image, zero_padding = enhance(input_image, enhancement_algorithm, zero_padding)
    visualise_image(image)
    print()
    image, zero_padding = enhance(image, enhancement_algorithm, zero_padding)
    visualise_image(image)
    print()
    print(sum(sum(image)))

if __name__=="__main__":
    main()