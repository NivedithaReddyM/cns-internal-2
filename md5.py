import hashlib


def md5(s):
    s_bytestring=s.encode()
    m=hashlib.md5()
    m.update(s_bytestring)
    return m.hexdigest()

s=input("Enter string:")
print(md5(s))
