import sys
from heapq import heappush, heappop
INF = sys.maxsize
n, m = map(int, input().split())

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

room = []
for _ in range(m):
    room.append(list(map(int, input())))

dis = [[INF] * n for _ in range(m)]
queue = []
heappush(queue, [0, 0, room[0][0]]) # x, y, weight

while queue:
    x, y, d = heappop(queue)
    if x == n - 1 and y == m - 1:
        break
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n:
            nd = d + room[nx][ny]
            if nd < dis[nx][ny]:
                dis[nx][ny] = nd
                heappush(queue, [nx, ny, nd])
print(dis[-1][-1])