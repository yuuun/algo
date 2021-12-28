import sys
import heapq
INF = sys.maxsize

n = int(input())
cnt = 1
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def find_route(cnt):
    dis = [[INF] * n for _ in range(n)]
    queue = []
    heapq.heappush(queue, [0, 0, route[0][0]]) #x좌표, y좌표, 거리
    while queue:
        x, y, d = heapq.heappop(queue)
        if x == n - 1 and y == n - 1:
            print('Problem ' + str(cnt) + ': ' + str(d))
            return
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                nd = d + route[nx][ny]
                if nd < dis[nx][ny]:
                    dis[nx][ny] = nd
                    heapq.heappush(queue, [nx, ny, nd])


while n != 0:
    route = []
    for _ in range(n):
        route.append(list(map(int, input().split())))
    find_route(cnt)
    cnt += 1

    n = int(input())