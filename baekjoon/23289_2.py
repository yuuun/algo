# 11:56 - 1:32
from collections import deque
n, m, k = map(int, input().split())
walls = [[0] * m for _ in range(n)]
heat = [[0] * m for _ in range(n)]
chk = [] # x, y
heater = [] # 방향, x, y
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 0:
            continue
        if tmp[j] == 5:
            chk.append([i, j])
            continue
        heater.append([tmp[j] - 1, i, j])

for _ in range(int(input())):
    x, y, t = map(int, input().split())
    if t == 0: # 위쪽 벽
        walls[x - 1][y - 1] += 1
        walls[x - 2][y - 1] += 4
    else: # 오른쪽 벽
        walls[x - 1][y - 1] += 2
        walls[x - 1][y] += 8

dxy = [[0, 1], [0, -1], [-1, 0], [1, 0]] #오른, 왼, 위, 아래
def init_heat():
    global update_heat
    update_heat = [[0] * m for _ in range(n)]
    def spread_three(x, y, d):
        def iscriteria(i, j):
            if 0 <= i < n and 0 <= j < m:
                return True
            return False
        if not (0 <= x < n and 0 <= y < m):
            return []
        li = []
        if d == 0: #오른
            if iscriteria(x - 1, y):
                if iscriteria(x - 1, y + 1):
                    if walls[x - 1][y] & 4 and not walls[x - 1][y] & 2:
                        li.append([x - 1, y + 1])
            if iscriteria(x + 1, y):
                if iscriteria(x + 1, y + 1):
                    if walls[x + 1][y] & 1 and not walls[x + 1][y] & 2:
                        li.append([x + 1, y + 1])
            if iscriteria(x, y) and iscriteria(x, y + 1):
                if not walls[x][y] & 2:
                    li.append([x, y + 1])
        
        elif d == 1: #왼
            if iscriteria(x - 1, y):
                if iscriteria(x - 1, y - 1):
                    if not walls[x - 1][y] & 4 and not walls[x - 1][y] & 8:
                        li.append([x - 1, y - 1])
            if iscriteria(x + 1, y):
                if iscriteria(x + 1, y - 1):
                    if not walls[x + 1][y] & 1 and not walls[x + 1][y] & 8:
                        li.append([x + 1, y - 1])

            if iscriteria(x, y) and iscriteria(x, y - 1):
                if not walls[x][y] & 8:
                    li.append([x, y - 1])

        elif d == 2: #위
            if iscriteria(x, y - 1):
                if iscriteria(x - 1, y - 1):
                    if not walls[x][y - 1] & 2 and not walls[x][y - 1] & 1:
                        li.append([x - 1, y - 1])
            if iscriteria(x, y + 1):
                if iscriteria(x - 1, y + 1):
                    if not walls[x][y + 1] & 8 and not walls[x][y + 1] & 1:
                        li.append([x - 1, y + 1])
            if iscriteria(x, y) and iscriteria(x - 1, y):
                if not walls[x][y] & 1:
                    li.append([x - 1, y])
        
        else:       # 아래
            if iscriteria(x, y - 1):
                if iscriteria(x + 1, y - 1):
                    if not walls[x][y - 1] & 4 and not walls[x][y - 1] & 2:
                        li.append([x + 1, y - 1])
            if iscriteria(x, y + 1):
                if iscriteria(x + 1, y + 1):
                    if not walls[x][y + 1] & 4 and not walls[x][y + 1] & 8:
                        li.append([x + 1, y + 1])
            if iscriteria(x, y) and iscriteria(x + 1, y):
                if not walls[x][y] & 4:
                    li.append([x + 1, y])
        return li
        
    for d, x, y in heater:
        visited = [[False] * m for _ in range(m)]
        q = deque()
        x, y = x + dxy[d][0], y + dxy[d][1]
        q.append((x, y, 5))
        visited[x][y] = True
        while q:
            x, y, h = q.popleft()
            update_heat[x][y] += h
            if h > 1:
                cand = spread_three(x, y, d)
                for nx, ny in cand:
                    if not visited[nx][ny]:
                        q.append((nx, ny, h - 1))
                        visited[nx][ny] = True

def blow_heat():
    for i in range(n):
        for j in range(m):
            heat[i][j] += update_heat[i][j]

def spread_heat():
    added_heat = [[0] * m for _ in range(n)]
    for x in range(n - 1):
        for y in range(m - 1):
            if not walls[x][y] & 4:
                nx = x + 1
                minus = int((heat[nx][y] - heat[x][y]) / 4)
                added_heat[x][y] += minus
                added_heat[nx][y] -= minus

            if not walls[x][y] & 2:
                ny = y + 1
                minus = int((heat[x][ny] - heat[x][y]) / 4)
                added_heat[x][y] += minus
                added_heat[x][ny] -= minus

    for x in range(n - 1):
        if not walls[x][-1] & 4:
            minus = int((heat[x + 1][-1] - heat[x][-1])/ 4)
            
            added_heat[x][-1] += minus
            added_heat[x + 1][-1] -= minus

    for y in range(m - 1):
        if not walls[-1][y] & 2:
            minus = int((heat[-1][y + 1] - heat[-1][y])/ 4)
            
            added_heat[-1][y] += minus
            added_heat[-1][y + 1] -= minus
    
    for x in range(n):
        for y in range(m):
            heat[x][y] += added_heat[x][y]
                
    remove_outer_heat()

def remove_outer_heat():
    for i in range(n):
        heat[i][0] -= 1 if heat[i][0] > 0 else 0
        heat[i][-1] -= 1 if heat[i][-1] > 0 else 0
    for j in range(1, m - 1):
        heat[0][j] -= 1 if heat[0][j] > 0 else 0
        heat[-1][j] -= 1 if heat[-1][j] > 0 else 0
    return

def check_heat():
    for x, y in chk:
        if heat[x][y] < k:
            return False
    return True

eat = 1
init_heat()
while eat < 101:
    blow_heat()
    spread_heat()
    if check_heat():
        break
    eat += 1

print(eat)