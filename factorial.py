# factorial

def factorial(n):
    assert n >= 0 and int(n) == n; "Only positive integers are allowed"
    if n in [0, 1]:
        return 1
    
    return n * factorial(n - 1)