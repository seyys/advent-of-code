import hashlib

d = "abbhdwsy"
salt = 0
password = [None] * 8

while(True):
    r_hash = hashlib.md5((d + str(salt)).encode(encoding='UTF-8')).hexdigest()
    if int(r_hash[0:5],16) == 0:
        position = int(r_hash[5], 16)
        character = r_hash[6]
        if position < 8 and password[position] == None:
            password[position] = character
            if all(password):
                break
    salt += 1

print(''.join(password))