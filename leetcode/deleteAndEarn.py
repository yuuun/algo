class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        sum_nums = [0] * (max(nums) + 1)
        for num in nums:
            sum_nums[num] += num
        
        dp = [0] * (max(nums) + 1)
        for idx, cnt in enumerate(sum_nums[:-1]):
            dp[idx + 1] += max(dp[idx - 1], dp[idx - 2]) + sum_nums[idx + 1]
            
        return max(dp[-1], dp[-2])