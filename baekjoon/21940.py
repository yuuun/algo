import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
nPlusOne = n + 1

maps = [[INF] * nPlusOne for _ in range(nPlusOne)]
for i in range(1, nPlusOne):
    maps[i][i] = 0 

for _ in range(m):
    a, b, t = map(int, input().split())
    maps[a][b] = t

k = int(input())
lived = list(map(int, input().split()))

for a in range(1, nPlusOne):
    for i in range(1, nPlusOne):
        for j in range(i + 1, nPlusOne):
            maps[i][j] = min(maps[i][j], maps[i][a] + maps[a][j])
            maps[j][i] = min(maps[j][i], maps[j][a] + maps[a][i])

min_val = INF
min_list = []
for city in range(1, nPlusOne):
    max_val = []
    for a in lived:
        max_val.append(maps[city][a] + maps[a][city])
    max_val = max(max_val)

    if max_val == min_val:
        min_list.append(city)

    elif max_val < min_val:
        min_val = max_val
        min_list = [city]


print(' '.join(map(str, min_list)))