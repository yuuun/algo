# TBD
from heapq import heappush, heappop

pq = []
table = []
n = int(input())
for _ in range(n):
    idx, s, e = map(int, input().split())
    heappush(pq, (s, e, idx))
for i in range(n):
    s, e, idx = heappop(pq)
    
    if len(table) == 0:
        heappush(table, (e, s, idx))
        continue

    te, ts, tidx = heappop(table)
    if te > s:
        heappush(table, (te, ts, tidx))
    heappush(table, (e, s, idx))
print(len(table))
print(table)