from heapq import heappop, heappush
n = int(input())
if n == 1:
    input()
    print(0)
else:
    pq = []
    ans = 0

    for _ in range(n):
        heappush(pq, int(input()))

    while len(pq) > 1:
        a, b = heappop(pq), heappop(pq)
        z = a + b
        ans += z
        heappush(pq, z)
    print(ans)