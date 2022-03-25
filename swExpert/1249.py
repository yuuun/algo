# 보급로
from collections import deque
dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]
MAX_SIZE = 1e10
for i in range(1, int(input()) + 1):
    n = int(input())
    maps = [list(map(int, input())) for _ in range(n)]
    min_val = [[MAX_SIZE] * n for _ in range(n)]
    min_val[0][0] = 0
    q = deque()
    q.append([0, 0])
    while q:
        x, y = q.popleft()
        c = min_val[x][y]
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                nc = c + maps[nx][ny]
                if min_val[nx][ny] > nc:
                    min_val[nx][ny] = nc
                    q.append([nx, ny])
    print('#{0} {1}'.format(i, min_val[-1][-1]))