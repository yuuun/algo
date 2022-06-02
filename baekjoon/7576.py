from collections import deque
m, n = map(int, input().split())
maps = []
n_totmato = 0
totmato = deque()
for i in range(n):
    tmp = list(map(int, input().split()))
    for j, t in enumerate(tmp):
        if t == 1:
            totmato.append([i, j])
        elif t == 0:
            n_totmato += 1

    maps.append(tmp)

ans = 0
dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]
while n_totmato > 0 and totmato:
    x, y = totmato.popleft()
    ans = max(ans, maps[x][y])
    c = maps[x][y] + 1
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if maps[nx][ny] == 0:
                totmato.append([nx, ny])
                maps[nx][ny] = c
                n_totmato -= 1

if n_totmato == 0:
    print(ans)
else:
    print(-1)