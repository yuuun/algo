n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]

dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]
cnt = n * m

for x in range(n):
    for y in range(m):
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if maps[x][y] != maps[nx][ny]:
                    cnt -= 1
                    break
print((1 << (cnt)) % 1000000007)

'''

from sys import stdin
n, m = map(int, stdin.readline().split())
lattice = stdin.readlines()
count = 1
for y in range(n):
    for x in range(m):
        same = True
        if x > 0:
            same = same and lattice[y][x] == lattice[y][x - 1]
        if y > 0:
            same = same and lattice[y][x] == lattice[y - 1][x]
        if x < m - 1:
            same = same and lattice[y][x] == lattice[y][x + 1]
        if y < n - 1:
            same = same and lattice[y][x] == lattice[y + 1][x]
        if same:
            count = (count * 2) % 1000000007
print(count)
'''