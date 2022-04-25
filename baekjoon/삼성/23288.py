# 8:40 - 9:07
n, m, k = map(int, input().split())
dice = [None, 1, 2, 3, 4, 5, 6] # 위, 뒤, 오른, 왼, 앞, 뒤
maps = [list(map(int, input().split())) for _ in range(n)]
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 동, 남, 서, 북
d_direction = {0: 2, 1: 3, 2: 0, 3: 1}
d = 0
x, y = 0, 0
def rotate_dice():
    if d == 0: #동
        dice[1], dice[4], dice[6], dice[3] = dice[4], dice[6], dice[3], dice[1]
    elif d == 2: #서
        dice[1], dice[3], dice[6], dice[4] = dice[3], dice[6], dice[4], dice[1]
    elif d == 1: #남
        dice[1], dice[2], dice[6], dice[5] = dice[2], dice[6], dice[5], dice[1]
    else:
        dice[1], dice[5], dice[6], dice[2] = dice[5], dice[6], dice[2], dice[1]

def move_dice():
    global d, x, y
    nx, ny = x + dxy[d][0], y + dxy[d][1]
    if not (0 <= nx < n and 0 <= ny < m):
        d = d_direction[d]
        nx, ny = x + dxy[d][0], y + dxy[d][1]
    rotate_dice()
    x, y = nx, ny
    
    if dice[6] > maps[x][y]:
        d = (d + 1) % 4
    elif dice[6] < maps[x][y]:
        d = (d - 1) % 4

from collections import deque
def calculate_point(nx, ny):
    q = deque()
    q.append([nx, ny])
    cur = maps[nx][ny]
    cnt = maps[nx][ny]
    visited[nx][ny] = True
    sq = deque()
    sq.append([nx, ny])
    while q:
        nx, ny = q.popleft()
        for dx, dy in dxy:
            nnx, nny = nx + dx, ny + dy
            if 0 <= nnx < n and 0 <= nny < m and not visited[nnx][nny]:
                if cur == maps[nnx][nny]:
                    q.append([nnx, nny])
                    visited[nnx][nny] = True
                    cnt += maps[nx][ny]
                    sq.append([nnx, nny])
    while sq:
        nx, ny = sq.popleft()
        score_map[nx][ny] = cnt

score_map = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
for nx in range(n):
    for ny in range(m):
        if not visited[nx][ny]:
            calculate_point(nx, ny)

score = 0
for _ in range(k):
    move_dice()
    score += score_map[x][y]
    # print(x, y, score_map[x][y], d, dice)
    # score += calculate_point()
print(score)