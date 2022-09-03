import numpy as np

d = 3001330

"""
4=1
5=3
6=5
7=7
8=1
9=3
10=5
11=7
12=9
13=11
14=13
15=15
16=1

2**n+m = 1+2*m
"""

elf = int(1 + 2 * (d - 2 ** np.floor(np.log2(d))))

print(elf)