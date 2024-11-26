# Write a Python program to do arithmetical operations addition and division.
# ........................addition aspects..........................
FirstNumber = float(input("Enter the first number: "));
SecondNumber = float(input("Enter the second number: "));
SumUp1 = FirstNumber + SecondNumber

print(f"{FirstNumber} + {SecondNumber} = {SumUp1}")



# ........................division aspects..........................
numberA = float(input("Enter the first number: "))
numberB = float(input("Enter the second number: "))

if numberB == 0:
    print("Error: Division by zero is invalid.")

divide = numberA / numberB
print(f"{numberA} divied by {numberB} = {divide}")