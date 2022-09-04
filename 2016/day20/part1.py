with open("input.txt") as f:
    d = f.readlines()
d = [x.strip().split('-') for x in d]
d = [[int(x) for x in row] for row in d]
d.sort(key=lambda x: x[0])

smallest_ip = 0
found_smallest_ip = False

while not found_smallest_ip:
    found_smallest_ip = True
    for min_ip, max_ip in d:
        if smallest_ip >= min_ip and smallest_ip <= max_ip:
            found_smallest_ip = False
            smallest_ip = max_ip + 1
            continue
    
print(smallest_ip)