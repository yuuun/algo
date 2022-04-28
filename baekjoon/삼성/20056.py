# 1:45 - 2:06
n, m, k = map(int, input().split())
maps = [[[] for _ in range(n)] for _ in range(n)]
dxy = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
fires = []
for _ in range(m):
    r, c, m, s, d =  map(int, input().split())
    maps[r - 1][c - 1].append([m, s, d])

def move_first():
    new_maps = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for m, s, d in maps[i][j]:
                nx, ny = (i + s * dxy[d][0]) % n, (j + s * dxy[d][1]) % n
                new_maps[nx][ny].append([m, s, d])
    return new_maps

def move_second():
    for i in range(n):
        for j in range(n):
            if len(maps[i][j]) > 1:
                tm, ts = 0, 0
                td1, td2 = 0, 0
                for m, s, d in maps[i][j]:
                    tm += m
                    ts += s
                    if d % 2 == 0:
                        td1 += 1
                    else:
                        td2 += 1
                
                tm = tm // 5
                if tm == 0:
                    maps[i][j] = []
                    continue
                ts = ts // len(maps[i][j])
                if td1 == 0 or td2 == 0:
                    dd = [0, 2, 4, 6]
                else:
                    dd = [1, 3, 5, 7]
                maps[i][j] = []
                for d in dd:
                    maps[i][j].append([tm, ts, d])


for _ in range(k):
    maps = move_first()
    move_second()

ans = 0
for i in range(n):
    for j in range(n):
        for m, _, _ in maps[i][j]:
            ans += m
print(ans)