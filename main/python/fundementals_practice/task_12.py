""" Calculate monthly phone bill """

# Assigning global var
STANDING_FEE = 10.00

# Assigning rate of charge
per_minute = 0.10
per_text = 0.05

# Asking for numbers
minutes = float(input("How many minutes have you used this month? "))
texts = float(input("How many texts have you sent this month? "))

# Preforming  calculations
minutes_fee = minutes * per_minute
texts_fee = texts * per_text
total = STANDING_FEE + minutes_fee + texts_fee

# Printing answer
print(total)
