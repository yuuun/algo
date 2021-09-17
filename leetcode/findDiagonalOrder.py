### https://leetcode.com/problems/diagonal-traverse-ii/submissions/
### time limit
'''
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        r = len(nums)
        tot = 0
        for num in nums:
            c_len = len(num)
            tot += c_len
                
        row, col = 1, 0
        ans = [nums[0][0]]
        while len(ans) < tot:
            while row != -1:
                if -1 < row and row < r:
                    if col < len(nums[row]):
                        ans.append(nums[row][col])
                    
                row -= 1
                col += 1
            row = col
            col = 0
            
        return ans
'''
from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        dictionary = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                dictionary[i + j].append(nums[i][j])
        return [v for k in dictionary.keys() for v in reversed(dictionary(k))]