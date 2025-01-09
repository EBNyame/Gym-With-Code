# Write a program to extract the first 3 characters of a string.
# Compare two strings and check if one starts with the other.

word = "Exodus"
extract3 = word[:3]
print(extract3)


# Compare two strings
if extract3 in word:
    print(bool(extract3))