## https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/638/week-3-september-15th-september-21st/3977/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r, c = len(matrix) - 1, len(matrix[0])
        # ans = [[0] * c for _ in range(r + 1)]
        cnt = 1
        row = 0
        col = -1
        trans = 1
        tot = (r + 1) * c
        ans = []
        while cnt <= tot:
            for i in range(c):
                col += trans
                ans.append(matrix[row][col])
                cnt += 1
            c -= 1
            for i in range(r):
                row += trans
                ans.append(matrix[row][col])
                cnt += 1
            r -= 1
            trans *= -1
            
        return ans