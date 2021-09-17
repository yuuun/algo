### https://leetcode.com/problems/number-of-equivalent-domino-pairs/submissions/
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = [[] for _ in range(len(dominoes))]
        visited = [False] * len(dominoes)
        
        for idx1, domin in enumerate(dominoes):
            i_a, i_b = domin
            for idx2 in range(idx1 + 1, len(dominoes)):
                if visited[idx1]:
                    break
                j_a, j_b = dominoes[idx2]
                if (i_a == j_a and i_b == j_b) or (i_a == j_b and i_b == j_a):
                    for an in ans[idx1]:
                        ans[an].append(idx2)
                    ans[idx1].append(idx2)
                    visited[idx2] = True
        cnt = 0
        for an in ans:
            cnt += len(an)
        return cnt


## 위는 시간이 매우 많이 소요한다.
'''
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = {}
        cnt = 0
        for a, b in dominoes:
            key = min(a, b) * 10 + max(a, b) 
            if key in d:
                cnt += d[key] # the number of dominoes already in the map is the number of the newly found pairs.
                d[key] += 1
            else:
                d[key] = 1   
        return cnt
'''