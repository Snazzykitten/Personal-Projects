""" Product increase / decrease """

# Asking for a number
price = float(input("Enter a products price: "))

# Preforming logic
if price > 50.0:
    print(price * 0.95)
else:
    print(price * 1.02)