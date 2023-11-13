
# imports from pycryptodome except binascii
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
import binascii
from Crypto.Hash import SHA256


#glob_data_list = []

def generate_key():
    global pair_key # set global to use other functions
    pair_key = RSA.generate(bits= 2048) #generating both private and public key at once

    
# this function signs the message = "message", it is also printing the signature after running.
def sign_message():
    global message, hash, signer, sig # set global to use other functions
    message = b"sign message"
    hash = SHA256.new(message)
    signer = PKCS115_SigScheme(pair_key)
    sig = signer.sign(hash)
    
    print(f"Signature is {binascii.hexlify(sig)}")


# this function verifys the message, to see if it matches the signed message and if it does then "valid signature" will be printed
def verify_validation():
    message= b"sign message"
    hash = SHA256.new(message)
    signer = PKCS115_SigScheme(pair_key)
    
    try:
        signer.verify(hash, sig)
        print("Valid signature")
    except:
        print("Invalid Signature")

'''
#*THIS PART IS COMMENTED OUT AS IT IS NOT IN HOMEWORK REQUIREMENTS, for my own learning*
#this function is testing the invalid return, it is tested with another message entered
def invalid_verification():
    message = b"testing a different message for invalid text"
    hash = SHA256.new(message)
    signer = PKCS115_SigScheme(pair_key)
    try:
        signer.verify(hash, sig)
        print("Valid signature")
    except:
        print("Invalid Signature") '''

#calling all functions for running
generate_key()
sign_message()
verify_validation()

