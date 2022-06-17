from collections import deque
def solution(s):
    stack = deque()
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    
    return 0 if stack else 1
        

print(solution('baabaa'), 1)
print(solution('cdcd'), 0)