# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/638/week-3-september-15th-september-21st/3978/
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        for c1, cnt in count1.items():
            if c1 in count2.keys():
                ans += [c1] * (min(count1[c1], count2[c1]))
        return ans