#tbd
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
ans = 2
while queue:
    lis = queue.pop(0)
    x, y = lis
    for dx, dy in d:
        tx, ty = x + dx, y + dy
        if 0 <= tx < n and 0 <= ty < m and adj[tx][ty] == 0:
            if adj[tx][ty] != -1:
                adj[tx][ty] = ans
                queue.append([tx, ty])
    ans += 1
print(adj)
print(ans)