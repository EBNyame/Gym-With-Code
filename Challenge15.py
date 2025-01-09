# Iterate through a list of strings and print each string.
# Write a loop to count how many characters two strings have in common from the start.


words = ["apple", "banana", "cherry", "date", "elderberry"]
for word in words:
    print(word)


a = "apple"
b = "appstore"

def cc(s1, s2):
    count = 0
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            count += 1
        else:
            break
    return count


print(cc(a, b))