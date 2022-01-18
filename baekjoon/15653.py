from collections import deque
n, m = map(int, input().split())
board = []
for i in range(n):
    tmp = list(input())
    if 'R' in tmp:
        rx, ry = [i, tmp.index('R')]
    if 'B' in tmp:
        bx, by = [i, tmp.index('B')]
    board.append(tmp)
cnt = 1
visited = [[[[False] * m for i in range(n)] for i in range(m)] for i in range(n)]
dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def move(i, j, dx, dy):
    c = 0
    while board[i + dx][j + dy] != '#' and board[i][j] != 'O':
        i += dx
        j += dy
        c += 1
    return i, j, c

def bfs(bx, by, rx, ry, cnt):
    q = deque()
    q.append([bx, by, rx, ry, cnt])
    while q:
        bx, by, rx, ry, cnt = q.popleft()
        for dx, dy in dxy:
            nbx, nby, bc = move(bx, by, dx, dy)
            nrx, nry, rc = move(rx, ry, dx, dy)

            if board[nbx][nby] != 'O':
                if board[nrx][nry] == 'O':
                    print(cnt)
                    return
            
                if nrx == nbx and nry == nby:
                    if rc > bc:
                        nrx -= dx
                        nry -= dy
                    else:
                        nbx -= dx
                        nby -= dy
                
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    q.append([nbx, nby, nrx, nry, cnt + 1])
    print(-1)
bfs(bx, by, rx, ry, 1)
visited[rx][ry][bx][by] = True