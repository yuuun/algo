#TBD
from collections import deque
k = int(input())

def bfs(s):
    visited[s] = 1
    q = deque()
    q.append(s)
    while q:
        a = q.popleft()
        for i in adj[a]:
            if visited[i] == 0:
                visited[i] = -visited[a]
                q.append(i)
            elif visited[i] == visited[a]:
                return False
    return True

for _ in range(k):
    v, e = map(int, input().split())
    adj = [[] for _ in range(v)]
    visited = [0 for _ in range(v)]
    for _ in range(e):
        x, y = map(lambda x: int(x) - 1, input().split())
        adj[x].append(y)
        adj[y].append(x)
    isTrue = True
    for idx, isvisit in enumerate(visited):
        if isvisit == 0:
            if not bfs(idx):
                isTrue = False
                break
    print('YES' if isTrue else 'NO')