import hashlib, os
from base64 import urlsafe_b64encode as encode
from base64 import urlsafe_b64decode as decode

def makeSecret(password):
    salt = os.urandom(4)
    h = hashlib.sha1(password)
    h.update(salt)
    return "{SSHA}" + encode(h.digest() + salt)

def checkPassword(challenge_password, password):
    challenge_bytes = decode(challenge_password[6:])
    digest = challenge_bytes[:20]
    salt = challenge_bytes[20:]
    hr = hashlib.sha1(password)
    hr.update(salt)
    return digest == hr.digest()

challenge_password = makeSecret('testing123')
checkPassword(challenge_password, 'testing123')
