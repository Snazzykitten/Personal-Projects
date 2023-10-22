""" Number guessing game """

# Importing libraries
import random

# Generating a random number
num1 = random.randint(1,10)

# Asking for input
user = int(input("Guess a number (1-10): "))

# Preforming logic
if user == num1:
    print("Correct!")
else:
    print("Not what i was thinking of.")
