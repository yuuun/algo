### https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/
###wrong answer
from collections import defaultdict
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        ## transpose
        n = len(hats)
        person = defaultdict(list)
        for per in range(n):
            for hat in hats[per]:
                person[hat].append(per)
        keys = [*person.keys()]

        def dfs(peo, idx, ans):
            if len(peo) == n:
                return ans + 1
            for p in person[keys[idx]]:
                if p not in peo:
                    ans = dfs(peo + [p], idx + 1, ans)
            return ans
        return dfs([], 0, 0)
''' 시간 초과
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
'''


''' 다른 사람 풀이
def numberWays(self, hats: List[List[int]]) -> int:
        preferences = [[] for _ in range(41)]
        for person, pref in enumerate(hats):
            for h in pref:
                preferences[h].append(person)
            
        @lru_cache(None)
        def count_ways(i, used):
            if bin(used).count('1') == len(hats):
                return 1
            if i == 41:
                return 0
          
            ways = count_ways(i+1, used)
            for p in preferences[i]:
                if used & 1 << p == 0:
                    ways += count_ways(i+1, used | 1<<p) % big
            return ways % big
        
        return count_ways(0, 0)
'''