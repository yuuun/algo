n, m, p = map(int, input().split())
maps = []
bx, by = 0, 0
for i in range(n):
    tmp = list(input())
    for j in range(m):
        if tmp[j] == 'B':
            bx, by = i, j
    maps.append(tmp)


from collections import deque, defaultdict
q = deque()
q.append([bx, by])
visited = [[-1] * m for _ in range(n)]
visited[bx][by] = 0
dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]
loc = defaultdict(list)
while q:
    x, y = q.popleft()
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == -1:
                if maps[nx][ny] != 'X':
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])
                    if maps[nx][ny] != '.':
                        loc[visited[nx][ny]].append(maps[nx][ny])
    
loc = {k: v for k, v in sorted(loc.items(), key=lambda x:x[0])}
t = 1
tmp = 0

power = {}
for _ in range(p):
    a, b = input().split()
    power[a] = int(b)
total = int(input())

cnt = 0
while total > 0:
    if t in loc:
        for k in loc[t]:
            tmp += power[k]
            cnt += 1
    total -= tmp
    t += 1

print(cnt)