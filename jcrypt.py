import base64
# import os # for random salts (but remember you can't regenerate the key later without the same salt!)
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def get_key(**kwargs):
    if kwargs == {}:
        key = Fernet.generate_key()
    else:
        #salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=(kwargs["salt"]).encode(),  # for random salt use os.urandom(16)
            iterations=390000,
        )
        key = base64.urlsafe_b64encode(kdf.derive((kwargs["password"]).encode()))
    return key


def encrypt(key, data):
    f = Fernet(key)
    token = f.encrypt(data.encode())
    return token.decode()


def decrypt(key, token):
    f = Fernet(key)
    cleartext = f.decrypt(token.encode())
    return cleartext.decode()
