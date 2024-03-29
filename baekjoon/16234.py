# 틀림
n, l, r = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]

from collections import deque
def move_people():
    visited = [[False] * n for _ in range(n)]
    isTrue = True
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                visited[x][y] = True
                q = deque()
                q.append([x, y])
                added = deque()
                added.append([x, y])
                total = maps[x][y]
                while q:
                    x, y = q.popleft()
                    for dx, dy in dxy:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            if l <= abs(maps[nx][ny] - maps[x][y]) <= r and not visited[nx][ny]:
                                q.append([nx, ny])
                                added.append([nx, ny])
                                visited[nx][ny] = True
                                total += maps[nx][ny]
                if len(added) > 1:
                    divided = total // len(added)
                    while added:
                        x, y = added.popleft()
                        if maps[x][y] != divided:
                            isTrue = False
                            maps[x][y] = divided
    return isTrue
days = 0
while True:
    if move_people():
        break
    days += 1
print(days)


'''
n, l, r = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

def check_walls():
    walls = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n - 1):
            if l <= abs(maps[i][j + 1] - maps[i][j]) <= r:
                continue
            walls[i][j] |= 1 << 1
            walls[i][j + 1] |= 1 << 3

    for j in range(n):
        for i in range(n - 1):
            if l <= abs(maps[i][j] - maps[i + 1][j]) <= r:
                continue
            walls[i][j] |= 1 << 2
            walls[i + 1][j] |= 1 << 0
    return move_people(walls)

from collections import deque
dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]]
def move_people(walls):
    visited = [[False] * n for _ in range(n)]
    ismoved = True
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                added = deque()
                added.append([i, j])

                q = deque()
                q.append([i, j])
                total = maps[i][j]
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        if walls[x][y] & (1 << k) == 0:
                            dx, dy = dxy[k]
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                                added.append([nx, ny])
                                q.append([nx, ny])
                                total += maps[nx][ny]
                                visited[nx][ny] = True
                divided = total // len(added)
                if len(added) > 1:
                    ismoved = False
                    while added:
                        x, y = added.popleft()
                        maps[x][y] = divided
    return ismoved
days = 0
while True:
    if check_walls():
        break
    days += 1
print(days)

'''