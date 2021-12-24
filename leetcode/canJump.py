# https://leetcode.com/problems/jump-game/discuss/1640470/Python3-Easy-to-Understand
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        
        curr = 0
        for i in range(len(nums)):
            curr = max(nums[i], curr-1)
            if curr == 0 and i != len(nums) - 1:
                return False
        return True