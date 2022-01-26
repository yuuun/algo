from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
dxy = [[0, -1], [0, 1], [1, 0], [-1, 0]]
q = deque()
ans = 0
chk = False

def bfs(x, y):
    q.append([x, y])
    while q:
        x, y = q.popleft()
        visited[x][y] = True

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] > 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])
                elif maps[nx][ny] <= 0:
                    count[x][y] += 1
    return 1

while True:
    visited = [[False] * m for _ in range(n)]
    count = [[0] * m for _ in range(n)]
    res = []
    for x in range(n):
        for y in range(m):
            if maps[x][y] > 0 and not visited[x][y]:
                res.append(bfs(x, y))
    
    for x in range(n):
        for y in range(m):
            maps[x][y] -= count[x][y]
    
    if len(res) == 0:
        break
    if len(res) > 1:
        chk = True
        break
    ans += 1

if chk:
    print(ans)
else:
    print(0)