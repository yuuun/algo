from collections import deque
n, m = map(int, input().split())
maps = []
walls = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 1:
            walls.append([i, j])
    maps.append(tmp)

h, w, sx, sy, fx, fy = map(int, input().split())
sx -= 1
sy -= 1
fx -= 1
fy -= 1

def check_rect(x, y):
    for i, j in walls:
        if x <= i < x + h and y <= j < y + w:
            return False
    return True

dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]
def bfs():
    q = deque([[sx, sy, 0]])
    visited = [[False] * m for _ in range(n)]
    visited[sx][sy] = True
    while q:
        x, y, c = q.popleft()
        if [x, y] == [fx, fy]:
            return c
        c += 1
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n - h + 1 and 0 <= ny < m - w + 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                if check_rect(nx, ny):
                    q.append([nx, ny, c])
    return -1

if not check_rect(sx, sy):
    print(-1)
    exit()

print(bfs())


'''
https://www.acmicpc.net/source/29830231
from sys import stdin
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, stdin.readline().strip().split())

board = [list(map(int, stdin.readline().split())) for _ in range(n)]

h,w,sr,sc,fr,fc = map(int, stdin.readline().strip().split())

def solv():
    global board
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                unable_point_check(i + 1, j + 1)
    return bfs()

def unable_point_check(x,y):
    global board
    start_x = x-h
    start_x = 0 if start_x < 0 else start_x

    start_y = y-w
    start_y = 0 if start_y < 0 else start_y

    for i in range(start_x,x):
        for j in range(start_y,y):
            board[i][j] = 1

def bfs():
    q = deque()
    visited = [[False]*(m-w+1) for _ in range(n-h+1)]

    q.appendleft((sr-1,sc-1,0))
    visited[sr-1][sc-1] = True

    while q:
        x,y,cnt = q.pop()

        if x == fr-1 and y == fc-1:
            return cnt

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not point_validator(nx,ny,visited):
                continue
            visited[nx][ny] = True
            q.appendleft((nx,ny,cnt+1))
    return -1

def point_validator(x,y,visited):
    if x < 0 or y < 0 or x > n-h or y > m-w:
        return False
    elif visited[x][y]:
        return False
    elif board[x][y] == 1:
        return False
    return True

print(solv())

'''