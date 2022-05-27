from heapq import heappop, heappush
n, m = map(int, input().split())

times = sorted(list(map(int, input().split())), reverse=True)
ans = []
for t in times:
    if len(ans) < m:
        heappush(ans, t)
    else:
        heappush(ans, heappop(ans) + t)
print(max(ans))