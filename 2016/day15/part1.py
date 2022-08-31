import re


class disk:
    def __init__(self, disk_num, num_pos, init_pos):
        self.disk_num = disk_num
        self.num_pos = num_pos
        self.init_pos = init_pos
        self.capsule_pos = disk_num + init_pos

    def increment(self, t):
        return (self.capsule_pos + t) % self.num_pos

with open("input.txt") as f:
    d = f.readlines()

disk_arrangement = []
for row in d:
    disk_num = int(re.search(r"(?<=Disc #)\d+", row).group(0))
    num_pos = int(re.search(r"\d+(?= positions)", row).group(0))
    init_pos = int(re.search(r"(?<=position )\d+", row).group(0))
    disk_arrangement.append(disk(disk_num, num_pos, init_pos))

t = 0
while True:
    if all(x.increment(t) == 0 for x in disk_arrangement):
        shortest_t = t
        break
    t += 1

print(shortest_t)