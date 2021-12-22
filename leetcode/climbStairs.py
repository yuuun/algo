class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        a, b = 1, 1
        while n > 1:
            a, b = b, a + b
            n -= 1
        return b