from collections import deque

n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]

dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]
def bfs(x, y):
    cnt = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = True
 
    while q:
        x, y = q.popleft()
 
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1 
    return cnt
 
 
cnt, max_val = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt += 1
            max_val = max(max_val, bfs(i, j))

print(cnt)
print(max_val)