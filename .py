import hashlib

str = hashlib.sha256(b'abdullah')

str_hex = str.hexdigest()

print(str_hex)