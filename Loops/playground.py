# this is just a playground

# data_points = 6
# count = 0
# while count < data_points:
#     print(count)
#     count += 1

# else:
#     print("Loop is Over")


def recursion_method(n):
    if n < 1:
        print("n is less than one")
    else:
        recursion_method(n-1)
        print(n)



recursion_method(4)