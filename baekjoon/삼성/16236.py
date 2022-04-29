# 9:15 - 10:20
n = int(input())
sizebaby = 2
bx, by = 0, 0
maps = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 9:
            bx, by = i, j
            tmp[j] = 0
    maps.append(tmp)

from collections import deque
dxy = [[-1, 0], [0, -1], [0, 1], [1, 0]]
def find_shortest():
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    q.append([bx, by, 0])
    visited[bx][by] = 0
    min_val = sizebaby
    sx, sy, sd = n, n, 1e10
    while q:
        x, y, d = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] > sizebaby:
                    continue
            
                if visited[nx][ny] == -1:
                    visited[nx][ny] = d + 1
                    q.append([nx, ny, d + 1])
                    if maps[nx][ny] > 0:
                        if min_val > maps[nx][ny]:
                            if sd == 1e10:
                                sx, sy, sd = nx, ny, d + 1

                            if sd == d + 1:
                                if sx > nx or (sx == nx and sy > ny):
                                    sx, sy = nx, ny
    return sx, sy, sd
ans = 0
tt = 0
while True:
    sx, sy, sd = find_shortest()
    tt += 1
    if (sx, sy) == (n, n):
        break
    if tt == sizebaby:
        sizebaby += 1
        tt = 0
    bx, by = sx, sy
    ans += sd
    
    maps[sx][sy] = 0

print(ans)