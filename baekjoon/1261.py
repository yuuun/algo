from collections import deque
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

m,n = map(int, input().split())
room = []
for _ in range(n):
    room.append(list(map(int, input())))
dist = [[-1] * m for _ in range(n)] 


q = deque()
q.append((0,0))
dist[0][0] = 0

while q:
    x,y = q.popleft()
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if dist[nx][ny] == -1:
                if room[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx, ny))
                else:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

print(dist[n-1][m-1])