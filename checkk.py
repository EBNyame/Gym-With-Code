numbers = [10, 3, 55, 33, 2, 1, 5, 9]



def check(array, index):
    if index >= len(array):
        print("Be serious...")

    else:
        print(array[index])

user_input = 8
check(numbers, user_input)