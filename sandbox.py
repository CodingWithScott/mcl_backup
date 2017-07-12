import hashlib

file1_md5_hasher = hashlib.md5()
file1_sha1_hasher = hashlib.sha1()

with open('trump.webp', 'rb') as md5_file:
    buf = md5_file.read()
    file1_md5_hasher.update(buf)

with open('trump.webp', 'rb') as sha1_file:
    buf = sha1_file.read()
    file1_sha1_hasher.update(buf)

print('\ntrump.webp')
print('md5:\t', file1_md5_hasher.hexdigest())
print('sha1:\t', file1_sha1_hasher.hexdigest())

file2_md5_hasher = hashlib.md5()
file2_sha1_hasher = hashlib.sha1()

with open('trump2.webp', 'rb') as md5_file:
    buf = md5_file.read()
    file2_md5_hasher.update(buf)

with open('trump2.webp', 'rb') as sha1_file:
    buf = sha1_file.read()
    file2_sha1_hasher.update(buf)

print('\ntrump2.webp')
print('md5:\t', file1_md5_hasher.hexdigest())
print('sha1:\t', file1_sha1_hasher.hexdigest())
print()

if (file1_md5_hasher.hexdigest() == file2_md5_hasher.hexdigest()):
    print('MD5 check:\tok!')
else:
    print('MD5 check:\tfailed!')
if (file1_sha1_hasher.hexdigest() == file2_sha1_hasher.hexdigest()):
    print('SHA1 check:\tok!')
else:
    print('SHA1 check:\tfailed!')
