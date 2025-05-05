"""

Problem: Sum of Digits
Write a recursive function sum_of_digits(n) that calculates the sum of the digits of a given number n.

Example:

Input: n = 123

Output: 1 + 2 + 3 = 6

"""

def sum(n):
    assert n >= 0 and int(n) == n, "The number has to be positive integer only"

    if n == 0:
        return 0
    
    else:
        return int(n % 10)  + sum(int(n / 10))
    

print(sum(1234))