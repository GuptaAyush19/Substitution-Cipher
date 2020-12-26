# ENCRYPTING OR DECRYPTING FILE
# Author : Ayush Gupta
# Date Created : 26-12-2020

import main

# user input for mode
mode = input("DO YOU WANT TO (E)NCRYPT OR (D)ECRYPT <text-file.txt> FILE? ").lower()

# encrypting
if mode.startswith("e"):
    # read the contents from the file
    fileR = open("text-file.txt", "r")
    text = fileR.read()
    fileR.close()
    # creating cipher text using substitution algorithm
    cipher = main.enrypt(text, main.KEY)
    fileW = open("text-file.txt", "w")
    fileW.write(cipher)
    fileW.close()
    print("SUCCESS!",end="")    

# decrypting
elif mode.startswith("d"):
    # read the contents from the file
    fileR = open("text-file.txt", "r")
    cipher = fileR.read()
    fileR.close()
    # decrypting cipher text using substitution algorithm
    text = main.decrypt(cipher, main.KEY)
    fileW = open("text-file.txt", "w")
    fileW.write(text)
    fileW.close()
    print("SUCCESS!",end="")

# unvalid user input
else:
    print("Not a valid input, terminated . . .", end="")
    
    