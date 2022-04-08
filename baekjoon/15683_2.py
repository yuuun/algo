from collections import deque
n, m = map(int, input().split())

maps = []
cctv = []
visited = [[False] * m for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    maps.append(tmp)
    for j, v in enumerate(tmp):
        if v != 0 and v != 6:
            cctv.append([i, j, v])
n_cctv = len(cctv)

dir = [[],
        [[[1, 0]], [[-1, 0]], [[0, 1]], [[0, -1]]],
        [[[-1, 0], [1, 0]], [[0, -1], [0, 1]]],
        [[[-1, 0], [0, 1]], [[0, 1], [1, 0]], [[1, 0], [0, -1]], [[0, -1], [-1, 0]]],
        [[[1, 0], [-1, 0], [0, 1]], [[1, 0], [-1, 0], [0, -1]], [[0, 1], [0, -1], [1, 0]], [[0, 1], [0, -1], [-1, 0]]],
        [[[1, 0], [-1, 0], [0, 1], [0, -1]]]]
ans = 1e10
def solution(idx):
    global ans
    if idx == n_cctv:
        cnt = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and maps[i][j] == 0:
                    cnt += 1
        ans = min(ans, cnt)
        return

    x, y, d = cctv[idx]
    for dxy in dir[d]:
        q = deque()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            while 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 6:
                    break
                elif not visited[nx][ny] and maps[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                nx += dx
                ny += dy
        solution(idx + 1)
        while q:
            nx, ny = q.popleft()
            visited[nx][ny] = False
        if d == 5:
            break

solution(0)
print(ans)