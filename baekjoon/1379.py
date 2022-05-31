from heapq import heappush, heappop

pq = []
n = int(input())
room = [0] * n
arr = []
for _ in range(n):
    idx, s, e = map(int, input().split())
    arr.append([s, e, idx - 1])

arr = sorted(arr, key=lambda x:(x[0]))
ans = 0
for s, e, idx in arr:
    if pq and pq[0][0] <= s:
        room[idx] = room[pq[0][2]]
        heappop(pq)
    else:
        ans += 1
        room[idx] = ans
        
    heappush(pq, [e, s, idx])
print(ans)
for i in room[1:]:
    print(i)