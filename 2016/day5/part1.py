import hashlib

d = "abbhdwsy"
salt = 0
password = ""

while(True):
    r_hash = hashlib.md5((d + str(salt)).encode(encoding='UTF-8')).hexdigest()
    if int(r_hash[0:5],16) == 0:
        password += r_hash[5]
        if len(password) >= 8:
            break
    salt += 1

print(password)