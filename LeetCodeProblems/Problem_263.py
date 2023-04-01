"""An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number."""
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        factors = [2,3,5]
        for x in factors:
            while n % x == 0:
                n //= x
        return n == 1
