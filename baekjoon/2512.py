#binary search - list의 값을 binary search하는 것이 아니라 목표 값을 searching하게 됨
n = int(input())
req = list(map(int, input().split()))
m = int(input())

low, high = 0, max(req)

while low <= high:
    mid = (low + high) // 2
    cur = 0
    for re in req:
        if re >= mid:
            cur += mid
        else:
            cur += re
    if cur <= m:
        low = mid + 1
    else:
        high = mid - 1
print(high)