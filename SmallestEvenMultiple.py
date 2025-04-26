# Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 1:
            return n * 2
        else:
            return n