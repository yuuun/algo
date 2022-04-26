# 6:00 - 6:37
n, q = map(int, input().split())
n_2 = 1 << n
maps = [list(map(int, input().split())) for _ in range(n_2)]

def rotate90(arr):
    return [list(elem) for elem in zip(*arr[::-1])]

def do_magic(l):
    l_2 = 1 << l
    for x in range(0, n_2, l_2):
        for y in range(0, n_2, l_2):
            arr = [maps[t][y:y + l_2] for t in range(x, x + l_2)]
            arr = rotate90(arr)
            for i1, i2 in zip(range(x, x + l_2), range(l_2)):
                for j1, j2 in zip(range(y, y + l_2), range(l_2)):
                    maps[i1][j1] = arr[i2][j2]

dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]
def reduce_ice():
    cnt_list = [[0] * n_2 for _ in range(n_2)]
    for x in range(n_2):
        for y in range(n_2):
            if maps[x][y] > 0:
                for dx, dy in dxy[:2]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < n_2 and 0 <= ny < n_2 and maps[nx][ny] > 0:
                        cnt_list[x][y] += 1
                        cnt_list[nx][ny] += 1
    
    for x in range(n_2):
        for y in range(n_2):
            if cnt_list[x][y] < 3 and maps[x][y] > 0:
                maps[x][y] -= 1

from collections import deque
def calculate_ice():
    visited = [[False] * n_2 for _ in range(n_2)]
    ans = 0
    tot = 0
    for i in range(n_2):
        for j in range(n_2):
            if maps[i][j] == 0:
                visited[i][j] = True
                continue
            if not visited[i][j]:
                q = deque()
                q.append([i, j])
                cnt = 1
                visited[i][j] = True
                tot += maps[i][j]
                while q:
                    x, y = q.popleft()
                    for dx, dy in dxy:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n_2 and 0 <= ny < n_2 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            if maps[nx][ny] > 0:
                                cnt += 1
                                q.append([nx, ny])
                                tot += maps[nx][ny]
                ans = max(ans, cnt)
    return ans, tot


for l in map(int, input().split()):
    do_magic(l)
    reduce_ice()

ans, tot = calculate_ice()
print(tot)
print(ans)