import sys
import copy
n, m = map(int, input().split())

dir = [[],
        [[[1, 0]], [[-1, 0]], [[0, 1]], [[0, -1]]],
        [[[-1, 0], [1, 0]], [[0, -1], [0, 1]]],
        [[[-1, 0], [0, 1]], [[0, 1], [1, 0]], [[1, 0], [0, -1]], [[0, -1], [-1, 0]]],
        [[[1, 0], [-1, 0], [0, 1]], [[1, 0], [-1, 0], [0, -1]], [[0, 1], [0, -1], [1, 0]], [[0, 1], [0, -1], [-1, 0]]],
        [[[1, 0], [-1, 0], [0, 1], [0, -1]]]]

def fill(_info, direction, y, x):
    for d in direction:
        nx, ny = x, y
        while True:
            nx += d[0]
            ny += d[1]
            
            if 0 <= nx < m and 0 <= ny < n and _info[ny][nx] != 6:
                if _info[ny][nx] == 0:
                        _info[ny][nx] = '#'
            else:
                break

def dfs(info, cnt):
    global ans
    global cctv
    _info = copy.deepcopy(info)
    
    if cnt == len(cctv):
        c = 0
        for i in _info:
            c += i.count(0)
        ans = min(ans, c)
        return

    y, x, v = cctv[cnt]
    for i in dir[v]:
        fill(_info, i, y, x)
        dfs(_info, cnt + 1)
        _info = copy.deepcopy(info)


info = []
cctv = []
ans = sys.maxsize
for i in range(n):
    tmp = list(map(int, input().split()))
    info.append(tmp)
    for j, v in enumerate(tmp):
        if v != 0 and v != 6:
            cctv.append([i, j, v])

dfs(info, 0)
print(ans)