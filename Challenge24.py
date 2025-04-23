def most_freq(s):
    s = s.strip().lower()

    freq = {}

    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
        
    max_freq = max(freq, key=freq.get)
    return max_freq


# s = input("your word: ")

print(most_freq("Accomodation"))