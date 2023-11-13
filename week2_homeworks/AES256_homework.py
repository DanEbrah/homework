'''
AES256 get the right library
create key and save it
create test string for encryption

'''
from Crypto.Cipher import AES
import os
from Crypto.Util.Padding import pad, unpad


def generate_key(): # function for generating key
    len = 32 #32 bytes long
    global symm_key # global var so it can be used in other functions
    symm_key = os.urandom(len) #generate with the len
    with open('symm_key.bin', 'wb') as e: # open with binary format / write
        e.write(symm_key)

def encrypt_with_key():
    global plaintext
    global cipher_text

    with open('symm_key.bin', 'rb') as e: #
       e.read()
    
    cipher = AES.new(symm_key, AES.MODE_EAX)

    plaintext = b"Testing this plain text"


    cipher_text = cipher.encrypt(plaintext)
    print(f"encrypted! {cipher_text}")

def decrypt_with_key():
    with open('symm_key.bin', 'rb') as e:
        e.read()
        global decrypted
    
  
    cipher = AES.new(symm_key, AES.MODE_EAX)
    decrypted = cipher.decrypt(cipher_text)
    print(f"decrypted! {decrypted}")

  
    
generate_key()
encrypt_with_key()
print("\n")
decrypt_with_key()

assert cipher_text == plaintext
