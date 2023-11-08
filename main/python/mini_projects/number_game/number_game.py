""" Number game """

# -------------------
# Importing libraries
# -------------------
import random
import os
from time import sleep

#-------------------
# Creating classes
# ------------------

# Color formatting
class colors:   
      red = '\033[31m'
      green = '\033[32m'
      blue = '\033[34m'
      yellow = '\033[93m'

# Terminal functions
class tty:
      clear = os.system('clear')

# Errors
class error:
      null = "ERROR: field is blank"
      rangein = "ERROR: value out of bounds"
      datatype = "ERROR: data type must be integer"


# -------------------
# Subprograms
# -------------------
def guess():
      
      print(colors.yellow, 'Please enter your guess')


      try:
            guessed = input(" ( > ) ").format(int)
            return guessed
      except ValueError:
            print(colors.red, "ERROR: TypeError")
            for i in 5:
                  print(colors.red, "Restarting in", (5-i))
            guess()
            


      # Filtering user input to handle exceptions

#      if str.strip(guessed) != (""): # Checking for blank fields
#
#           try: # Checking if input is integer
#                guessed = int(guessed) 
#
#            except ValueError: 
#                  print(colors.red, error.datatype)  
#                  guess()
#
#            finally: # Checking if input is within range
#                  if guessed > 100 or guessed < 1:
#                        print(colors.red, error.rangein)
#                        guess()
#                  
#                  else: # Returning filtered value
#                        return guessed
#            
#      else:
#            print(colors.red, error.null)
#            guess()



# -------------------
# Main program
# -------------------

# Preforming system functions
tty.clear

# Intro
print(colors.blue, "Welcome to the number guessing game!")
print(colors.blue, "Guess the number I am thinking of. It is between 1-100.")
print(colors.blue, "I will give you clues after your first guess.")

random = random.randint(1,100)

# Defining num guessed before the while loop as the use only
# difines it once the guess function is called
num_guessed = 0
guesses = 0

while num_guessed != random:
      
      num_guessed = guess()
      guesses += 1

      if int((num_guessed)) < random:
            print(colors.red, "Guess higher")
            
      elif int((num_guessed)) > random:
            print(colors.red, "Guess lower")
      else:
            print(colors.green, "You guessed the number in", guesses, "guesses!")
            print()
