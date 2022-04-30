from collections import deque
n, m, k = map(int, input().split())
maps = [[5] * n for _ in range(n)]
tree = [[[] for _ in range(n)] for _ in range(n)]
A = [list(map(int, input().split())) for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z)

def spring_summer():
    new = [[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if tree[x][y]:
                flag = True
                for i, t in enumerate(sorted(tree[x][y])):
                    if t <= maps[x][y] and flag:
                        maps[x][y] -= t
                        new[x][y].append(t + 1)
                    else:
                        flag = False
                        maps[x][y] += t // 2
    return new

dxy = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [0, -1], [1, -1], [1, 0], [1, 1]]
def fall_winter():
    new = [[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            maps[x][y] += A[x][y]
            for t in tree[x][y]:
                new[x][y].append(t)
                if t % 5 == 0:
                    for dx, dy in dxy:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            new[nx][ny].append(1)
    return new

for kkk in range(k):
    tree = spring_summer()
    tree = fall_winter()
ans = 0
for x in range(n):
    for y in range(n):
        ans += len(tree[x][y])
print(ans)