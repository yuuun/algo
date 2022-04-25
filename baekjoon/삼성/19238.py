# 2: 40 - 3:21 시간초과
n, m, f = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
tx, ty = map(int, input().split())
tx, ty = tx - 1, ty - 1
cust = []
for i in range(m):
    sx, sy, ex, ey =  map(lambda x: int(x) - 1, input().split())
    cust.append([sx, sy, ex, ey])
cust = sorted(cust, key=lambda x: (x[0], x[1]))

from collections import deque
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def find_min(sx, sy, ex, ey):
    if [sx, sy] == [ex, ey]:
        return 0
    q = deque()
    q.append([sx, sy, 0])
    visited = [[False] * n for _ in range(n)]
    visited[sx][sy] = True

    while q:
        x, y, dis = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] == 0 and not visited[nx][ny]:
                if [ex, ey] == [nx, ny]:
                    return dis + 1
                else:
                    visited[nx][ny] = True
                    q.append([nx, ny, dis + 1])
    print(-1)
    exit()

for i in range(m):
    cust[i].append(find_min(*cust[i]))
cust_visited = [False] * m
def find_cust():
    global f, tx, ty
    min_dis = 1e20
    idx = -1
    for i in range(m):
        if cust_visited[i]:
            continue
        d = find_min(tx, ty, cust[i][0], cust[i][1])
        if d < min_dis:
            idx = i
            min_dis = d
        
    if f < min_dis:
        print(-1)
        exit()
    f -= min_dis
    if f < cust[idx][-1]:
        print(-1)
        exit()
    cust_visited[idx] = True
    f += cust[idx][-1]
    tx, ty = cust[idx][2], cust[idx][3]

tmp = 0
while tmp < m:
    find_cust()
    tmp += 1
print(f)