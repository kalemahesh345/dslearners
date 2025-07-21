# Q1. Swap Two Numbers Without Using a Third Variable...



# a = int(input("Enter the first number a: "))
# b = int(input("Enter the second number b: "))
a=10
b=15


print(f"Before swapping: a = {a}, b = {b}")


a = a + b
b = a - b
a = a - b

print(f"After swapping: a = {a}, b = {b}")
