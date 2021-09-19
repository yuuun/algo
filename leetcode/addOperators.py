
## https://leetcode.com/problems/expression-add-operators/discuss/1467079/Python-Solution-using-Backtracking

## solution: https://leetcode.com/problems/expression-add-operators/discuss/1467079/Python-Solution-using-Backtracking
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def backtracking(i, prev, curr, n, path=[]):    
            # base case
            if i == len(num):
                if n == target and curr == 0:
                    output.append("".join(path[1:]))
                return
            curr = 10 * curr + ord(num[i]) - ord("0")
            if curr > 0:
                # no insert
                backtracking(i+1, prev, curr, n, path)
            # add
            backtracking(i+1, curr, 0, n+curr, path+["+", str(curr)])
            
            
            if path:
                # substract
                backtracking(i+1, -curr, 0, n-curr, path+["-", str(curr)])
                
                # multiply
                backtracking(i+1, prev*curr, 0, n-prev+curr*prev, path+["*", str(curr)])
            
                    
        output = []
        backtracking(0, 0, 0, 0)
        return output