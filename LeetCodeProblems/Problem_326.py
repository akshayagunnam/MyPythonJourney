"""Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range (0, 31):
            if n == 3**i:
                return True
        else:
            return False
