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
    t = v + 1
    adj = [[] for _ in range(t)]
    visited = [False for _ in range(t)]
    for _ in range(e):
        x, y = map(int, input().split())
        adj[x].append(y)

    isTrue = True
    for idx, isvisit in enumerate(visited):
        if not isvisit:
            if not bfs(idx):
                isTrue = False
                break
    print("NO" if isTrue else "YES")
    