arr = [2, 5, 6, 8, 33, 9]
arr.remove(max(arr))
print(arr)
arr.pop()
print(arr)


def search(array, lookup):
    for i in array:
        if i == lookup:
            return array.index(lookup)
    
    return "Lamar stop fooling"


print(search(arr, 88))