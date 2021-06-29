from collections import deque
n = int(input())
d = [[2, -1], [2, 1], [-2, -1], [-2, 1],
    [1, 2], [1, -2], [-1, 2], [-1, -2]]
for _ in range(n):
    k = int(input())
    x, y = map(int, input().split())
    desx, desy = map(int, input().split())
    visited = [[0] * k for _ in range(k)]
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        if x == desx and y == desy:
            print(visited[x][y] - 1)
            break
        for dx, dy in d:
            tx, ty = x + dx, y + dy
            if 0 <= tx < k and 0 <= ty < k and visited[tx][ty] == 0:
                queue.append([tx, ty])
                visited[tx][ty] = visited[x][y] + 1