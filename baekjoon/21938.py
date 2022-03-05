from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pixels = [list(map(int, input().split())) for _ in range(n)]
boundary = int(input()) * 3
new_pixels = []
for i in range(n):
    tmp = []
    for j in range(m):
        if sum(pixels[i][3 * j: 3 * (j + 1)]) >= boundary:
            tmp.append(True)
        else:
            tmp.append(False)
    new_pixels.append(tmp)

visited = [[False] * m for _ in range(n)]
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def is_criteria(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if is_criteria(nx, ny) and not visited[nx][ny] and new_pixels[nx][ny]:
                visited[nx][ny] = True
                q.append([nx, ny])

ans = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if new_pixels[i][j]:
                bfs(i, j)
                ans += 1
print(ans)