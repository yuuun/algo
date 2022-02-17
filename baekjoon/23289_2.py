from collections import deque
r, c, k = map(int, input().split())

checked_pos = [] # 체크할 온풍기 위치
heater = [] # 온풍기 위치 ([온풍기 위치x, 온풍기 위치y, 방향])

for i in range(r):
    tmp = list(map(int, input().split()))
    for j, t in enumerate(tmp):
        if t == 0:
            continue    
        if 0 < t < 5:
            heater.append([i, j, t])
        else:
            checked_pos.append([i, j])

walls = [[[False] * 5 for _ in range(c)] for _ in range(c)] # 허수, 오른, 왼, 위, 아래

for _ in range(int(input())):
    x, y, t = map(int,  input().split())
    x -= 1
    y -= 1
    if t == 0:
        walls[x][y][3] = True
        walls[x - 1][y][4] = True
    if t == 1:
        walls[x][y][1] = True
        walls[x][y + 1][2] = True
        
maps = [[0] * c for _ in range(r)]

dxys = [[], [[-1, 1], [0, 1], [1, 1]], [[-1, -1], [0, -1], [1, -1]], [[-1, -1], [-1, 0], [-1, 1]], [[1, -1], [1, 0], [1, 1]]]

def iscriteria(x, y):
    if 0 <= x < r and 0 <= y < c:
        return True
    return False

def isnext(x, y, t, idx):
    if idx == 1:
        if walls[x][y][t]:
            return False
        else:
            return True
    
    if walls[x][y][t]:
        return False
    if t < 3:
        if idx == 0:
            if walls[x][y][3]:
                return False
        if idx == 2:
            if walls[x][y][4]:
                return False
    else:
        if idx == 0:
            if walls[x][y][2]:
                return False
        if idx == 2:
            if walls[x][y][1]:
                return False
    return True
        
def init_heater():
    added_heater = [[0] * c for _ in range(r)]
    for x, y, t in heater:
        x += dxys[t][1][0]
        y += dxys[t][1][1]
        q = deque()
        q.append([x, y, 4])
        global visited
        
        visited = [[False] * c for _ in range(r)]
        visited[x][y] = True
        added_heater[x][y] += 5
        
        while q:
            print(q)
            x, y, cnt = q.popleft()
            for idx, dxy in enumerate(dxys[t]):
                if 0 < cnt and isnext(x, y, t, idx):
                    nx, ny = x + dxy[0], y + dxy[1]
                    if iscriteria(nx, ny) and not visited[nx][ny]:
                        added_heater[nx][ny] += cnt
                        
                        q.append([nx, ny, cnt - 1])
                        visited[nx][ny] = True
        print(added_heater)
    return added_heater

def update_heater():
    global added_heater
    for i in range(r):
        for j in range(c):
            maps[i][j] += added_heater[i][j]

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
            
# def spread_heat():
#     heats = [[0] * c for _ in range(r)]
#     for x in range(r - 1):
#         nx = x + 1
#         for y in range(c - 1):
#             if iscriteria(nx, y):
#                 if up_walls[nx][y] < 0:
#                     sub = abs(maps[nx][y] - maps[x][y]) // 4
#                     if maps[nx][y] > maps[x][y]:
#                         heats[nx][y] -= sub
#                         heats[x][y] += sub
#                     else:
#                         heats[nx][y] += sub
#                         heats[x][y] -= sub
            
#             if iscriteria(x, y):
#                 if right_walls[x][y] < 0:
#                     ny = y + 1
#                     sub = abs(maps[x][ny] - maps[x][y]) // 4
#                     if maps[x][ny] > maps[x][y]:
#                         heats[x][ny] -= sub
#                         heats[x][y] += sub
#                     else:
#                         heats[x][ny] += sub
#                         heats[x][y] -= sub
#     y = c - 1
#     for x in range(1, r):
#         nx = x - 1
#         if up_walls[x][y] < 0:
#             sub = abs(maps[nx][y] - maps[x][y]) // 4
#             if maps[nx][y] > maps[x][y]:
#                 heats[nx][y] -= sub
#                 heats[x][y] += sub
#             else:
#                 heats[nx][y] += sub
#                 heats[x][y] -= sub

#     for x in range(r):
#         for y in range(c):
#             maps[x][y] += heats[x][y]
#     minus_one()
    

# def cnt_choc():
#     for x, y in checked_pos:
#         if maps[x][y] < k:
#             return False
#     return True

visited = [[False] * c for _ in range(r)]
cnt = 1
added_heater = init_heater()
print(added_heater)
# while cnt <= 100:
#     update_heater()
#     print(maps)
    # spread_heat()
    # if cnt_choc():
    #     break
    # cnt += 1
print(cnt)
print(maps)