from collections import deque
r, c, k = map(int, input().split())

checked_pos = [] # 체크할 온풍기 위치
heater = [] # 온풍기 위치 ([온풍기 위치x, 온풍기 위치y, 방향])

added_heat = [[0] * c for _ in range(r)]

for i in range(r):
    tmp = list(map(int, input().split()))
    for j, t in enumerate(tmp):
        if t == 0:
            continue    
        if 0 < t < 5:
            heater.append([i, j, t])
        else:
            checked_pos.append([i, j])

up_walls = [[-1] * c for _ in range(r)] # 오른: 1, 위: 0
right_walls = [[-1] * c for _ in range(r)]

for _ in range(int(input())):
    x, y, t = map(int, input().split())
    x -= 1
    y -= 1
    if t == 1:
        right_walls[x][y] = 0
    elif t == 0:
        up_walls[x][y] = 0

maps = [[0] * c for _ in range(r)]
dxys = [[], [[-1, 1], [0, 1], [1, 1]], [[-1, -1], [0, -1], [1, -1]], [[-1, -1], [-1, 0], [-1, 1]], [[1, -1], [1, 0], [1, 1]]]


right_dxy = [[], [[0, -1], [-1, -1], [1, -1]],
            [[0, 0], [1, 0], [-1, 0]],
            [[], [1, -1], [1, 0]],
            [[], [-1, -1], [-1, 0]]]

up_dxy = [[], [[], [0, -1], [1, -1]], 
                [[], [1, 1], [0, 1]],
                [[1, 0], [1, -1], [1, 1]],
                [[0, 0], [0, -1], [0, 1]]]

def iscriteria(x, y):
    if 0 <= x < r and 0 <= y < c:
        return True
    return False

def fill_heat(nx, ny, t):
    if iscriteria(nx, ny) and not visited[nx][ny]:        
        if t < 3:
            tx, ty = nx + right_dxy[t][0][0], ny + right_dxy[t][0][1]
            if iscriteria(tx, ty):
                if right_walls[tx][ty] == 0:
                    return False
                else:
                    return True
            for dx, dy in up_dxy[t][1:]:
                tx, ty = nx + dx, ny + dy
                if iscriteria(tx, ty) and up_walls[tx][ty] == 0:
                    return False
            return True
            
        else:
            tx, ty = nx + up_dxy[t][0][0], ny + up_dxy[t][0][1]
            if iscriteria(tx, ty):
                if up_walls[tx][ty] == 0:
                    return False
                else:
                    return True
            for dx, dy in right_dxy[t][1:]:
                tx, ty = nx + dx, ny + dy
                if iscriteria(tx, ty) and right_walls[tx][ty] == 0:
                    return False
            return True
    return False


def init_map():
    for x, y, t in heater:
        x += dxys[t][1][0]
        y += dxys[t][1][1]
        q = deque()
        q.append([x, y, 4])
        global visited
        
        visited = [[False] * c for _ in range(r)]
        visited[x][y] = True
        added_heat[x][y] += 5
        
        while q:
            x, y, cnt = q.popleft()
            for dx, dy in dxys[t]:
                nx, ny = x + dx, y + dy
                if 0 < cnt and iscriteria(nx, ny) and not visited[nx][ny] and fill_heat(nx, ny, t):
                    added_heat[nx][ny] += cnt
                    q.append([nx, ny, cnt - 1])
                    visited[nx][ny] = True
        print(added_heat)
def blow_heater():
    for i in range(r):
        for j in range(c):
            maps[i][j] += added_heat[i][j]
    

def minus_one():
    for i in range(r):
        if maps[i][0] != 0:
            maps[i][0] -= 1
        if maps[i][-1] != 0:
            maps[i][-1] -= 1

    for j in range(1, c - 1):
        if maps[0][j] != 0:
            maps[0][j] -= 1
        if maps[-1][j] != 0:
            maps[-1][j] -= 1
            
def spread_heat():
    heats = [[0] * c for _ in range(r)]
    for x in range(r - 1):
        nx = x + 1
        for y in range(c - 1):
            if iscriteria(nx, y):
                if up_walls[nx][y] < 0:
                    sub = abs(maps[nx][y] - maps[x][y]) // 4
                    if maps[nx][y] > maps[x][y]:
                        heats[nx][y] -= sub
                        heats[x][y] += sub
                    else:
                        heats[nx][y] += sub
                        heats[x][y] -= sub
            
            if iscriteria(x, y):
                if right_walls[x][y] < 0:
                    ny = y + 1
                    sub = abs(maps[x][ny] - maps[x][y]) // 4
                    if maps[x][ny] > maps[x][y]:
                        heats[x][ny] -= sub
                        heats[x][y] += sub
                    else:
                        heats[x][ny] += sub
                        heats[x][y] -= sub
    y = c - 1
    for x in range(1, r):
        nx = x - 1
        if up_walls[x][y] < 0:
            sub = abs(maps[nx][y] - maps[x][y]) // 4
            if maps[nx][y] > maps[x][y]:
                heats[nx][y] -= sub
                heats[x][y] += sub
            else:
                heats[nx][y] += sub
                heats[x][y] -= sub
    
    x = r - 1
    for y in range(1, c):
        ny = y - 1
        if right_walls[x][ny] < 0:
            sub = abs(maps[x][ny] - maps[x][y]) // 4
            if maps[x][ny] > maps[x][y]:
                heats[x][ny] -= sub
                heats[x][y] += sub
            else:
                heats[x][ny] += sub
                heats[x][y] -= sub

    for x in range(r):
        for y in range(c):
            maps[x][y] += heats[x][y]
    minus_one()
    

def cnt_choc():
    for x, y in checked_pos:
        if maps[x][y] < k:
            return False
    return True

visited = [[False] * c for _ in range(r)]
cnt = 1
init_map()
while cnt <= 100:
    blow_heater()
    spread_heat()
    if cnt_choc():
        break
    cnt += 1
print(cnt)
print(maps)