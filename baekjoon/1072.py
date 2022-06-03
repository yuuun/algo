x, y = map(int, input().split())
z = (y * 100) // x
if z >= 99:
    print(-1)
else:
    answer = 1e20
    left = 1
    right = x
    while left <= right:
        mid = (left + right) // 2
        if (y + mid) * 100 // (x + mid) <= z:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
    print(answer)