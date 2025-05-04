# Sum of numbers
# Prompt the user to enter positive numbers. Add them until the user enters a negative number, then print the sum.

def sum():
    user_value = int(input("Value: "))
    count = 0
    total = 0
    while user_value >= 0:
        total += user_value

    print(total)


sum()