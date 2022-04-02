n, m = map(int, input().split())
def combination(arr, k):
    for i in range(len(arr)):
        if k == 1:
            yield [arr[i]]
        else:
            for j in combination(arr[i + 1:], k - 1):
                yield [arr[i]] + j

maps = []
stores = []
total_house = 0

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 2: # 치킨집일 때
            stores.append([i, j, 1])
        elif tmp[j] == 1:
            total_house += 1
    maps.append(tmp)

from collections import deque
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def bfs(store):
    q = deque(store)
    visited = [[False] * n for _ in range(n)]
    
    ans = 0
    cnt_house = 0
    while q:
        x, y, cnt = q.popleft()
        visited[x][y] = True
        if cnt > min_val:
            return False
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    if maps[nx][ny] == 1:
                        ans += cnt
                        cnt_house += 1
                    if cnt_house == total_house:
                        return ans
                    q.append([nx, ny, cnt + 1])
    return ans

min_val = 1e10
for store in combination(stores, m):
    tmp = bfs(store)
    if tmp:
        min_val = min(min_val, tmp)
print(min_val)