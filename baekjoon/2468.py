import sys
sys.setrecursionlimit(100000)

n = int(input())
adj = []
min_val = 100
max_val = 2

d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def dfs(x, y, idx):
    for dx, dy in d:
        tx, ty = x + dx, y + dy
        if 0 <= tx < n and 0 <= ty < n:
            if not visited[tx][ty] and adj[tx][ty] >= idx:
                visited[tx][ty] = True
                dfs(tx, ty, idx)

for _ in range(n):
    tmp = list(map(int, input().split()))
    adj.append(tmp)
    ma = max(tmp)
    if max_val < ma:
        max_val = ma

ans = 1
for idx in range(max_val):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if adj[i][j] >= idx and not visited[i][j]:
                cnt += 1
                visited[i][j] = True
                dfs(i, j, idx)
    if ans < cnt:
        ans = cnt
print(ans)