def FindMax(array):
    maximumNumber = float('-inf')
    for value in array:
        if value > maximumNumber:
            maximumNumber = value
    return maximumNumber


