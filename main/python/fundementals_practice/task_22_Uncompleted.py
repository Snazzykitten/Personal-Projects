""" Storing a looping sequence """

# Asking for input
num1 = int(input("Enter a number: "))

# Defining a empty list to store
numbers = []

# Looping
for i in range(1, num1 + 1):
    numbers.append(i)
    
print(numbers)
ans = numbers.index(2)
#print(list)
for num in range(1, num1):
    ans = (ans * numbers.index(num))
    print(ans)