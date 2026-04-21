///70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps///


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        else:
            a = 1
            b = 2
            for i in range(3,n+1):
                a, b = b , a + b
        return b        


# Fibonacci sequence pattern:

# ways(n) = ways(n-1) + ways(n-2)
# can also be done like
    
        # return  self.climbstairs(n-2) + self.climbstairs(n-2)
