# 6: 00 - 6:26
def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for j in combination(arr[i+1:], r - 1):
                yield [arr[i]] + j

n, m = map(int, input().split())
maps = []
virus = []
tot = 0
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 2:
            virus.append([i, j])
        elif tmp[j] == 0:
            tot += 1
    maps.append(tmp)

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def bfs(q):
    visited = [[False] * n for _ in range(n)]
    max_val = 0
    t = 0
    nq = deque()
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        nq.append([x, y, 0])

    while nq:
        x, y, c = nq.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                if maps[nx][ny] == 1:
                    continue
                nq.append([nx, ny, c + 1])
                if maps[nx][ny] == 0:
                    max_val = max(max_val, c + 1)
                    t += 1
    if tot == t:
        return max_val
    else:
        return 1e20

from collections import deque
ans = 1e20
for arr in combination(virus, m):
    q = deque(arr)
    k = bfs(q)
    if k != 1e20:
        ans = min(ans, k)

print(ans if ans != 1e20 else -1)