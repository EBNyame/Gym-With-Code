# Write a function that takes two strings and returns the first common character.
def TCC(s1, s2):
    for char in s1:
        if char in s2:
            return char
    return None


print(TCC('apple', 'banana'))