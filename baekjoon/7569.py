from collections import deque
m, n, h = map(int, input().split())
adj = [[[0] * m for _ in range(n)] for _ in range(h)]

q = deque()

for k in range(h):
    for j in range(n):
        ad = list(map(int, input().split()))
        adj[k][j] = ad
        for idx, val in enumerate(ad):
            if val == 1:
                q.append([k, j, idx])
        
d = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], 
    [0, -1, 0], [0, 0, 1], [0, 0, -1]]

while q:
    z, y, x = q.popleft()
    for dz, dy, dx in d:
        tz, ty, tx = z + dz, y + dy, x + dx
        if 0 <= tz < h and 0 <= ty < n and 0 <= tx < m:
            if adj[tz][ty][tx] == 0:
                adj[tz][ty][tx] = adj[z][y][x] + 1
                q.append([tz, ty, tx])

def print_val(adj):
    max_val = 0
    for ad in adj:
        for a in ad:
            if 0 in a:
                return -1
            for i in a:
                if max_val < i:
                    max_val = i
    return max_val - 1

print(print_val(adj))