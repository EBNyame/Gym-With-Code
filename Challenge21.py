#Check if all elements of list A are in list B.

a = [2, 3, 4, 6]
b = [2, 6]

check = all(item in a for item in b)
for a in b:
    print(a)
print(check)
