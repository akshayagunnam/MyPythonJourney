"""ou are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?"""
class Solution:
        def climbStairs(self, n: int) -> int:
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            x = 2
            y = 3 
            for i in range(n-3):
                y, x = y + x, y
            return y
        
