n = int(input())
if n == 1 or n == 3:
    print(-1)
else:
    t = n % 5
    if t % 2 == 0:
        ans = n // 5 + t // 2
    else:
        ans = n // 5 - 1 + (t + 5) // 2
    print(ans)