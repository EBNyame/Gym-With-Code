print("Create an array and traverse.")

# 1. Create an array and traverse.
from array import *

arr = array('i', [1, 4, 3, 6, 6, 8])

for i in arr:
    print(i)


print("Access individual elements through indexes")
# 2. Access individual elements through indexes
for i in range(len(arr)):
    print(arr[i])


print("Append any value to the array using append() method")
# 3. Append any value to the array using append() method
arr.append(2)
print(arr)


print("Insert value in an array using insert() method")
# 4. Insert value in an array using insert() method

arr.insert(3, 10)
print(arr)


print("Extend python array using extend() method")
# 5. Extend python array using extend() method

arr2 = array('i', [1, 2, 3, 4, 5])
arr.extend(arr2)
print(arr)


print("Add items from list into array using fromlist() method")
# 6. Add items from list into array using fromlist() method

my_list = [12, 33, 55]
arr.fromlist(my_list)
print(arr)


print("Remove any array element using remove() method")
# 7. Remove any array element using remove() method
arr.remove(1)
print(arr)


print("Remove last array element using pop() method")
# 8. Remove last array element using pop() method
arr.pop()
print(arr)


print("Fetch any element through its index using index() method")
# 9. Fetch any element through its index using index() method
fetch = arr.index(8)
print(fetch)


print("Reverse a python array using reverse() method")
# 10. Reverse a python array using reverse() method
arr.reverse()
print(arr)


print("Get array buffer information through buffer_info() method")
# 11. Get array buffer information through buffer_info() method
baf = arr.buffer_info
print(baf)


print("Check for number of occurrences of an element using count() method")
# 12. Check for number of occurrences of an element using count() method
s = arr.count(6)
print(s)


