# 52분 소요

from collections import deque
n, q = map(int, input().split())
ice_size = 2 ** n
ice = [list(map(int, input().split())) for _ in range(ice_size)]
lstep = list(map(int, input().split()))

def rotate_ice(l):
    k = 2 ** l
    for x in range(0, ice_size, k):
        for y in range(0, ice_size, k):
            tmp = [ice[i][y:y + k] for i in range(x, x + k)]
            
            for i in range(k):
                for j in range(k):
                    ice[x + j][y + k - 1 - i] = tmp[i][j]

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def remove_ice():
    del_list = []
    for x in range(ice_size):
        for y in range(ice_size):
            if ice[x][y] > 0:
                cnt = 0
                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < ice_size and 0 <= ny < ice_size:
                        if ice[nx][ny] > 0:
                            cnt += 1
                if cnt < 3:
                    del_list.append([x, y])
    
    for x, y in del_list:
        ice[x][y] -= 1

def find_big_ice():
    visited = [[False] * ice_size for _ in range(ice_size)]
    n_size = []
    sum_ice = 0

    def bfs(x, y):
        cnt = 0
        q = deque()
        q.append([x, y])
        while q:
            x, y = q.popleft()
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if 0 <= nx < ice_size and 0 <= ny < ice_size:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        if ice[nx][ny] > 0:
                            cnt += 1
                            q.append([nx, ny])
        return cnt

    for i in range(ice_size):
        for j in range(ice_size):
            sum_ice += ice[i][j]
            if not visited[i][j]:
                visited[i][j] = 0
                if ice[i][j] > 0:
                    n_size.append(bfs(i, j))
    
    if len(n_size) == 0:
        return 0, sum_ice
    return max(n_size), sum_ice
    
for l in lstep:
    if l > 0:
        rotate_ice(l)
    remove_ice()

num_ice, sum_ice = find_big_ice()
print(sum_ice)
print(num_ice)