# :closed_lock_with_key: jcrypt
A micro-wrapper for Python cryptography

## :books: About
This is a micro-wrapper for the Python [cryptography](https://cryptography.io/) library. Intended for small projects, it is meant to simplify basic start-up tasks (i.e. writing crypto functions) when using the standard Fernet recipe. 


Python [cryptography](https://cryptography.io/) is a *fantastic* library, but let's make it easier!    

## :old_key: Use
```python
import jcrypt


# Generate a random Fernet key:
key = jcrypt.get_key()


# Generate a Fernet key with password/salt (see note about salts):
key = jcrypt.get_key(password="lazydog", salt="salt")


# Encrypt a message:
msg = "Hello world!"
ciphertext = jcrypt.encrypt(gen_key, msg)


# Decrypt a message:
ciphertext = "gAAAAABi3V9...(etc.)"
ciphertext = jcrypt.decrypt(key, ciphertext)

```

## :salt: About Salts
From the [cryptography docs](https://cryptography.io/):
> *In this scheme, the salt has to be stored in a retrievable location in order to derive the same key from the password in the future.*

Arguably using a random salt (via os.urandom(16)) is safer, however, sharing/storage may be problematic and may not be easy for beginners. In this implementation the salt is essentially treated as a second password. 

## :mega: Shoutouts
- [cryptography](https://cryptography.io/). You never cease to amaze me.
- [Alex Gaynor](https://github.com/alex) for pushing me to do better. 


