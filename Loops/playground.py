# this is just a playground

# data_points = 6
# count = 0
# while count < data_points:
#     print(count)
#     count += 1

# else:
#     print("Loop is Over")


# def recursion_method(n):
#     if n < 1:
#         print("n is less than one")
#     else:
#         recursion_method(n-1)
#         print(n)



# recursion_method(4)




# def ah(s):
#     start = 0
#     end = len(s) - 1

    
#     for char in s:
#         print(int(char))


# print(ah("101"))


# n = 10

# k = 2
# # ok = []
# # ok = [x for x in range(1, n, k)]

# # print(ok)

# l = []
# for i in range(1, n + 1, k):
#     print(i)
#     # L = list(i)/'
#     # print(L)
#     l.append(i)
#     print(l)


a = [1,4,0,2,0,0]

for i in range(len(a)- 1):
    if a[i] == 0:
        a[i], a[i + 1] = a[i + 1], a[i]

print(a)