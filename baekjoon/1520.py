m, n = map(int, input().split()) # 세로크기, 가로크기
maps = [list(map(int, input().split())) for _ in range(m)]

dxy = [[-1, 0], [1, 0], [0, 1], [0, -1]]
dis = [[-1] * n for _  in range(m)]
def dfs(x, y):
    if x == m - 1 and y == n - 1:
        return 1
    if dis[x][y] != -1:
        return dis[x][y]
    dis[x][y] = 0
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n:
            if dis[nx][ny] < maps[x][y]:
                dis[x][y] += dfs(nx, ny)
    return dis[nx][ny]

print(dfs(0, 0))