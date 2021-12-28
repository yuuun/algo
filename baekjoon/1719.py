#TBD
import heapq
import sys
from collections import defaultdict
INF = sys.maxsize
n, m = map(int, input().split())
route = defaultdict(list)

for _ in range(m):
    s, e, c = map(int, input().split())
    route[s].append([e, c])
    route[e].append([s, c])

def get_min(st):
    queue = []
    first = ['-' for _ in range(n + 1)]
    heapq.heappush(queue, (st, 0))
    while queue:
        cur, dis = heapq.heappop(queue)
        if dist[cur] < dis:
            continue
        for node in route[cur]:
            cost = dis + node[1]
            if dist[node[0]] > cost:
                first[node[0]] = cur
                dist[node[0]] = cost
                heapq.heappush(queue, (node[0], cost))
    print(dist)
    return first[1:]

for i in range(1, n + 1):
    dist = [INF] * (n + 1)
    ans = get_min(i)
    
    print(' '.join(map(str, ans)))
        