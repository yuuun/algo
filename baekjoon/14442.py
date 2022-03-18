from collections import deque
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
maps = [list(map(lambda x: int(x), input().rstrip())) for _ in range(n)]
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]

dxs = [1, -1, 0, 0]
dys = [0, 0, -1, 1]
def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1
    while q:
        x, y, cnt = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][cnt]
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny][cnt]:
                    if maps[nx][ny] and cnt < k:
                        visited[nx][ny][cnt + 1] = visited[x][y][cnt] + 1
                        q.append((nx, ny, cnt + 1))
                    elif not maps[nx][ny]:
                        visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                        q.append((nx, ny, cnt))
                

    return -1

print(bfs())
