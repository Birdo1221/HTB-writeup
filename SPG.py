import string
import random
from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

ALPHABET = string.ascii_letters + string.digits + '~!@#$%^&*'

def generate_password():
    master_key = int.from_bytes(MASTER_KEY, 'little')
    password = ''

    while master_key:
        bit = master_key & 1
        if bit:
            password += random.choice(ALPHABET[:len(ALPHABET)//2])
        else:
            password += random.choice(ALPHABET[len(ALPHABET)//2:])
        master_key >>= 1

    return password

def crack_password(password):
    master_key = 0

    for i, p in enumerate(password):
        if p in ALPHABET[:len(ALPHABET) // 2]:
            master_key |= 1 << i

    return master_key.to_bytes((7 + len(password)) // 8, 'little')

def main():
    password = 't*!zGnf#LKO~drVQc@n%oFFZyvhvGZq8zbfXKvE1#*R%uh*$M6c$zrxWedrAENFJB7xz0ps4zh94EwZOnVT9&h'
    ciphertext = 'GKLlVVw9uz/QzqKiBPAvdLA+QyRqyctsPJ/tx8Ac2hIUl8/kJaEvHthHUuwFDRCs'
    MASTER_KEY = crack_password(password)
    encryption_key = sha256(MASTER_KEY).digest()
    cipher = AES.new(encryption_key, AES.MODE_ECB)

    decrypted_flag = unpad(cipher.decrypt(b64decode(ciphertext)), AES.block_size).decode()
    print("Decrypted Flag:", decrypted_flag)

if __name__ == "__main__":
    main()
