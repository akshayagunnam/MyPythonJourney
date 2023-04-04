"""Given an integer number n, return the difference between the product of its digits and the sum of its digits."""
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        n = str(n)
        for i in n:
            product = product * int(i)
            sum = sum + int(i)
        return product - sum
