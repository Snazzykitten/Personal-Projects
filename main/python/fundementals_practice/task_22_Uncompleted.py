""" Storing a looping sequence """

# Asking for input
num1 = int(input("Enter a number: "))

# Defining a empty list to store
numbers = []
a = 0

# Looping
for i in range(0, num1):
    numbers.append(i+1)

#print(list)
print(sum(numbers))
