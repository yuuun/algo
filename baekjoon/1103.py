n, m = map(int, input().split())
maps = []
for _ in range(n):
    inp = input().split()
    maps.append(list(inp[0]))

dxy = [[0, 1], [0, -1], [-1, 0], [1, 0]]
ans = 0

dp = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    weight = int(maps[y][x])
    for dx, dy in dxy:
        nx = x + weight * dx
        ny = y + weight * dy
        if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] != 'H' and cnt + 1 > dp[ny][nx]:
            if visited[ny][nx]:
                print(-1)
                exit()
            else:
                dp[ny][nx] = cnt + 1
                visited[ny][nx] = True
                dfs(nx, ny, cnt + 1)
                visited[ny][nx] = False

dfs(0, 0, 0)
print(ans + 1)