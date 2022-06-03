for _ in range(int(input())):
    n = int(input())
    left = 1
    right = int(n ** 0.5 * 2)
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if mid * (mid + 1) <= 2 * n:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    print(ans)