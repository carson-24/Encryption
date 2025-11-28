import os
from dotenv import load_dotenv
import sys
from cryptography.fernet import Fernet

'''
Function encrpt( plaintext ):
 Overview
  - encrypt a message and return it
 Arguments
  - plaintext: string to be encrypted 
    NOTE: must be plain strings with no whitespace
 Returns
  - hash: encrypted message to be stored

'''
def encrypt(plaintext: str) -> str:
    # check that agruments passed correctly
    if str(plaintext).strip() is not plaintext:
        return 1

    secret = get_key()

    # create a encryption tool
    f_obj = Fernet(secret)

    # create a has with the message
    b_message = plaintext.encode('utf-8')
    hash = f_obj.encrypt(b_message)

    return hash.decode('utf-8')

'''
Function: decrypt ( hash ):
 Overview
  - decrypt a hash and return it
 Arguments
  - hash: stored hash made from secret and plaintext
 Returns
  - plaintext message stored originally
'''
def decrypt(hash: str) -> str:
    # get key to decrpyt message
    secret = get_key()

    # create a cyrptic object
    f_obj = Fernet(secret)

    # return message
    b_message = f_obj.decrypt(hash)
    return b_message.decode('utf-8')



'''
Function: get_key()
 Overview
 - get the key stored locally
 Returns
 - Fernet encryption key
'''
def get_key() -> bytes:
    # load the local encryotion secret
    load_dotenv()
    secret = os.getenv('FERNET_KEY')
    return secret.encode('utf-8')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit(1)
    if sys.argv[1] == 'encrypt':
        print("encryption: ", encrypt(sys.argv[2]))
    elif sys.argv[1] == 'decrypt':
        print("decryption: ", decrypt(sys.argv[2]))
    elif sys.argv[1] == 'getkey':
        print("key: ", get_key().decode('utf-8'))