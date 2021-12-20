# https://leetcode.com/problems/fibonacci-number/
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 2 or n == 1:
            return 1
        a, b = 1, 1
        while n > 2:
            a, b = b, a + b
            n -= 1
        return b