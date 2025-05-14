numbers = 1, 2, 3, 4
list1 = list(numbers)
print(list1)
list1.extend([10,11])
print(list1)


n_list = list(())
print(n_list)

n = n_list.copy()
print(n)

n.extend([1,2,3,3])
print(n)

n.remove(3)
print(n)

sum = n + list1
print(sum)

sum.sort()
print(sum)

sorted_sum = sorted(sum, reverse=True)
print(sorted_sum)