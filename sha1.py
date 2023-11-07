import hashlib


def sha1(s):
    s_bytestring=s.encode()
    m=hashlib.sha1()
    m.update(s_bytestring)
    return m.hexdigest()

s=input("Enter string:")
print(sha1(s))





