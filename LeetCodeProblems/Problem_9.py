#Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        reverse = x[::-1]
        if x == reverse:
            return True
        else:
            return False
