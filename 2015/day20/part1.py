d = 29000000
# OEIS seq A002182
candidates = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 15120, 20160, 25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 332640, 498960, 554400, 665280, 720720, 1081080, 1441440, 2162160]

for i in candidates:
    if sum(x * 10 for x in range(1,i+1) if i % x == 0) >= d:
        break

print(i)

# Complete luck that this even finds the right answer lol