### https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/
###시간 초과ㅠㅠ
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats)
        def dfs(hat, idx, ans):
            if idx == n:
                return ans + 1
            for h in hats[idx]:
                if h not in hat:
                    ans = dfs(hat + [h], idx + 1, ans)
            return ans
        return dfs([], 0, 0)