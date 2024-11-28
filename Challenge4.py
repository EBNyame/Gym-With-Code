# Write a Python program to swap two variables.
a = input("Enter a value for a: ")
b = input("Enter a value for b: ")
print(f"this is the initial value for a: {a} and b: {b}")

# swap
temp = a
a = b
b = temp

print(f"now a is {a} and b is {b}")