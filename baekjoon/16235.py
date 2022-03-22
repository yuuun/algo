# 4: 30 - 5:30
from collections import deque
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
maps = [[5] * n for _ in range(n)]
tree = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    r, c, t = map(int, input().split())
    tree[r - 1][c - 1].append(t)

def spring_summer():
    for i in range(n):
        for j in range(n):
            len_tree = len(tree[i][j])
                
            for k in range(len_tree):
                if tree[i][j][k] <= maps[i][j]:
                    maps[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                else:
                    for _ in range(k, len_tree):
                        maps[i][j] += tree[i][j].pop() // 2
                    break

dxy = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
def fall_winter():
    for i in range(n):
        for j in range(n):
            for z in tree[i][j]:
                if z % 5 == 0:
                    for dx, dy in dxy:
                        x = i + dx
                        y = j + dy
                        if 0 <= x < n and 0 <= y < n:
                            tree[x][y].appendleft(1)
            maps[i][j] += arr[i][j]

def cnt_tree():
    cnt = 0
    for i in range(n):
        for j in range(n):
            cnt += len(tree[i][j])
    return cnt

while k > 0:
    spring_summer()
    fall_winter()
    k -= 1
print(cnt_tree())