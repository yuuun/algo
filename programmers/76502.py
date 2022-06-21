from collections import deque
def solution(s):
    cnt = 0
    s = deque(s)
    for _ in range(len(s)):
        s.rotate()
        stack = deque()
        for i in s:
            if stack:
                if i == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        stack.append(i)
                elif i == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        stack.append(i)
                elif i == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
            else:
                stack.append(i)
            
        if len(stack) == 0:
            cnt += 1
    return cnt
print(solution("[](){}"), 3)