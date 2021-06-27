n, m = map(int, input().split())
adj = [list(input()) for _ in range(n)]

d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
def bfs():
    adj[0][0] = 1
    queue = [[0, 0]]
    while queue:
        x, y = queue.pop(0)
        for dx, dy in d:
            tx, ty = x + dx, y + dy
            if 0 <= tx < n and 0 <= ty < m and adj[tx][ty] == '1':
                queue.append([tx, ty])
                adj[tx][ty] = adj[x][y] + 1
    return adj[-1][-1]

print(bfs())