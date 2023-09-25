""" Arithmetit logic """

# Asking for input
num1 = int(input("Enter a number: "))

# Preforming logic
if num1 > 12:
    print(num1 * 6)
else:
    num2 = int(input("Enter another number: "))
    if num2 > 6:
        print(num1 * num2)
    else:
        print(num1 + num2)
