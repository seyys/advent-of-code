d = "01111001100111011"
disk_size = 272

while len(d) < disk_size:
    a = d
    b = ''.join(['0' if x == '1' else '1' for x in a[::-1]])
    d = a + '0' + b

d = d[:disk_size]
checksum = d
while len(checksum) % 2 == 0:
    new_checksum = ''
    for i in range(0, len(checksum), 2):
        new_checksum += '1' if checksum[i] == checksum[i+1] else '0'
    checksum = new_checksum

print(checksum)
