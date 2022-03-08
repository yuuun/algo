from copy import deepcopy
m, s = map(int, input().split())

dxy = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
sxy = [[-1, 0], [0, -1], [1, 0], [0, 1]] # 상, 좌, 하, 우
maps = [[[] for _ in range(4)] for _ in range(4)]

for _ in range(m):
    x, y, d = map(int, input().split())
    maps[x - 1][y - 1].append(d - 1)

sx, sy = map(int, input().split())
sx -= 1
sy -= 1
smell = [[0] * 4 for _ in range(4)]

def move_fish():
    moved_fish = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            while new_map[x][y]:
                d = new_map[x][y].pop()
                for i in range(d, d - 8, -1):
                    i %= 8
                    nx, ny = x + dxy[i][0], y + dxy[i][1]
                    if [nx, ny] != [sx, sy] and 0 <= nx < 4 and 0 <= ny < 4 and not smell[nx][ny]:
                        moved_fish[nx][ny].append(i)
                        break
                else:
                    moved_fish[x][y].append(d)
    return moved_fish

def move_shark(x, y, cnt, depth, visited):
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
                move_shark(nx, ny, cnt + len(new_map[nx][ny]), depth + 1, visited)
                visited.pop()
            else:
                move_shark(nx, ny, cnt, depth + 1, visited)


for _ in range(s):
    new_map = deepcopy(maps)
    new_map = move_fish()
    max_val = -1
    final = []
    move_shark(sx, sy, 0, 0, [])
    
    for x, y in final:
        if new_map[x][y]:
            new_map[x][y] = []
            smell[x][y] = 3

    for i in range(4):
        for j in range(4):
            if smell[i][j] > 0:
                smell[i][j] -= 1
    
    # 5
    for i in range(4):
        for j in range(4):
            maps[i][j] += new_map[i][j]

ans = 0
for i in range(4):
    for j in range(4):
        ans += len(maps[i][j])
print(ans)