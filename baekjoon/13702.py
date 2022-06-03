n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
left, right = 1, max(arr)

tmp = 0
while left <= right:
    mid = (left + right) // 2
    t = sum(a // mid for a in arr)
    if t >= k:
        left = mid + 1
        tmp = mid
    else:
        right = mid - 1
print(tmp)