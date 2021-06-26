import sys
sys.setrecursionlimit(10000)

t = int(input())
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def dfs(x, y):
    adj[x][y] = 0
    for dx, dy in d:
        tx = x + dx
        ty = y + dy
        if 0 <= tx < m and 0 <= ty < n:
            if adj[tx][ty] == 1:
                dfs(tx, ty)
                
for _ in range(t):
    m, n, k = map(int, input().split())
    adj = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        adj[x][y] = 1
    if k == 1:
        print(1)
    else:
        cnt = 0

        for x in range(m):
            for y in range(n):
                if adj[x][y] == 1:
                    dfs(x, y)
                    cnt += 1
        print(cnt)
