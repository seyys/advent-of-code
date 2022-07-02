import hashlib

d = b"yzbqklnj"
salt = 1

while(True):
    r_hash = hashlib.md5(d + bytes(salt)).hexdigest()
    if int(r_hash[0:6],16) == 0:
        break
    salt += 1

print(salt)