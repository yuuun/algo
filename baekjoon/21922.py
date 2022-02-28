from collections import deque
n, m = map(int, input().split())
maps = []
visited = [[False] * m for _ in range(n)]
q = deque() # row, col, direction
for i in range(n):
    tmp = list(map(int, input().split()))
    for j, t in enumerate(tmp):
        if t == 9:
            q.append([i, j, [0, 1, 2, 3]])
            visited[i][j] = True
    maps.append(tmp)

dxy = [[1, 0], [-1, 0], [0, -1], [0, 1]] # 아래, 위, 왼, 오른쪽 방향으로 

changed_direction = [[], [0, 1, -1, -1],
                        [-1, -1, 2, 3],
                        [2, 3, 0, 1],
                        [3, 2, 1, 0]]

while q:
    x, y, dire = q.popleft()
    for i in dire:
        nx, ny = x + dxy[i][0], y + dxy[i][1]
        while 0 <= nx < n and 0 <= ny < m:
            cur = maps[nx][ny]
            if cur == 9:
                break
            visited[nx][ny] = True
            
            if cur:
                if changed_direction[cur][i] != -1:
                    i = changed_direction[cur][i]
                else:
                    break
            nx, ny = nx + dxy[i][0], ny + dxy[i][1]
cnt = 0
for vi in visited:
    cnt += vi.count(True)
print(cnt)