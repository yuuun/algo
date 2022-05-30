from heapq import heappush, heappop
n =  int(input())

q = []
for _ in range(n):
    q.append(list(map(int, input().split())))
q.sort()

pq = []
heappush(pq, q[0][1])
for i in range(1, n):
    if q[i][0] < pq[0]:
        heappush(pq, q[i][1])
    else:
        heappop(pq)
        heappush(pq, q[i][1])
print(len(pq))