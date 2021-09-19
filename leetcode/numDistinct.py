class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ans = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
        for i in range(len(s) + 1):
            ans[0][i] = 1
            
        for i, ti in enumerate(t):
            for j, si in enumerate(s):
                if ti == si:
                    ans[i + 1][j + 1] = ans[i][j] + ans[i + 1][j]
                else:
                    ans[i + 1][j + 1] = ans[i + 1][j]
        return ans[-1][-1]