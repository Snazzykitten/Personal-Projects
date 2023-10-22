""" Automatic test grading scheme """

# Asking for scores
score = int(input("Enter the users score: "))

# Preforming logic
if score > 89:
    print("A*")
elif score > 79:
    print("A")
elif score > 69:
    print("B")
elif score > 50:
    print("C")
else:
    print("Fail")
    