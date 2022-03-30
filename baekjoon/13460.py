import sys
input = sys.stdin.readline
n, m = map(int, input().split())
maps = []
bx, by = 0, 0
rx, ry = 0, 0
fx, fy = 0, 0
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
for i in range(n):
    tmp = list(input())
    for j in range(m):
        if tmp[j] == '#':
            continue
        if tmp[j] == 'B':
            bx, by = i, j
            tmp[j] = '.'
            continue
        if tmp[j] == 'R':
            rx, ry = i, j
            tmp[j] = '.'
            continue
        if tmp[j] == 'O':
            fx, fy = i, j
    maps.append(tmp)

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def move_marble(x, y, dx, dy):
    while True:
        nx = x + dx
        ny = y + dy
        if nx == fx and ny == fy:
            return False
        if maps[nx][ny] == '#':
            return x, y
        else:
            x, y = nx, ny

def move_two(a, b, d, nt):
    if d == 1:
        if b > a:
            b = nt
            a = nt - 1
        else:
            a = nt
            b = nt - 1
    else:
        if b > a:
            a = nt
            b = nt + 1
        else:
            b = nt 
            a = nt + 1
    return a, b

from collections import deque

ans = 11
def bfs(_bx, _by, _rx, _ry):
    global ans
    q = deque()
    q.append([_bx, _by, _rx, _ry, 1])
    visited[_bx][_by][_rx][_ry] = True
    while q:
        bx, by, rx, ry, cnt = q.popleft()
        if cnt == 11:
            continue
        for dx, dy in dxy:
            btmp = move_marble(bx, by, dx, dy)
            if btmp:
                nbx, nby = btmp
            else:
                continue
            rtmp = move_marble(rx, ry, dx, dy)
            if rtmp:
                nrx, nry = rtmp
            else:
                ans = min(ans, cnt)
                continue
            if nrx == nbx and nry == nby:
                if dx == 0: # y축 이동
                    nby, nry = move_two(by, ry, dy, nby)
                else: # x축 이동
                    nbx, nrx = move_two(bx, rx, dx, nbx)
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.append([nbx, nby, nrx, nry, cnt + 1])

bfs(bx, by, rx, ry)
print(ans if ans < 11 else -1)