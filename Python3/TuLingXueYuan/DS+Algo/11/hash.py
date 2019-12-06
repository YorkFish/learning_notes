import hashlib


md5 = hashlib.md5()
# md5.update(b"hello world")
md5.update(bytes("hello world", "utf8"))
password = md5.hexdigest()
print(password)
