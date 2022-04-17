# TBD
n, m = map(int, input().split())
dxys = [[[0, 1], [0], [0]], [[0], [0, 1, 2]], [[1], [1], [0, 1]], [[0, 1, 2], [2]], [[0, 1], [1], [1]], [[2], [0, 1, 2]], [[0], [0], [0, 1]], [[0, 1, 2], [0]],
         [[0, 1], [0, 1]],
         [[0, 1, 2, 3]], [[0], [0], [0], [0]],
         [[1], [0, 1], [0]], [[0], [0, 1], [1]], [[1, 2], [0, 1]], [[0, 1], [1, 2]],
         [[0, 1, 2], [1]], [[1], [0, 1, 2]], [[0], [0, 1], [0]], [[1], [0, 1], [1]]]

maps = [list(map(int, input().split())) for _ in range(n)]
ans = []
def cnt_score(dxy):
    for i in range(len(dxy)):
        for j in dxy[i]:
            for y in range(m - len(dxy[j])):
                return

for dxy in dxys:
    if n > len(dxy):
        continue
    tot = 0
    