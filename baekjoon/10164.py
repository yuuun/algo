n, m, k = map(int, input().split())
x, y = k // m, k % m
if y != 0:
    y -= 1
else:
    if x != 0:
        x -= 1
        y = m - 1

def cnt(r, c):
    maps = [[1] * c for _ in range(r)]
    maps[0][0] = 1
    for i in range(1, r):
        for j in range(1, c):
            maps[i][j] = maps[i][j - 1] + maps[i - 1][j]
    return maps[-1][-1]

print(cnt(x + 1, y + 1) * cnt(n - x, m - y))