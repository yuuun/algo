n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]]
ans = 0
visited = [[False] * m for _ in range(n)]
max_val = max(map(max, maps))
def dfs(x, y, idx, total):
    global ans
    if ans >= total + max_val * (3 - idx):
        return
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if idx == 1:
                    visited[nx][ny] = True
                    dfs(x, y, idx + 1, total + maps[nx][ny])
                    visited[nx][ny] = False
                visited[nx][ny] = True
                dfs(nx, ny, idx + 1, total + maps[nx][ny])
                visited[nx][ny] = False
            
for x in range(n):
    for y in range(n):
        visited[x][y] = True
        dfs(x, y, 0, maps[x][y])
        visited[x][y] = False
print(ans)