with open("input.txt") as f:
    d = f.readlines()
d = [x.strip().split('-') for x in d]
d = [[int(x) for x in row] for row in d]
d.sort(key=lambda x: x[0])

max_ip_in_system = 4294967295

whitelist = []
ip = 0

while ip < max_ip_in_system:
    found_min_ip_of_whitelist_block = False
    while not found_min_ip_of_whitelist_block and ip < max_ip_in_system:
        found_min_ip_of_whitelist_block = True
        for min_ip, max_ip in d:
            if ip >= min_ip and ip <= max_ip:
                found_min_ip_of_whitelist_block = False
                min_ip_of_whitelist_block = max_ip + 1
                ip = min_ip_of_whitelist_block
                continue
    if found_min_ip_of_whitelist_block:
        max_ip_of_whitelist_block = [x for x,__ in d if x > ip][0] - 1
        ip = max_ip_of_whitelist_block + 1
    else:
        max_ip_of_whitelist_block = max_ip_in_system
    whitelist.append([min_ip_of_whitelist_block, max_ip_of_whitelist_block])

num_whitelist = sum([max_ip - min_ip + 1 for min_ip, max_ip in whitelist])
print(num_whitelist)