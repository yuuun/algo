from collections import deque
n, m = map(int, input().split())
maps = []
visited = [[False] * m for _ in range(n)]
wolf = deque()
for i in range(n):
    tmp = list(input())
    for j in range(m):
        if tmp[j] == 'W':
            wolf.append([i, j])
            visited[i][j] = True
        elif tmp[j] == '#':
            visited[i][j] = True
    maps.append(tmp)

dxy = [[0, 1], [-1, 0], [0, -1], [1, 0]]
while wolf:
    x, y = wolf.popleft()
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if maps[nx][ny] == '.' and not visited[nx][ny]:
            visited[nx][ny] = True
            wolf.append([nx, ny])
        else:
            while True:
                if maps[nx][ny] == '#':
                    nx -= dx
                    ny -= dy
                    break
                elif maps[nx][ny] == '.':
                    break
                nx += dx
                ny += dy
            if not visited[nx][ny]:
                wolf.append([nx, ny])
                visited[nx][ny] = True

for i in range(n):
    for j in range(m):
        if visited[i][j] or maps[i][j] == '+':
            print(maps[i][j], end='')
        else:
            print('P', end='')
    print()
