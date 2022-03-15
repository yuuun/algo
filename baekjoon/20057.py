# 실패!
from collections import deque
n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
k = n // 2
dxy = [[0, -1], [1, 0], [0, 1], [-1, 0]]

i, cnt = 0, 1
d = -1
ans = 0

def move_wind(x, y):
    global ans

    dx, dy = dxy[d]
    # print(x, y, d, dx, dy)
    nx1, ny1 = x + dx, y + dy
    nx2, ny2 = nx1 + dx, ny1 + dy
    nx3, ny3 = nx2 + dx, ny2 + dy
    value = maps[nx1][ny1]
    tot = 0
    if d % 2 == 0: # 왼쪽 오른쪽으로 이동
        tmp = int(value * 0.01)
        tot += 2 * tmp
        for tx in [x + 1, x - 1]:
            if 0 <= tx < n:
                maps[tx][y] += tmp
            else:
                ans += tmp
        
        tmp = int(value * 0.07)
        tot += 2 * tmp
        for tx in [x + 1, x - 1]:
            if 0 <= ny1 < n and 0 <= tx < n:
                maps[tx][ny1] += tmp
            else:
                ans += tmp
        
        tmp = int(value * 0.02)
        tot += 2 * tmp
        for tx in [x + 2, x - 2]:
            if 0 <= ny1 < n and 0 <= tx < n:
                maps[tx][ny1] += tmp
            else:
                ans += tmp
    
        tmp = int(value * 0.1)
        tot += 2 * tmp
        for tx in [x + 1, x - 1]:
            if 0 <= ny2 < n and 0 <= tx < n:
                maps[tx][ny2] += tmp
            else:
                ans += tmp

        if 0 <= ny3 < n:
            maps[x][ny3] = int(value * 0.05)
    else:
        tmp = int(value * 0.01)
        tot += 2 * tmp
        for ty in [y + 1, y - 1]:
            if 0 <= ty < n:
                maps[x][ty] += tmp
            else:
                ans += tmp
        
        tmp = int(value * 0.07)
        tot += 2 * tmp
        for ty in [y + 1, y - 1]:
            if 0 <= nx1 < n and 0 <= ty < n:
                maps[nx1][ty] += tmp
            else:
                ans += tmp
        
        tmp = int(value * 0.02)
        tot += 2 * tmp
        for ty in [y + 2, y - 2]:
            if 0 <= nx1 < n and 0 <= ty < n:
                maps[nx1][ty] += tmp
            else:
                ans += tmp
    
        tmp = int(value * 0.1)
        tot += 2 * tmp
        for ty in [y + 1, y - 1]:
            if 0 <= nx2 < n and 0 <= ty < n:
                maps[nx2][ty] += tmp
            else:
                ans += tmp
        tmp = int(value * 0.05)
        tot += tmp
        if 0 <= nx3 < n:
            maps[nx3][y] = tmp
        else:
            ans += tmp
    
    tmp = value - tot
    if 0 <= nx3 < n and 0 <= ny3 < n:
        maps[nx3][ny3] = tmp
    else:
        ans += tmp

def get_index():
    sx, sy = k, k
    size_map = n ** 2
    cnt = 1
    idx = 1
    q = deque()
    while size_map > idx:
        for i in range(4):
            t = 0
            while t < cnt and size_map > idx:
                sx += dxy[i][0]
                sy += dxy[i][1]
                q.append([sx, sy, i])
                t += 1
                idx += 1
            if i in [1, 3]:
                cnt += 1
    return q

q = get_index()
while q:
    x, y, t = q.popleft()
    move_wind(x, y)
    d = t
    
print(maps, ans)