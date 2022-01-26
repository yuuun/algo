n, k = map(int, input().split())
stones = list(map(int, input().split()))

dp = [False] * (n + 1)
dp[1] = True
for i in range(1, n):
    if dp[i]:
        for j in range(i + 1, n + 1):
            if not dp[j]:
                res = (j - i) * (1 + abs(stones[j - 1] - stones[i - 1]))
                if res <= k:
                    dp[j] = True

            if dp[n]:
                print('YES')
                exit()
    if dp[n]:
        print('YES')
        exit()

print('NO')