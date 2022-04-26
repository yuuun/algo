# 5:25 - 6:00
# 미세먼지 안녕!
r, c, t = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(r)]
for i in range(r):
    if maps[i][0] == -1:
        air = i
        break

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def spread_dust():
    cnt_list = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if maps[x][y] == -1:
                continue
            tmp_5 = maps[x][y] // 5
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] != -1:
                    cnt_list[x][y] -= tmp_5
                    cnt_list[nx][ny] += tmp_5
    for x in range(r):
        for y in range(c):
            maps[x][y] += cnt_list[x][y]
    return

def rotate_upair():
    for x in range(air - 1, 0, -1):
        maps[x][0] = maps[x - 1][0]
    for y in range(c - 1):
        maps[0][y] = maps[0][y + 1]
    for x in range(air):
        maps[x][-1] = maps[x + 1][-1]
    for y in range(c - 1, 1, -1):
        maps[air][y] = maps[air][y - 1]
    maps[air][1] = 0
    return

def rotate_downair():
    air2 = air + 1

    for x in range(air2 + 1, r - 1):
        maps[x][0] = maps[x + 1][0]
    for y in range(c - 1):
        maps[-1][y] = maps[-1][y + 1]
    for x in range(r - 1, air2, -1):
        maps[x][-1] = maps[x - 1][-1]
    for y in range(c - 1, 1, -1):
        maps[air2][y] = maps[air2][y - 1]
    maps[air2][1] = 0
    return

for _ in range(t):
    spread_dust()
    rotate_upair()
    rotate_downair()
print(sum(sum(i) for i in maps) + 2)