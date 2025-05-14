names = ["Ko", "Eve", "Ami"]


for i, name in enumerate(names):
    print(f"Index: {i}, Name: {name}")


nums = [2, 4 ,7, 89, 3, 5, 6]

ex = [num for num in nums if num % 2 == 0]
print(ex)

sx = ["even" if num % 2 == 0 else "odd" for num in nums]
print(sx)

my = [[0]] * 5
print(my)

my[0] = 1
print(my)

my[0][0] = 1
print(my)