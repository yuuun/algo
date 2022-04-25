m, s = map(int, input().split())
dxy = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
sxy = [[-1, 0], [0, -1], [1, 0], [0, 1]]

maps = [[[] for _ in range(4)] for _ in range(4)]
for _ in range(m):
    x, y, d = map(lambda x:int(x) - 1, input().split())
    maps[x][y].append(d)
sx, sy = map(int, input().split())
sx -= 1
sy -= 1
smell = [[0] * 4 for _ in range(4)]

def deepcopy(arr):
    return [[a for a in ar] for ar in arr]

def move_fish():
    global _maps
    _maps = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            for t in maps[x][y]:
                for i in range(t, t - 8, -1):
                    i %= 8
                    nx, ny = x + dxy[i][0], y + dxy[i][1]
                    if 0 <= nx < 4 and 0 <= ny < 4 and not (sx == nx and sy == ny) and smell[nx][ny] == 0:
                        _maps[nx][ny].append(i)
                        break
                else:
                    _maps[x][y].append(t)


def move_shark(depth, x, y, cnt, visited):
    global max_val, sx, sy, final
    if depth == 3:
        if max_val < cnt:
            sx, sy = x, y
            max_val = cnt
            final = visited[:]
        return
    
    for dx, dy in sxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            if [nx, ny] not in visited:
                visited.append([nx, ny])
                move_shark(depth + 1, nx, ny, cnt + len(_maps[nx][ny]), visited)
                visited.pop()
            else:
                move_shark(depth + 1, nx, ny, cnt, visited)

def remove_smell():
    for x in range(4):
        for y in range(4):
            if smell[x][y] > 0:
                smell[x][y] -= 1
    
    for x, y in final:
        if _maps[x][y] != []:
            _maps[x][y] = []
            smell[x][y] = 2

def add_fish():
    for x in range(4):
        for y in range(4):
            maps[x][y].extend(_maps[x][y])

def count_fish():
    ans = 0
    for x in range(4):
        for y in range(4):
            ans += len(maps[x][y])
    return ans

for _ in range(s):
    move_fish()
    final = []
    max_val = -1
    move_shark(0, sx, sy, 0, [])
    remove_smell()
    add_fish()
print(count_fish())