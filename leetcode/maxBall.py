##  https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/637/week-2-september-8th-september-14th/3973/
# from collections import Counter
from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count_dict1 = defaultdict(int)
        count_dict2 = defaultdict(int)
        for t in text:
            if t in ['l' , 'o']:
                count_dict1[t] += 1
            if t in ['a', 'b', 'n']:
                count_dict2[t] += 1

        min_val1 = 0 if len(count_dict1) == 0 else min(count_dict1.values()) // 2
        min_val2 = 0 if len(count_dict2) == 0 else min(count_dict2.values())
        
        return min(min_val1, min_val2)

ball = Solution()
print(ball.maxNumberOfBalloons('loonbalxballpoon'))