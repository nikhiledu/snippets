#!/usr/bin/env python
import base64, hashlib, os, sys
from base64 import urlsafe_b64encode as encode

def hashed_password(uid):
    #password = base64.b64encode(hashlib.sha256(uid.encode()).digest())
    password = '1234'
    salt = os.urandom(4)
    sha = hashlib.sha1(password)
    sha.update(salt)
    digest_salt_b64 = '{}{}'.format(sha.digest(), salt).encode('base64').strip()
    return '{{SSHA}}{}'.format(digest_salt_b64)

print(sys.argv[1])
print(hashed_password(sys.argv[1]))
