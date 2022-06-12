with open('input.txt') as f:
    d = f.readlines()
    dd = []
    for row in d:
        foo = row.split(" | ")
        foo = [x.split() for x in foo]
        dd.append(foo)

segments = []
digits = []
for i in range(len(dd)):
    segments.append(["abcdefg" for x in range(7)])
    digits.append(["" for x in range(10)])
    for digit in [item for sublist in dd[i] for item in sublist]:
        if len(digit) == 2: # 1
            for character in digit:
                for pos in [0,1,3,4,6]:
                    segments[i][pos] = segments[i][pos].replace(character,"")
            digits[i][1] = ''.join(sorted(digit))
        if len(digit) == 3: # 7
            for character in digit:
                for pos in [1,3,4,6]:
                    segments[i][pos] = segments[i][pos].replace(character,"")
            digits[i][7] = ''.join(sorted(digit))
        if len(digit) == 4: # 4
            for character in digit:
                for pos in [0,4,6]:
                    segments[i][pos] = segments[i][pos].replace(character,"")
            digits[i][4] = ''.join(sorted(digit))
        if len(digit) == 7:
            digits[i][8] = ''.join(sorted(digit))
    # pos 0
    segments[i][0] = ''.join((set(digits[i][7])).difference(set(digits[i][1])))
    for pos in [1,2,3,4,5,6]:
        segments[i][pos] = segments[i][pos].replace(segments[i][0], "")
    # digit 4
    for pos in [2,4]:
        segments[i][pos] = ''.join((set(digits[i][4])).difference(set(digits[i][1])))
    for pos in [0,1,3,5,6]:
        for character in segments[i][2]:
            segments[i][pos] = segments[i][pos].replace(character, "")
    # 5 seg digits
    for digit in [item for sublist in dd[i] for item in sublist]:
        if len(digit) == 5:
            # digit 3
            foo = digit
            for character in digits[i][7]:
                foo = foo.replace(character,"")
            if len(foo) == 2:
                digits[i][3] = ''.join(sorted(digit))
                continue
            # digit 5 and 2
            for character in digits[i][4]:
                foo = foo.replace(character, "")
            if len(foo) == 1:
                digits[i][5] = ''.join(sorted(digit))
            else:
                digits[i][2] = ''.join(sorted(digit))
    # pos 3
    foo_3 = digits[i][3]
    foo_4 = digits[i][4]
    for character in digits[i][1]:
        foo_3 = foo_3.replace(character, "")
        foo_4 = foo_4.replace(character, "")
    segments[i][3] = ''.join(set(foo_3).intersection(foo_4))
    for digit in [item for sublist in dd[i] for item in sublist]:
        if len(digit) == 6:
            # digit 0
            if len(set(digit).union(segments[i][3])) == 7:
                digits[i][0] = ''.join(sorted(digit))
            elif len(set(digit).intersection(digits[i][1])) == 1:
                digits[i][6] = ''.join(sorted(digit))
            else:
                digits[i][9] = ''.join(sorted(digit))
    x = 1

values = []
for i in range(len(dd)):
    v = []
    for j in dd[i][1]:
        v.append((digits[i]).index(''.join(sorted(j))))
    v = ''.join([str(x) for x in v])
    v = int(v)
    values.append(v)

print(sum(values))
"""
1 - count 2 -     2     5
7 - count 3 - 0   2     5
4 - count 4 -   1 2 3   5
8 - count 7 - 0 1 2 3 4 5 6

2 - count 5 - 0   2 3 4   6
3 - count 5 - 0   2 3   5 6
5 - count 5 - 0 1   3   5 6

6 - count 6 - 0 1   3 4 5 6
9 - count 6 - 0 1 2 3   5 6
0 - count 6 - 0 1 2   4 5 6

 0000
1    2
1    2
 3333
4    5
4    5
 6666
"""