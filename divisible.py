# Write a Python program to check if a number is divisible by both 3 and 5.

# a = 15
a = int(input("Enter your number: "))
if a % 3 == 0 and a % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")