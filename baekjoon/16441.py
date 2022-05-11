from collections import deque
n, m = map(int, input().split())
maps = []
visited = [[False] * m for _ in range(n)]
wolf = deque()
for i in range(n):
    tmp = list(input())
    for j in range(m):
        if tmp[j] == 'W':
            wolf.append([i, j, [0, 1, 2, 3]])
            visited[i][j] = True
        elif tmp[j] == '#' or tmp[j] == '+':
            visited[i][j] = True
    maps.append(tmp)

dxy = [[0, 1], [-1, 0], [0, -1], [1, 0]]
while wolf:
    x, y, dir = wolf.popleft()
    for d in dir:
        dx, dy = dxy[d]
        nx, ny = x + dx, y + dy
        if maps[nx][ny] == '.' and not visited[nx][ny]:
            visited[nx][ny] = True
            wolf.append([nx, ny, [0, 1, 2, 3]])
        if maps[nx][ny] == '+':
            tx, ty = nx + dx, ny + dy
            while maps[tx][ty] != '#':
                tx, ty = tx + dx, ty + dy
            di = [0, 1, 2, 3]
            di.remove(2)
            tx, ty = tx - dx, ty - dy
            wolf.append([tx, ty, di])
            visited[tx][ty] = True
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            print(maps[i][j], end='')
        else:
            print('P', end='')
    print()
