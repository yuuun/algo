import heapq
from collections import defaultdict
import sys
INF = sys.maxsize
n = int(input())  # 도시의 개수
m = int(input())  # 버스의 개수

route = defaultdict(list)
for _ in range(m):
    s, e, c = map(int, input().split())
    route[s].append([e, c])
    
start, end = map(int, input().split())

dist = [INF] * (n + 1)

def get_min(st):
    queue = []
    heapq.heappush(queue, (st, 0))
    while queue:
        cur, dis = heapq.heappop(queue)
        if dist[cur] < dis:
            continue

        for node in route[cur]:
            cost = dis + node[1]
            if dist[node[0]] > cost:
                dist[node[0]] = cost
                heapq.heappush(queue, (node[0], cost))

get_min(start)
print(dist[end])