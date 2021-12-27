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

def get_min(st):
    queue = []
    heapq.heappush(queue, (st, 0))
    while queue:
        cur, dis = heapq.heappop(queue)
        if dist[cur] < dis:
            continue
        for node in route[st]:
            cost = dis + node[1]
            if dist[node[0]] > cost:
                dist[node[0]] = cost
                heapq.heappush(queue, (node[0], cost))



for i in range(1, n + 1):
    dist = [INF] * (n + 1)
    get_min(i)
    ans = []
    for j in range(1, n + 1):
        if i == j: 
           ans.append('-')
        else:
            ans.append(str(dist[j]))
    print(' '.join(map(str, ans)))
        