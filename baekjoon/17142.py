from collections import deque
n, m = map(int, input().split())
maps = []
virus = []
empty = []
visited = [[False] * n for _ in range(n)]
for i in range(n):
    row = list(map(int, input().split()))
    for j, r in enumerate(row):
        if r == 2:
            virus.append([i, j])
        elif r == 1:
            visited[i][j] = True
        else:
            empty.append([i, j])
    maps.append(row)
del row
if len(empty) == 0:
    print(0)
    exit()

def combination(arr, k):
    for i in range(len(arr)):
        if k == 1:
            yield [arr[i]]
        else:
            for j in combination(arr[i + 1:], k - 1):
                yield [arr[i]] + j

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def spread_virus(virus_list):
    _visited = [[v for v in vis] for vis in visited]
    q = deque()
    for v in virus_list:
        q.append(v + [0])
        _visited[v[0]][v[1]] = True
    while q:
        x, y, cnt = q.popleft()
        if maps[x][y] == 0:
            candidate.add(cnt)
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and not _visited[nx][ny]:
                _visited[nx][ny] = True
                q.append([nx, ny, cnt + 1])
    
    for x, y in empty:
        if not _visited[x][y]:
            return False
    return True

min_val = n ** 2
for virus_list in combination(virus, m):
    candidate = set()
    if spread_virus(virus_list):
        if candidate:
            min_val = min(min_val, max(candidate))
print(min_val if min_val != n ** 2 else -1)