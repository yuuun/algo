from collections import deque
r, c = map(int, input().split())
direction = {'|': [1, 3], '-': [0, 2], '+': [0, 1, 2, 3], 'M': [0, 1, 2, 3], 'Z': [0, 1, 2, 3], 
            '1': [0, 1], '2': [0, 3], '3': [2, 3], '4': [1, 2]}
maps = []
for i in range(r):
    tmp = list(input())
    for j in range(c):
        if tmp[j] == 'M':
            sx, sy = i, j
        elif tmp[j] == 'Z':
            zx, zy = i, j
    maps.append(tmp)
chck, fx, fy = [], 0, 0

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
visited = [[False] * c for _ in range(r)]
def bfs(x, y, d):
    global fx, fy
    q = deque()
    q.append([x, y, d])
    visited[x][y] = True
    while q:
        x, y, d = q.popleft()
        for di in d:
            dx, dy = dxy[di]
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if maps[nx][ny] != '.':
                    visited[nx][ny] = True
                    nd = direction[maps[nx][ny]]
                    q.append([nx, ny, nd])
                else:
                    if maps[x][y] == 'M' or maps[x][y] == 'Z':
                        continue
                    if not fx and not fy:
                        fx, fy = nx + 1, ny + 1
                    nd = (di + 2) % 4
                    if nd not in chck:
                        chck.append(nd)

bfs(sx, sy, [0, 1, 2, 3])
bfs(zx, zy, [0, 1, 2, 3])

for i in range(r):
    for j in range(c):
        if maps[i][j] != '.' and not visited[i][j]:
            bfs(i, j, direction[maps[i][j]])
chck.sort()

if len(chck) == 4:
    print(fx, fy, '+')
else:
    block_list = ['|', '-', '1', '2', '3', '4']
    for s in block_list:
        if chck == direction[s]:
            print(fx, fy, s)