# Check if a number is positive, negative, or zero.


def check(number):
    if number < 0:
        print("Negative number")

    elif number == 0:
        print("Zero")

    else:
        print("Positive number")


number = int(input("Number: "))
check(number)