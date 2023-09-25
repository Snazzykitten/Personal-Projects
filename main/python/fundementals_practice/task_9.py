""" Random num addition """

# Importing libraries
import random

# Asking for numbers
num1 = float(input("Enter a number: "))
num2 = random.randint(1,20)

# Preforming calculations
ans1 = num1 + num2
ans2 = num1 * num2

# Printing answers
print(ans1, ans2)
