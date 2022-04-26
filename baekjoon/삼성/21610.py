# 4: 35 - 5:20
#마법사 상어와 비바라기
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
dxy = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
cloud = [[False] * n for _ in range(n)]
cloud[n - 1][0] = True
cloud[n - 1][1] = True
cloud[n - 2][0] = True
cloud[n - 2][1] = True

from collections import deque
def move_cloud(d, s):
    q = deque()
    new_q = deque()
    for x in range(n):
        for y in range(n):
            if cloud[x][y]:
                nx, ny = (x + s * dxy[d][0]) % n, (y + s * dxy[d][1]) % n
                maps[nx][ny] += 1
                cloud[x][y] = False
                q.append([nx, ny])
    
    while q:
        nx, ny = q.popleft()
        cnt = 0
        for dx, dy in [[-1, -1], [-1, 1], [1, 1], [1, -1]]:
            nnx, nny = nx + dx, ny + dy
            if 0 <= nnx < n and 0 <= nny < n and maps[nnx][nny] > 0:
                cnt += 1
        new_q.append([nx, ny, cnt])
    
    while new_q:
        x, y, cnt = new_q.popleft()
        maps[x][y] += cnt
        cloud[x][y] = True
    
    for x in range(n):
        for y in range(n):
            if maps[x][y] > 1 and not cloud[x][y]:
                q.append([x, y])
                maps[x][y] -= 2
            if cloud[x][y]:
                cloud[x][y] = False
    while q:
        x, y = q.popleft()
        cloud[x][y] = True
    return

for _ in range(m):
    d, s = map(int, input().split())
    move_cloud(d - 1, s)

print(sum(sum(i) for i in maps))