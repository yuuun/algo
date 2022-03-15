# 50분 소요
r, c, m = map(int, input().split())
sharks = [[[] for _ in range(c)] for _ in range(r)]
dxy = [[-1, 0], [1, 0], [0, 1], [0, -1]] #위, 아래, 오른, 왼
for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    sharks[x - 1][y - 1].append([s, d - 1, z]) # 속도, 방향, 크기

total_shark = 0
def get_shark(idx):
    global total_shark
    for j in range(r):
        if sharks[j][idx]:
            shark = sharks[j][idx].pop()
            total_shark += shark[-1]
            return
    return

mod_r = 2 * r - 2
mod_c = 2 * c - 2
def move_shark():
    new_shark = [[[] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if sharks[i][j]:
                s, d, z = sharks[i][j].pop()
                if d < 2:
                    x = (i + s * dxy[d][0]) % mod_r
                    if x < r:
                        new_shark[x][j].append([s, d, z])
                    else:
                        x = mod_r - x
                        new_shark[x][j].append([s, 1 - d, z])
                else:
                    y = (j + s * dxy[d][1]) % mod_c
                    if y < c:
                        new_shark[i][y].append([s, d, z])
                    else:
                        y = mod_c - y
                        new_shark[i][y].append([s, 5 - d, z])

    return new_shark


def eat_shark():
    for i, row in enumerate(sharks):
        for j, shark in enumerate(row):
            if len(shark) > 1:
                shark = sorted(shark, key=lambda x: -x[2])
                sharks[i][j] = [shark[0]]

idx = 0
while idx < c:
    get_shark(idx)
    idx += 1
    sharks = move_shark()
    eat_shark()
print(total_shark)