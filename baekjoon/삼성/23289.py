# 6:00 - 7: 07
r, c, k = map(int, input().split())
heater = []
check = []
for i in range(r):
    tmp = list(map(int, input().split()))
    for j in range(c):
        if tmp[j] == 5:
            check.append([i, j])
        elif tmp[j] > 0:
            heater.append([i, j, tmp[j] - 1])

wall = [[[True] * 4 for _ in range(c)] for _ in range(r)] # 오른, 왼, 위, 아래
maps = [[0] * c for _ in range(r)]

for _ in range(int(input())):
    x, y, t = map(int, input().split())
    x -= 1
    y -= 1
    if t == 1:
        wall[x][y][0] = False
        if y + 1 < c:
            wall[x][y + 1][1] = False
    else:
        wall[x][y][2] = False
        if x > 0:
            wall[x - 1][y][3] = False

from collections import deque
def init_heat():
    global added_heat
    added_heat = [[0] * c for _ in range(r)]
    for x, y, d in heater:
        q = deque()
        visited = [[False] * c for _ in range(r)]
        if d == 0: # 오른 쪽방향일 때
            if y + 1 >= c:
                continue
            q.append([x, y + 1, 5])
            while q:
                x, y, h = q.popleft()
                visited[x][y] = True
                added_heat[x][y] += h
                if y + 1 >= c:
                    continue
                if h > 0:
                    h -= 1
                    if x > 0:
                        if wall[x - 1][y][3] and wall[x - 1][y][0] and not visited[x - 1][y + 1]:
                            visited[x - 1][y + 1] = True
                            q.append([x - 1, y + 1, h])
                    if wall[x][y][0] and not visited[x][y + 1]:
                        visited[x][y + 1] = True
                        q.append([x, y + 1, h])
                    if x + 1 < r:
                        if wall[x + 1][y][2] and wall[x + 1][y][0] and not visited[x + 1][y + 1]:
                            visited[x + 1][y + 1] = True
                            q.append([x + 1, y + 1, h])
        elif d == 1: # 왼 쪽방향일 때
            if y - 1 < 0:
                continue
            q.append([x, y - 1, 5])
            while q:
                x, y, h = q.popleft()
                visited[x][y] = True
                added_heat[x][y] += h
                if y - 1 < 0:
                    continue
                if h > 0:
                    h -= 1
                    if x > 0:
                        if wall[x - 1][y][3] and wall[x - 1][y][1] and not visited[x - 1][y - 1]:
                            q.append([x - 1, y - 1, h])
                            visited[x - 1][y - 1] = True
                    if wall[x][y][1] and not visited[x][y - 1]:
                        visited[x][y - 1] = True
                        q.append([x, y - 1, h])
                    if x + 1 < r:
                        if wall[x + 1][y][2] and wall[x + 1][y][1] and not visited[x + 1][y - 1]:
                            visited[x + 1][y - 1] = True
                            q.append([x + 1, y - 1, h])
        
        elif d == 2: # 위 방향
            if x - 1 < 0:
                continue
            q.append([x - 1, y, 5])
            while q:
                x, y, h = q.popleft()
                visited[x][y] = True
                added_heat[x][y] += h
                if x - 1 < 0:
                    continue
                if h > 0:
                    h -= 1
                    if y > 0:
                        if wall[x][y - 1][2] and wall[x][y - 1][0] and not visited[x - 1][y - 1]:
                            q.append([x - 1, y - 1, h])
                            visited[x - 1][y - 1] = True
                    if wall[x][y][2] and not visited[x - 1][y]:
                        visited[x - 1][y] = True
                        q.append([x - 1, y, h])
                    if y + 1 < c:
                        if wall[x][y + 1][2] and wall[x][y + 1][1] and not visited[x - 1][y + 1]:
                            visited[x - 1][y + 1] = True
                            q.append([x - 1, y + 1, h])
        else: # 아래 방향
            if x + 1 >= r:
                continue
            q.append([x + 1, y, 5])
            while q:
                x, y, h = q.popleft()
                visited[x][y] = True
                added_heat[x][y] += h
                if x + 1 >= r:
                    continue
                if h > 0:
                    h -= 1
                    if y > 0:
                        if wall[x][y - 1][3] and wall[x][y - 1][0] and not visited[x + 1][y - 1]:
                            visited[x + 1][y - 1] = True
                            q.append([x + 1, y - 1, h])
                    if wall[x][y][3] and not visited[x + 1][y]:
                        q.append([x + 1, y, h])
                        visited[x + 1][y] = True
                    if y + 1 < c:
                        if wall[x][y + 1][3] and wall[x][y + 1][1] and not visited[x + 1][y + 1]:
                            q.append([x + 1, y + 1, h])
                            visited[x + 1][y + 1] = True

init_heat()
def fill_heat():
    for x in range(r):
        for y in range(c):
            maps[x][y] += added_heat[x][y]

dxy = [[0, 1], None, None, [1, 0]] #오른, 아래
def spread_heat():
    new_heat = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            for d in [0, 3]:
                nx, ny = x + dxy[d][0], y + dxy[d][1]
                if nx < r and ny < c:
                    if wall[x][y][d]:
                        val = int((maps[x][y] - maps[nx][ny]) / 4)
                        new_heat[x][y] -= val 
                        new_heat[nx][ny] += val
    
    for x in range(r):
        for y in range(c):
            maps[x][y] += new_heat[x][y]

    for x in range(r):
        if maps[x][0] > 0:
            maps[x][0] -= 1
        if maps[x][-1] > 0:
            maps[x][-1] -= 1
    for y in range(1, c - 1):
        if maps[0][y] > 0:
            maps[0][y] -= 1
        if maps[-1][y] > 0:
            maps[-1][y] -= 1

def check_heat():
    for x, y in check:
        if maps[x][y] < k:
            return False
    return True
cnt = 1
while cnt < 101:
    fill_heat()
    spread_heat()
    if check_heat():
        break
    cnt += 1
print(cnt)
print(maps)