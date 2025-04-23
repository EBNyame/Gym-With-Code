# Write a function that checks if a number is even or odd:

def check(a):
    if a % 2 == 0:
        print(f"{a} is a even number")
    else:
        print(f"{a} is a odd number")

check(int(input("Enter a number: ")))