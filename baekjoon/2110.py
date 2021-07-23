n, c = map(int, input().split())
x = sorted([int(input()) for _ in range(n)])

start, end = 1, x[-1] - x[0]

res = 0
while start <= end:
    mid = (start + end) // 2
    tmp = x[0]
    cnt = 1
    for i in range(1, n):
        if x[i] >= tmp + mid:
            cnt += 1
            tmp = x[i]
    
    if cnt >= c:
        start = mid + 1
        res = mid
    else:
        end = mid - 1
print(res)