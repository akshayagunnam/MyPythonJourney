"""Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt."""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range (100000):
            if i*i == num:
                return True
        else:
            return False
