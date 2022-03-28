dxy = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]

maps = []
fish = [[] for _ in range(17)] # x, y, direction
for k in range(4):
    map_tmp = []
    tmp = list(map(int, input().split()))
    for i, j in zip(range(0, 8, 2), range(1, 8, 2)):
        size = tmp[i]
        dir = tmp[j] - 1
        map_tmp.append([size, dir])
        i //= 2
        fish[size] = [k, i]
        
    maps.append(map_tmp)
    
def move_fish(sx, sy):
    for i in range(1, 17):
        if fish[i]:
            x, y = fish[i]

            for _ in range(8):
                nx, ny = x + dxy[maps[x][y][1]][0], y + dxy[maps[x][y][1]][1]
                if not 0 <= nx < 4 or not 0 <= ny < 4 or (nx == sx and ny == sy):
                    maps[x][y][1] = (maps[x][y][1] + 1) % 8
                    continue
                fish[i] = [nx, ny]
                if maps[nx][ny] != []:
                    fish[maps[nx][ny][0]] = [x, y]
                maps[nx][ny], maps[x][y] = maps[x][y], maps[nx][ny]
                break

def deepcopy(arr):
    if len(arr) == 17:
        return [[a for a in ar] for ar in arr]
    return [[[i for i in a] for a in ar] for ar in arr]

def dfs(x, y, d, cnt):
    global ans, maps, fish
    move_fish(x, y)
    while True:
        nx, ny = x + dxy[d][0], y + dxy[d][1]
        if not (0 <= nx < 4 and 0 <= ny < 4):
            ans = max(ans, cnt)
            return
        if not maps[nx][ny]:
            x, y = nx, ny
            continue
        
        tmp_fish, tmp_map = deepcopy(fish), deepcopy(maps)
        remove1, remove2 = fish[maps[nx][ny][0]], maps[nx][ny]
        fish[maps[nx][ny][0]], maps[nx][ny] = [], []
        dfs(nx, ny, remove2[1], cnt + remove2[0])
        fish, maps = tmp_fish, tmp_map
        fish[maps[nx][ny][0]], maps[nx][ny] = remove1, remove2
        x, y = nx, ny

ans = 0
sx, sy = 0, 0
idx = maps[sx][sy][0]
cnt = idx
sd = maps[sx][sy][1]
fish[idx] = []
maps[sx][sy] = []

dfs(0, 0, sd, cnt)
print(ans)