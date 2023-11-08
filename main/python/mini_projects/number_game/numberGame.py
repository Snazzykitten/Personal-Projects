# ===============================================
# Number Guessing Game
# ===============================================
# This game will ask the user to guess the secret
# number, if you guess incorrectly, the game will
# check for exeptions, and give you a hint after 
# the first guess.

# ===============================================
# Importing libraries
# ===============================================
import random
import os
from time import sleep

# ===============================================
# Creating variables
# ===============================================
# Constants
# -----------------------------------------------
RANDOM_NUM = random.randint(1, 100)

# ===============================================
# Creating classes
# ===============================================
# ANSI escape escape sequences
# -----------------------------------------------
class Pretty:
    error = '\033[31m'
    correct = '\033[32m'
    default = '\033[93m'
    question = '\033[34m'

# ===============================================
# Microprograms
# ===============================================
# Pretty print function
def right_print(txt):
    print('\033[32m'.format(txt))
def except_print(txt):
    print('\033[31m'.format(txt))
def reg_print(txt):
    print('\033[93m'.format(txt))
# -----------------------------------------------
# System control function
def clear():
    os.system(clear)

def intro():
    reg_print("Welcome to the number guessing game!")
    reg_print("You must guess a random value between 'x-y'.")

    X = input("Enter x: ")
    Y = input("Enter y: ")

    for i in 5:
        print(Colors.fg.yellow)

def guess():
    """ To process input of user's integer to a set criteria. """

    #--------------------------------------------
    reg_print(txt)"")

# ===============================================
# Mainprogram
# ===============================================
def main():
    """ The primary function to run the program. """

    intro()

    num_guessed = 0
    amount_guessed = 0

    while num_guessed != RANDOM_NUM:

        num_guessed = guess()
        amount_guessed += 1

main()
