two_d_array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]

print(two_d_array[0][3])

for i in range(len(two_d_array)):
    
    two_d_array.remove(two_d_array[0])

    print(two_d_array)