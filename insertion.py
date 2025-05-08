two_d_array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]
print(two_d_array)

def search(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return "The value is located at index " + str(i) + " " + str(j)
            


    return "The element is not found"


print(search(two_d_array, 9))