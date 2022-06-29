from collections import deque

dxy = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, -1], [1, 1], [-1, 1], [-1, -1]]
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    maps = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    q = deque()
    cnt = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1 and not visited[i][j]:
                cnt += 1
                q.append([i, j])
                while q:
                    x, y = q.popleft()
                    for dx, dy in dxy:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                            visited[nx][ny] = True
                            if maps[nx][ny] == 1:
                                q.append([nx, ny])
    print(cnt)