## https://leetcode.com/problems/reverse-string-ii/submissions/
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ''
        sign = -1
        for i in range(0, len(s), k):
            ans += s[i: i + k][::sign]
            sign *= -1
        return ans