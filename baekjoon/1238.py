import heapq
import sys
from collections import defaultdict
INF = sys.maxsize

n, m, x = map(int, input().split())
route = defaultdict(list)

for _ in range(m):
    s, e, c = map(int, input().split())
    route[s].append([e, c])


def get_min(st):
    queue = []
    heapq.heappush(queue, (st, 0))
    dist = [INF] * (n + 1)
    # dist[st] = 0
    
    while queue:
        cur, dis = heapq.heappop(queue)
        if dist[cur] < dis:
            continue
        for ne, nd in route[cur]:
            cost = dis + nd
            if dist[ne] > cost:
                dist[ne] = cost
                heapq.heappush(queue, (ne, cost))
    return dist[1:]

distance = []
for i in range(1, n + 1):
    distance.append(get_min(i))

ans = []
for i in range(n):
    ans.append(distance[i][x] + distance[x][i])
print(max(ans))