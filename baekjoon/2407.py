n, m = map(int, input().split())
m = min(m, n - m)

dp = [[0] * (m + 1) for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    dp[i][1] = i + 1
    dp[i][0] = 1
    
for i in range(1, n):
    for j in range(1, (m + 1)):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
print(dp[-1][-1])