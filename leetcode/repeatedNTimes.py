class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        ex = set()
        for i, n in enumerate(nums):
            ex.add(n)
            if len(ex) != (i + 1):
                return n
                break
