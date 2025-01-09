# Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.
def percentage(word, letter):
    countLetter = word.count(letter)
    totalLetters = len(word)
    percentage = (countLetter / totalLetters) * 100
    return int(percentage)


print(percentage('Hello World', 'o'))  