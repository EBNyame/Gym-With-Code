def palindrome(x):
    if x < 0:
        return False
    
    converted_x = str(x)

    if converted_x == converted_x[::-1]:
        return True
    else:
        return False
    
print(palindrome(121))