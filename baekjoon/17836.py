from collections import deque
n, m, t = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def bfs():
    sword = 1e10
    q = deque()
    q.append([0, 0])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        if maps[x][y] == 2:
            sword = n - 1 - x + m - 1 - y + visited[x][y] - 1
        if x == n - 1  and y == m - 1:
            return min(sword, visited[x][y] - 1)
        
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 1:
                if visited[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
    return sword

ans = bfs()
if ans > t:
    print('Fail')
else:
    print(ans)