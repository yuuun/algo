class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], nums[1]
        for i in range(2, len(dp)):
            dp[i] = nums[i] + max(dp[i-2], dp[i-3])
        return max(dp)