from collections import deque
from heapq import heappop, heappush
import sys
n, m, fuel = map(int, input().split())

maps = [[0] * (n + 1)]
for _ in range(n):
    maps.append([0] + list(map(int, input().split())))
taxi_pos = list(map(int, input().split()))
origin, dest = [[]], [[]]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    origin.append([x1, y1])
    dest.append([x2, y2])

customers = [False for _ in range(m + 1)]
dxy =  [[0, 1], [0, -1], [1, 0], [-1, 0]]

def bfs():
    global taxi_pos, cust
    sy, sx = taxi_pos[0], taxi_pos[1]
    chk = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    dist = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]
    q = deque([])
    chk[sy][sx] = True
    dist[sy][sx] =  0
    q.append([sy, sx])
    while q:
        y, x = q.popleft()
        for dx, dy in dxy:
            ny, nx = y + dy, x + dx
            if 0 < ny <= n and 0 < nx <= n:
                if not chk[ny][nx]:
                    chk[ny][nx] = True
                    if maps[ny][nx] == 0:
                        dist[ny][nx] = dist[y][x] + 1
                        q.append([ny, nx])
    return dist

def find_cust():
    global maps, customers, fuel
    cust_dis = bfs()
    pq = []
    for i in range(1, m + 1):
        if not customers[i]:
            y, x = origin[i][0], origin[i][1]
            dist = cust_dis[y][x]
            if fuel - dist >= 0:
                heappush(pq, [dist, y, x, i])
    if not pq:
        return -1
    dist, _, _, cust_idx = heappop(pq)
    fuel -= dist
    customers[cust_idx] = True
    return cust_idx

def go_dst(cust_idx):
    global fuel
    dis = bfs()
    y, x = dest[cust_idx][0], dest[cust_idx][1]
    dist = dis[y][x]
    if fuel < dist:
        return -1
    return dist

pos = True
cnt = m
while cnt:
    cust_idx = find_cust()
    # print(fuel, cust_idx)
    if cust_idx == -1:
        pos = False
        break
    taxi_pos = origin[cust_idx]
    dist = go_dst(cust_idx)
    if dist == -1:
        pos = False
        break
    fuel += dist
    
    taxi_pos = dest[cust_idx]
    cnt -= 1

if pos:
    print(fuel)
else:
    print(-1)