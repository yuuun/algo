# TBD
n, m, k = map(int, input().split())
maps = []
shark = {}
for i in range(n):
    tmp = list(map(int, input().split()))
    lis = []
    for j in range(n):
        if tmp[j] == 0:
            lis.append([])
        else:
            t = tmp[j] - 1
            lis.append([t, k])
            shark[t] = [i, j]
    maps.append(lis)

dshark = list(map(lambda x: int(x) - 1, input().split()))
dirshark = []
dxy = [[-1, 0], [0, -1], [1, 0], [0, 1]] # 위, 왼, 아래, 오른
for i in range(1, m + 1):
    tmp = []
    for _ in range(4):
        tmp.append(list(map(lambda x:int(x) - 1, input().split())))
    dirshark.append(tmp)

def move_shark():
    for i in range(m):
        x, y = shark[i]
        second = []
        d = dshark[i]
        flag = False
        for dd in dirshark[i][d]:
            nx, ny = x + dxy[dd][0], y + dxy[dd][1]
            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] == []:
                    maps[nx][ny] = [i, k + 1]
                    flag = True
                    shark[i] = [nx, ny]
                    break
                elif maps[nx][ny][0] == i:
                    second.append([nx, ny])
        
        if not flag:
            nx, ny = second[0]
            maps[nx][ny] = [i, k + 1]
            flag = True
            shark[i] = [nx, ny]
        print(shark)
    return
time = 0
print(maps)
while time < 1001:
    move_shark()

    for i in range(n):
        for j in range(n):
            if len(maps[i][j]) > 0:
                maps[i][j][1] -= 1
    time += 1

print(time if time != 1001 else -1)