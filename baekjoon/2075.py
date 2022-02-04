
'''
메모리 초과
n = int(input())
nums = sorted(list(map(int, input().split())))

for _ in range(n - 1):
    tmp = list(map(int, input().split()))
    for t in tmp:
        if t < nums[0]:
            continue
        if t > nums[-1]:
            nums = nums[1:] + [t]
            continue
        for idx, num in enumerate(nums[1:]):
            if t < num:
                nums = nums[1:idx + 1] + [t] + nums[idx + 1:]
                break
print(nums[0])

'''

import heapq
n = int(input())
heap = []
for _ in range(n):
    nums = list(map(int, input().split()))
    if not heap:
        for num in nums:
            heapq.heappush(heap, num)
    else:
        for num in nums:
            if heap[0] < num:
                heapq.heappush(heap, num)
                heapq.heappop(heap)
print(heap[0])
    