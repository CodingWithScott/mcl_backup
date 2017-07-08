import hashlib
 
hasher = hashlib.md5()
with open('trump.gif', 'rb') as afile:
    buf = afile.read()
    hasher.update(buf)
print(hasher.hexdigest())