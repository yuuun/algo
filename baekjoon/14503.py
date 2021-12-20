n, m = map(int, input().split())
r, c, d = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
maps = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

def sol(x, y, d):
    global cnt
    if maps[x][y] == 0:
        maps[x][y] = 2
        cnt += 1
    for _ in range(4):
        nd = (d + 3) % 4
        nx, ny = x + dx[nd], y + dy[nd]
        if maps[nx][ny] == 0:
            sol(nx, ny, nd)
            return
        d = nd
    nd = (d + 2) % 4
    nx, ny = x + dx[nd], y + dy[nd]

    if maps[nx][ny] == 1:
        return
    sol(nx, ny, d)

sol(r, c, d)
print(cnt)    