# Write a function that returns the first and last item in a tuple

def tuple(t):
    first = t[0]
    last = t[-1]

    print(f"the first item is {first} and the last item is {last}")

t = (2, 4, 5, 6)
tuple(t)