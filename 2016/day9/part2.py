import re


def decompress(d):
    if '(' in d:
        len_decompressed = 0
        while '(' in d:
            idx_start = d.index('(')
            idx_end = d.index(')')
            len_section, num_repeats = d[idx_start+1:idx_end].split('x')
            len_section = int(len_section)
            num_repeats = int(num_repeats)
            len_decompressed += idx_start
            len_decompressed += num_repeats * decompress(d[idx_end+1:idx_end+len_section+1])
            d = d[idx_end+len_section+1:]
        len_decompressed += len(d)
        return len_decompressed
    else:
        return len(d)

with open("input.txt") as f:
    d = f.readlines()
d = d[0].strip()

# Assume that all expansions are neatly nested

# d = "X(8x2)(3x3)ABCY"
# d = "X(8x2)(3x3)ABCY" # -> X(3x3)ABC(3x3)ABCY
# d = "(27x12)(20x12)(13x14)(7x10)(1x12)A" # -> 12x ((20x12)(13x14)(7x10)(1x12)A)
# d = "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN" # -> 3x ((3x3)ABC(2x3)XY(5x2)PQRST) X(18x9)(3x2)TWO(5x7)SEVEN

idx = 0

print(decompress(d))