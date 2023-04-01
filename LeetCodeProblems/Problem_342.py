"""Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x."""
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n!= 0 and n%4 == 0:
            n=n/4
        return n==1
