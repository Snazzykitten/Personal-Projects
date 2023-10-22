""" Am i bob """

# Asking for input
name = input("Enter your name: ")

# Preforming logic
if name == "Bob":
    num1 = int(input("Enter a number: "))
    if num1 < 5:
        print("Correct")
else:
    print("Incorrect")