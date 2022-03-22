#TBD
#from collections import deque
k = int(input())

def bfs(s):
    visited[s] = True
    for vi in adj[s]:
        if visited[vi]:
            return False
        visited[vi] = True

    return True

for _ in range(k):
    v, e = map(int, input().split())
    adj = [[] for _ in range(v)]
    visited = [False for _ in range(v)]
    visited[0] = True
    for _ in range(e):
        x, y = map(lambda x: int(x) - 1, input().split())
        adj[x].append(y)

    cnt = 0
    for idx, isvisit in enumerate(visited):
        if not isvisit:
            if not bfs(idx):
                cnt += 1
    
    print("NO" if cnt > 1 else "YES")