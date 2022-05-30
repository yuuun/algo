import sys
input = sys.stdin.readline
from heapq import heappop, heappush
n = int(input())

pq = []
for _ in range(n):
    a = int(input())
    if a == 0:
        if pq:
            print(-heappop(pq))
        else:
            print(0)
    else:
        heappush(pq, -a)