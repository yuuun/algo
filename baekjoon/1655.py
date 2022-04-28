from heapq import heappop, heappush
leftHeap = []
rightHeap = []
for _ in range(int(input())):
    n = int(input())
    if len(leftHeap) == len(rightHeap):
        heappush(leftHeap, -n)
    else:
        heappush(rightHeap, n)
    if rightHeap and -leftHeap[0] > rightHeap[0]:
        min_val = heappop(rightHeap)
        max_val = -heappop(leftHeap)
        heappush(leftHeap, -min_val)
        heappush(rightHeap, max_val)
    print(-leftHeap[0])