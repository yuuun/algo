#시간 초과,...
m, n = map(int, input().split())
adj = []
queue = []
cnt = 1
for x in range(n):
    tmp = list(map(int, input().split()))
    adj.append(tmp)
    for idx, t in enumerate(tmp):
        if t == 1:
            queue.append([x, idx])
              
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
while queue:
    lis = queue.pop(0)
    x, y = lis
    for dx, dy in d:
        tx, ty = x + dx, y + dy
        if 0 <= tx < n and 0 <= ty < m and adj[tx][ty] == 0:
            adj[tx][ty] = adj[x][y] + 1
            queue.append([tx, ty])

max_val = 0
for ad in adj:
    if 0 in ad:
        print(-1)
        break
    for a in ad:
        if max_val < a:
            max_val = a
print(max_val - 1)