import sys
sys.setrecursionlimit(100000)

def dfs(v):
    visited[v] = True
    for tmp in adj[v]:
        if not visited[tmp]:
            dfs(tmp)
            
n, m = map(int, input().split())
t = n + 1
adj = [[] for _ in range(t)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)


visited = [False] * t
cnt = 0    
for i in range(1, t):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)