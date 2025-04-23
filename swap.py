#Input two numbers and swap them without using a third variable.

name = int(input("Enter your name: "))
age = int(input("Enter your age: "))
name, age = age, name


print(f"Now your name is {age} and your age is {name}")