from collections import defaultdict, deque
n, m, x, y = map(int, input().split())
maps = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    maps[a].append(b)
    maps[b].append(a)

if not maps[x]:
    print(-1)
    exit()

dis = [[False] * (y + 1) for _ in range(n + 1)]

def bfs(x, cnt):
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        for i in maps[x]:
            dis[i][cnt] = True

dis[x][0] = True

for i in range(0, y):
    for j in range(1, n + 1):
        if dis[j][i]:
            bfs(j, i + 1)

ans = []
for i in range(1, n + 1):
    if dis[i][y]:
        ans.append(i)

print(' '.join(map(str, ans)))