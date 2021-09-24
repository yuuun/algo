## https://leetcode.com/problems/find-pivot-index/submissions/
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums[1:])
        piv = 0
        while True:
            if left == right:
                return piv  
            if piv == len(nums) - 1:
                return -1
            
            left += nums[piv]
            piv += 1
            right -= nums[piv]
        
        return piv