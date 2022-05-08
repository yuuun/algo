n, m = map(int, input().split())
a = list(map(int, input().split()))
left, right = 0, 1
cnt = 0
while right <= n and left <= right:
    nums = sum(a[left:right])
    if nums == m:
        cnt += 1
        right += 1
    elif nums < m:
        right += 1
    else:
        left += 1
print(cnt)