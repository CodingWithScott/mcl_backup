import hashlib

md5_hasher = hashlib.md5()
sha1_hasher = hashlib.sha1()

with open('trump.webp', 'rb') as md5_file:
    buf = md5_file.read()
    md5_hasher.update(buf)

with open('trump.webp', 'rb') as sha1_file:
    buf = sha1_file.read()
    sha1_hasher.update(buf)

print('\ntrump.webp')
print('md5:\t', md5_hasher.hexdigest())
print('sha1:\t', sha1_hasher.hexdigest())

md5_hasher2 = hashlib.md5()
sha1_hasher2 = hashlib.sha1()

with open('trump2.webp', 'rb') as md5_file:
    buf = md5_file.read()
    md5_hasher2.update(buf)

with open('trump2.webp', 'rb') as sha1_file:
    buf = sha1_file.read()
    sha1_hasher2.update(buf)

print('\ntrump2.webp')
print('md5:\t', md5_hasher2.hexdigest())
print('sha1:\t', sha1_hasher2.hexdigest())

