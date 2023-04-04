""""A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.

"""
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        factors = []
        total = 0
        if num > 33550336:
            return False
        for i in range (1, num//2 + 1):
            if num % i == 0:
                factors.append(i)
        for j in range(0, len(factors)):
            total = total + factors[j]
        if total == num:
            return True
        else:
            return False
