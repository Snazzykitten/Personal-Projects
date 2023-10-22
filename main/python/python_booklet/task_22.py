""" Storing a looping sequence """

# Asking for input
num = int(input("Enter a number: "))

# Looping
for i in range(1, num):
    num = num * i

print(num)
