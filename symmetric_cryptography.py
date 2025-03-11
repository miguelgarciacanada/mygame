#Program that encrypts and decrypts a text
#Taken from: https://snyk.io/blog/using-python-libraries-for-secure-network-communication/
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import base64

# Generate a random password for the key
password = b'123456'


# Generate a salt
salt = os.urandom(16) #a salt is just random data that you use as additional input into your hash to make it harder to “unhash” your password. It protects your password from dictionary attacks 


# Derive a key from the password using PBKDF2
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000
)

key = base64.urlsafe_b64encode(kdf.derive(password))


# Create a Fernet cipher using the key
cipher = Fernet(key) #The Fernet module implements an easy-to-use authentication scheme that uses a symmetric encryption algorithm


# Encrypt a message
encrypted_message = cipher.encrypt(b"Hello, world!")  #The b letter indicates that the text will be used as byte type


# Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message)
print(decrypted_message)
