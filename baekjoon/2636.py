#TBD
from collections import deque
m, n = map(int, input().split())
adj = [list(map(int, input().split())) for _ in range(m)]

d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
q = deque()

area = 0
def makeSide(idx1, idx2):
    global area
    for dx, dy in d:
        tx, ty = idx1 + dx, idx2 + dy
        if 0 <= tx < m and 0 <= ty < n:
            if adj[tx][ty] == 0:
                adj[idx1][idx2] = 2
                q.append([idx1, idx2, 1])
                area += 1
                return

for idx1, ad in enumerate(adj):
    for idx2, a in enumerate(ad):
        if a == 1:
            makeSide(idx1, idx2)
cur = 0
while q:
    idx1, idx2, cnt = q.popleft()
    if cnt > cur:
        print(cnt, cur, area)
        area = 0
        cur = cnt
    for dx, dy in d:
        tx, ty = idx1 + dx, idx2 + dy
        if 0 <= tx < m and 0 <= ty < n:
            if adj[tx][ty] == 1:
                adj[tx][ty] = 2
                q.append([tx, ty, cnt + 1])
                area += 1
        adj[idx1][idx1] = 0

print(cnt, area)
