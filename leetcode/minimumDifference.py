## https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        if k == 1:
            return 0
        min_val = 100000
        for i in range(k - 1, len(nums)):
            sub = nums[i] - nums[i - k + 1]
            if sub < min_val:
                min_val = sub
        return min_val