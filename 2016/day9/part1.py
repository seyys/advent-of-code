with open("input.txt") as f:
    d = f.readlines()
d = d[0].strip()

# d = "X(8x2)(3x3)ABCY"

decompressed_file = ""
idx = 0

while idx < len(d):
    if d[idx] == '(':
        instruction = ''
        while d[idx] != ')':
            idx += 1
            instruction += d[idx]
        idx += 1
        copy_length, copy_repeats = instruction[:-1].split('x')
        copy_length = int(copy_length)
        copy_repeats = int(copy_repeats)
        decompressed_file += d[idx:idx + copy_length] * copy_repeats
        idx += copy_length
    else:
        decompressed_file += d[idx]
        idx += 1

# print(decompressed_file)
print(len(decompressed_file))