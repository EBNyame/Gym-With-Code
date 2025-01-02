def reversedString(s):
    reversedString = ""
    for char in s:
        reversedString = char + reversedString
    return reversedString

print(reversedString("man"))