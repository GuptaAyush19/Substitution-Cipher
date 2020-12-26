# TEST FOR <MAIN.PY> PYTHON PROGRAM
# Author : Ayush Gupta
# Date Created : 26-12-2020

import random
import main

random.seed(10)

# function to generate a random word having 10 letters
def randomStr():
    n = ""
    for i in range(10):
        n += main.alphaU[random.randint(0, len(main.alphaU)-1)]
    return n

for i in range(100):
    # compare the original plain-text with the decrypted encrypted cipher text
    # of the original plain-text to check the symmetry of the algorithm
    text = randomStr()
    cipher = main.enrypt(text, main.KEY)
    decText = main.decrypt(cipher, main.KEY)
    if decText != text:
        # if the symmetry breaks, then it means that there is some
        # problem with <main.py> python program
        print("noob")
        break
    
print("done", end="")