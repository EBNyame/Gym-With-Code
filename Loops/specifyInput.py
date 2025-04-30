# Write a program to classify a character as vowel, consonant, digit, or special character.


def specify(word):
    for char in word:
        if char.lower() in 'aeiou':
            print(f"{char} is Vowel")

        elif char.isalpha():
            print(f"{char} is Consonant")

        elif char.isdigit():
            print(f"{char} is Digit")

        else:
            print(f"{char} is a special character")

specify("Ghana@50")