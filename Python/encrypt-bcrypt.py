#!/usr/bin/env python
import bcrypt

salt = bcrypt.gensalt(10)
salt2 = 'jhgjkhkjhjkhkjhkjhkjh'
hashed = bcrypt.hashpw('Nikh1'.encode('utf-8'), salt2)
print(salt)
print(hashed)

if bcrypt.hashpw('Nikh1l'.encode('utf-8'), hashed) == hashed:
    print("It matches")
else:
    print("It does not match")

