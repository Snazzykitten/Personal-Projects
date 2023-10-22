""" Countdown enter """

# Asking for input
loops = int(input("Enter a number: "))

# Preforming logic
for loop in range(loops):
    key_pressed = input("")
    if key_pressed == "":
        print(loops - loop)
