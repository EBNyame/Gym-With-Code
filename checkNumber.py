#Check if a number is positive, negative, or zero.

number = int(input("Number: "))

if number < 0:
    print("Negative")
elif number == 0:
    print("Zero")
else:
    print("Positive")