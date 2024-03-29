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
    dist = [INF] * (n + 1)
    dist[st] = 0
    while queue:
        cur, dis = heapq.heappop(queue)
        if dist[cur] < dis:
            continue
        for ne, nd in route[cur]:
            cost = dis + nd
            if dist[ne] > cost:
                first[ne] = cur
                dist[ne] = cost
                heapq.heappush(queue, (ne, cost))
    return first[1:]

ans = []
for i in range(1, n + 1):
    
    ans.append(get_min(i))

for i in range(len(ans)):
    for j in range(len(ans)):
        print(str(ans[j][i]), end=' ')
    print()