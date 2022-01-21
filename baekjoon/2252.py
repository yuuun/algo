# 위상 정렬: 순서가 정해져 있는 작업
from collections import deque
n, m = map(int, input().split())

height = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    indegree[b] += 1
    height[a].append(b)
    
q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)
        
while q:
    a = q.popleft()
    print(a, end=' ')
    for b in height[a]:
        indegree[b] -= 1
        if indegree[b] == 0:
            q.append(b)