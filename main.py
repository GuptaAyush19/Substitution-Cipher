# SUBSTITUTION ALGORITHM
# Author : Ayush Gupta
# Date Created : 26-12-2020

from KEY import KEY

alpha = "abcdefghijlkmnopqrstuvwxyz"
alphaU = alpha.upper()
KEY = KEY.lower()

# function to encrypt plain-text using substitution algorithm
def enrypt(text, key):
    keyU = key.upper()
    text = list(text)
    cipher = ""
    # we first convert the plain-text into a list of letters
    # and then compare it with the key list to encrypt
    for letter in text:
        if letter in alpha:
            cipher += key[alpha.index(letter)]
        elif letter in alphaU:
            cipher += keyU[alphaU.index(letter)]
        else:
            cipher += letter
    return "".join(cipher)

# function to decrypt substitution cipher
def decrypt(cipher, key):
    keyU = key.upper()
    cipher = list(cipher)
    text = ""
    # we first convert the cipher into a list of letters
    # and then compare it with the sorted english alphabet list to decrypt 
    for letter in cipher:
        if letter in alpha:
            text += alpha[key.index(letter)]
        elif letter in alphaU:
            text += alphaU[keyU.index(letter)]
        else:
            text += letter
    return "".join(text)
      
