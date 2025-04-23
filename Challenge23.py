# Write a function to return the first non-repeating character in a string:

def non_repeating(word):
    for char in word:
        if word.count(char) == 1:
            return char
    return None
non_repeating("banana")

#.............................CONTINUE LATER.........................