def power(base, y):
    assert y >= 0 and int(y) == y, "The exponent must be positive integer only"
    if y == 0:
        return 0
    if y == 1:
        return base
    return base * power(base, y - 1)

print(power(2,-3))    