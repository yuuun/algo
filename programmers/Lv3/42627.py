from heapq import heappop, heappush
def solution(jobs):
    heap = []
    cur = 1e10
    for t, dur in jobs:
        heappush(heap, [dur, t])
        if cur > t:
            cur = t

    ans = 0
    tmp = []
    while heap:
        while heap and cur < heap[0][1]:
            dur, t = heappop(heap)
            heappush(tmp, [dur, t])
        if not heap:
            cur += 1
        else:
            dur, t = heappop(heap)
            cur += dur
            ans += (cur - t)
        
        while tmp:
            t = heappop(tmp)
            heappush(heap, t)

    return ans // len(jobs)