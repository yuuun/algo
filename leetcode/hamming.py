# https://leetcode.com/problems/hamming-distance/submissions/
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        plus = str(int(bin(x)[2:]) + int(bin(y)[2:]))
        
        ans = 0
        for s in plus:
            if s == '1':
                ans += 1
        
        return ans

        ## return bin(x^y).count('1')
        '''
        r = 0
        while x or y:
            r += (x & 1) != (y & 1)
            x >>= 1
            y >>= 1
        return r
        '''