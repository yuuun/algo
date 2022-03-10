n, m = map(int, input().split())
maps = [[0] * (m + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

for i in range(n + 1):
    for j in range(1, m + 1):
        maps[i][j] += maps[i][j - 1]

for j in range(m + 1):
    for i in range(1, n + 1):
        maps[i][j] += maps[i - 1][j]
for _ in range(int(input())):
    i, j, x, y = list(map(int, input().split()))
    i -= 1
    j -= 1
    print(maps[x][y] - maps[i][y] - maps[x][j] + maps[i][j])