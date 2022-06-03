s, c = map(int ,input().split())
arr = [int(input()) for _ in range(s)]
left = 1
right = max(arr)

ans = 0
k = 0
while left <= right:
    mid = (left + right) // 2
    t = sum(a // mid for a in arr)
    if t >= c:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(sum(arr) - ans * c)