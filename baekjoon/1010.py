t = int(input())

dp = [[0] * 31 for _ in range(31)] # 최댓값이 30이기 때문에
dp[0][0] = 1
for n in range(1, 31):
    dp[n][0] = 1
    for p in range(1, 31):
        dp[n][p] = dp[n - 1][p] + dp[n - 1][p - 1]

for _ in range(t):
    n, m = map(int, input().split())
    print(dp[m][n])