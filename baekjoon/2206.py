from collections import deque
n, m = map(int, input().split())
maps = [list(map(lambda x:int(x), input())) for _ in range(n)]

ans = []

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def bfs(visited):
    q = deque()
    flag = 0
    q.append([0, 0, flag])
    visited[0][0][flag] = 1
    while q:
        x, y, f = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][f]
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 0 and visited[nx][ny][f] == 0:
                    q.append([nx, ny, f])
                    visited[nx][ny][f] = visited[x][y][f] + 1
                if maps[nx][ny] == 1 and f == 0:
                    q.append([nx, ny, 1])
                    visited[nx][ny][1] = visited[x][y][0] + 1
    return -1
print(bfs(visited))