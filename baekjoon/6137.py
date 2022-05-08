from collections import deque
n = int(input())
s = deque()
for _ in range(n):
    s.append(input())
t = ''
while s:
    if s[0] > s[-1]:
        t += s.pop()
    else:
        t += s.popleft()
print(t)