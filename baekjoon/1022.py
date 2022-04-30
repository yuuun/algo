inp = list(map(int, input().split()))
max_val = max(map(lambda x: abs(x), inp))
r1, c1, r2, c2 = map(lambda x: x + max_val, inp)
n = 2 * max_val + 1
r2 += 1
c2 += 1

maps = [[0] * (c2 - c1) for _ in range(r2 - r1)]
x, y = n // 2, n // 2
if r1 <= x < r2 and c1 <= y < c2:
    maps[x - r1][y - c1] = 1
d = 0
cnt = 2
dxy = [[0, 1], [-1, 0], [0, -1], [1, 0]]
max_cnt = 0
def move_one(t):
    global x, y, d, cnt, max_cnt
    while t > 0:
        x += dxy[d][0]
        y += dxy[d][1]
        if r1 <= x < r2 and c1 <= y < c2:
            maps[x - r1][y - c1] = cnt
            max_cnt = max(cnt, max_cnt)
        cnt += 1
        t -= 1
    d = (d + 1) % 4

for i in range(1, n):
    move_one(i)
    move_one(i)
move_one(n - 1)
max_cnt = len(str(max_cnt))
for x in range(r2 - r1):
    for y in range(c2 - c1):
        print('%*d'%(max_cnt, maps[x][y]), end=' ')
    print()